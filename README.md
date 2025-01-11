Device:
We deploy the microservice benchmark socialNetwork on two servers (node1:Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz and node2：Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz), and run the workload script and collect data on the master server node3:Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz. 
Workload:
The workload script (locust.py) is a compose-post request implemented by locust. Specifically, we continue to simulate 100 users, with each user sending requests at a rate of 1rps.
Folder:
The folder "normal" records monitoring data for 8 hours of continuous normal workload.
The folder "pod" and "node" represent the faults injected into pod and server, respectively. Specifically, each "time" folder represents an experiment.
To simulate container CPU resource leakage failure, starting from the second minute in each experiment, we inject 1-core CPU resource usage into one of the pods every 20 seconds. The injection process for container memory leakage failure, server CPU leakage failure, and server memory leakage failure has been explained in the paper (Readers can start creating data labels yourselves from the second minute , if necessary).  
