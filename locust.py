from locust import HttpUser, task, between
#from multiprocessing import shared_memory
import random
import logging
import time

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

charset = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
  'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q',
  'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H',
  'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5',
  '6', '7', '8', '9', '0']

decset = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
task_name = "dsb-sn"
mcr_name = "locust_client_mcr_" + task_name
max_user_index = 962 # 81306 465017

time_ratio = 1

mcr = 1

def stringRandom(l):
    s = [charset[random.randint(0,len(charset)-1)] for _ in range(l)]
    return ''.join(s)


def decRandom(l):
    s = [decset[random.randint(0,len(decset)-1)] for _ in range(l)]
    return ''.join(s)


class WebsiteUser(HttpUser):
    last_mcr = 1
    last_end_time = 0
    last_wait_time = 0
    first_start = True

    def wait_time(self):
        this_time = time.time()

        midt = time_ratio
        if midt >= 60:
            midt = 60
        midt = between(midt*0.7, midt*1.3)(0)

        if self.last_end_time != 0:
            midt -= this_time - self.last_end_time - self.last_wait_time
        self.last_wait_time = midt
        self.last_end_time = this_time
        if midt < 0:
            midt = 0

        return midt
    
    
    @task(1)
    def compost_post(self):
        if self.first_start:
            self.first_start = False
        #    time.sleep(random.random()*time_ratio*6)
        user_index = random.randint(0, max_user_index - 1)
        user_id = str(user_index)
        username = "username_" + user_id
        text = stringRandom(256)
        num_user_mentions = random.randint(0, 5)
        num_urls = random.randint(0, 5)
        num_media = random.randint(0, 4)
        media_ids = '['
        media_types = '['

        for _ in range(num_user_mentions):
            user_mention_id = random.randint(0, max_user_index - 1)
            while user_index == user_mention_id:
                user_mention_id = random.randint(0, max_user_index - 1)
            text = text + " @username_" + str(user_mention_id)
            
        for _ in range(num_urls):
            text = text + " http://" + stringRandom(64)

        for _ in range(num_media):
            media_id = decRandom(18)
            media_ids = media_ids + '"' + media_id + '",'
            media_types = media_types + '"png",'

        media_ids = media_ids[:-1] + "]"
        media_types = media_types[:-1] + "]"
        path = "/wrk2-api/post/compose"
        headers = {}
        body = ""
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        if num_media:
            body = f"username={username}&user_id={user_id}&text={text}&media_ids={media_ids}&media_types={media_types}&post_type=0"
        else:
            body = f"username={username}&user_id={user_id}&text={text}&post_type=0"
        self.client.post(path, body)