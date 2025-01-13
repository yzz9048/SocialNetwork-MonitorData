Device:
We deploy the microservice benchmark socialNetwork on two servers (node1:Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz and node2：Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz), and run the workload script and collect data on the master server node3:Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz. 

Workload:
The workload script (locust.py) is a compose-post request implemented by locust. Specifically, we continue to simulate 100 users, with each user sending requests at a rate of 1rps.

Folder:
The folder "normal" records monitoring data for 8 hours of continuous normal workload.
The folder "pod" and "node" represent the faults injected into pod and server, respectively. Specifically, each "time" folder represents an experiment. The time in "log" folder is UTC+0, and you have to add 8h when fusing data to align the time with the metric/trace. The specific execution time of all experiments is as follows:

"pod/cpu_leak/time1" : 2025-1-9T15:10 to 2025-1-9T15:20

"pod/cpu_leak/time2" : 2025-1-9T15:31 to 2025-1-9T15:41

"pod/cpu_leak/time3" : 2025-1-9T15:50 to 2025-1-9T16:00

"node/cpu_leak/time1" : 2025-1-9T16:30 to 2025-1-9T16:40

"node/cpu_leak/time2" : 2025-1-9T16:50 to 2025-1-9T17:00

"node/cpu_leak/time3" : 2025-1-9T17:10 to 2025-1-9T17:20

"pod/memory_leak/time1" : 2025-1-10T10:30 to 2025-1-10T10:40

"pod/memory_leak/time2" : 2025-1-10T10:50 to 2025-1-10T11:00

"pod/memory_leak/time3" : 2025-1-10T11:10 to 2025-1-10T11:20

"node/memory_leak/time1" : 2025-1-10T14:21 to 2025-1-10T14:31

"node/memory_leak/time2" : 2025-1-10T15:00 to 2025-1-10T15:10

"node/memory_leak/time3" : 2025-1-10T15:40 to 2025-1-10T15:50

"normal": 2025-1-11T10:20 to 2025-1-11T18:20

To simulate container CPU resource leakage failure, starting from the second minute in each experiment, we inject 1-core CPU resource usage into one of the pods every 20 seconds. The injection process for container memory leakage failure, server CPU leakage failure, and server memory leakage failure has been explained in the paper (Readers can start creating data labels yourselves from the second minute , if necessary).  Specifically, we inject faults into pod user-timeline-service-fb5ffbd4-6q2nn and node2 respectively. Attention please, due to the design of the chaos tool ChaosBlade itself, the experiment simulating memory leaks occupied all node resources and was automatically destroyed in the 5th minute of fault injection.
