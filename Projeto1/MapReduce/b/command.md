COMMAND:

    hadoop jar  $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -input /user/italo/projeto/input/words.txt -output /user/italo/projeto/b/output/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file MapReduce/b/mapper.py -file MapReduce/b/reducer.py

LOG:

    2022-08-06 11:15:33,185 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
    packageJobJar: [MapReduce/b/mapper.py, MapReduce/b/reducer.py, /tmp/hadoop-unjar283893411761866907/] [] /tmp/streamjob4493361660991330700.jar tmpDir=null
    2022-08-06 11:15:35,489 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 11:15:36,082 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 11:15:36,581 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/italo/.staging/job_1659792899936_0002
    2022-08-06 11:15:37,233 INFO mapred.FileInputFormat: Total input files to process : 1
    -types.xml'.
    2022-08-06 11:15:38,096 INFO impl.YarnClientImpl: Submitted application applib: job_1659792899936_0002cation_1659792899936_0002                                                    ]
    2022-08-06 11:15:38,191 INFO mapreduce.Job: The url to track the job: http://DESKTOP-QCCMFLA.localdomain:8088/proxy/application_1659792899936_0002/       -types.xml'.
    2022-08-06 11:15:38,195 INFO mapreduce.Job: Running job: job_1659792899936_00cation_1659792899936_000202                                                                           DESKTOP-QCCMFLA.localdomain:8088/proxy/application_1659792899936_0002/
    2022-08-06 11:15:51,356 INFO mapreduce.Job: Job job_1659792899936_0002 runnin02g in uber mode : false                                                       g in uber mode : false
    2022-08-06 11:15:51,357 INFO mapreduce.Job:  map 0% reduce 0%
    2022-08-06 11:16:11,484 INFO mapreduce.Job:  map 6% reduce 0%
    2022-08-06 11:16:17,508 INFO mapreduce.Job:  map 8% reduce 0%
    2022-08-06 11:16:23,528 INFO mapreduce.Job:  map 12% reduce 0%
    2022-08-06 11:16:29,545 INFO mapreduce.Job:  map 13% reduce 0%
    2022-08-06 11:16:30,548 INFO mapreduce.Job:  map 14% reduce 0%
    2022-08-06 11:16:35,561 INFO mapreduce.Job:  map 16% reduce 0%
    2022-08-06 11:16:36,595 INFO mapreduce.Job:  map 18% reduce 0%
    2022-08-06 11:16:37,599 INFO mapreduce.Job:  map 19% reduce 0%
    2022-08-06 11:16:55,692 INFO mapreduce.Job:  map 25% reduce 0%
    2022-08-06 11:17:01,711 INFO mapreduce.Job:  map 27% reduce 0%
    2022-08-06 11:17:08,685 INFO mapreduce.Job:  map 29% reduce 0%
    2022-08-06 11:17:09,688 INFO mapreduce.Job:  map 30% reduce 0%
    2022-08-06 11:17:43,118 INFO mapreduce.Job:  map 31% reduce 0%
    2022-08-06 11:18:11,501 INFO mapreduce.Job:  map 32% reduce 0%
    2022-08-06 11:18:15,510 INFO mapreduce.Job:  map 33% reduce 0%
    2022-08-06 11:18:26,536 INFO mapreduce.Job:  map 34% reduce 0%
    2022-08-06 11:18:44,360 INFO mapreduce.Job:  map 35% reduce 0%
    2022-08-06 11:18:58,588 INFO mapreduce.Job:  map 36% reduce 0%
    2022-08-06 11:19:13,143 INFO mapreduce.Job:  map 37% reduce 0%
    2022-08-06 11:19:15,148 INFO mapreduce.Job:  map 38% reduce 0%
    2022-08-06 11:19:40,761 INFO mapreduce.Job:  map 42% reduce 13%
    2022-08-06 11:19:46,777 INFO mapreduce.Job:  map 44% reduce 13%
    2022-08-06 11:19:52,520 INFO mapreduce.Job:  map 45% reduce 13%
    2022-08-06 11:19:53,522 INFO mapreduce.Job:  map 46% reduce 13%
    2022-08-06 11:20:03,802 INFO mapreduce.Job:  map 47% reduce 13%
    2022-08-06 11:21:50,552 INFO mapreduce.Job:  map 48% reduce 13%
    2022-08-06 11:22:16,211 INFO mapreduce.Job:  map 49% reduce 13%
    2022-08-06 11:22:28,229 INFO mapreduce.Job:  map 50% reduce 13%
    2022-08-06 11:22:55,914 INFO mapreduce.Job:  map 51% reduce 13%
    2022-08-06 11:23:19,461 INFO mapreduce.Job:  map 52% reduce 13%
    2022-08-06 11:23:20,463 INFO mapreduce.Job:  map 53% reduce 13%
    2022-08-06 11:23:22,467 INFO mapreduce.Job:  map 53% reduce 18%
    2022-08-06 11:23:42,517 INFO mapreduce.Job:  map 57% reduce 18%
    2022-08-06 11:23:51,530 INFO mapreduce.Job:  map 58% reduce 18%
    2022-08-06 11:23:54,535 INFO mapreduce.Job:  map 59% reduce 18%
    2022-08-06 11:23:57,540 INFO mapreduce.Job:  map 60% reduce 18%
    2022-08-06 11:24:00,546 INFO mapreduce.Job:  map 62% reduce 18%
    2022-08-06 11:24:06,556 INFO mapreduce.Job:  map 63% reduce 18%
    2022-08-06 11:24:09,562 INFO mapreduce.Job:  map 64% reduce 18%
    2022-08-06 11:24:10,569 INFO mapreduce.Job:  map 65% reduce 18%
    2022-08-06 11:24:11,571 INFO mapreduce.Job:  map 67% reduce 18%
    2022-08-06 11:24:12,573 INFO mapreduce.Job:  map 68% reduce 18%
    2022-08-06 11:24:15,578 INFO mapreduce.Job:  map 69% reduce 22%
    2022-08-06 11:24:21,596 INFO mapreduce.Job:  map 69% reduce 23%
    2022-08-06 11:31:30,452 INFO mapreduce.Job:  map 70% reduce 23%
    2022-08-06 11:33:27,957 INFO mapreduce.Job:  map 71% reduce 23%
    2022-08-06 11:33:38,725 INFO mapreduce.Job:  map 73% reduce 23%
    2022-08-06 11:33:45,736 INFO mapreduce.Job:  map 74% reduce 23%
    2022-08-06 11:33:52,747 INFO mapreduce.Job:  map 78% reduce 23%
    2022-08-06 11:33:58,758 INFO mapreduce.Job:  map 80% reduce 23%
    2022-08-06 11:34:07,617 INFO mapreduce.Job:  map 82% reduce 23%
    2022-08-06 11:34:09,620 INFO mapreduce.Job:  map 83% reduce 23%
    2022-08-06 11:34:21,772 INFO mapreduce.Job:  map 84% reduce 23%
    2022-08-06 11:34:34,587 INFO mapreduce.Job:  map 84% reduce 28%
    2022-08-06 11:35:11,864 INFO mapreduce.Job:  map 85% reduce 28%
    2022-08-06 11:37:34,179 INFO mapreduce.Job:  map 86% reduce 28%
    2022-08-06 11:38:50,637 INFO mapreduce.Job:  map 87% reduce 28%
    2022-08-06 11:39:32,725 INFO mapreduce.Job:  map 88% reduce 28%
    2022-08-06 11:39:51,630 INFO mapreduce.Job:  map 89% reduce 28%
    2022-08-06 11:40:02,647 INFO mapreduce.Job:  map 90% reduce 28%
    2022-08-06 11:40:03,649 INFO mapreduce.Job:  map 91% reduce 28%
    2022-08-06 11:40:04,650 INFO mapreduce.Job:  map 92% reduce 28%
    2022-08-06 11:40:05,652 INFO mapreduce.Job:  map 93% reduce 28%
    2022-08-06 11:40:10,740 INFO mapreduce.Job:  map 94% reduce 28%
    2022-08-06 11:40:18,431 INFO mapreduce.Job:  map 95% reduce 28%
    2022-08-06 11:40:24,223 INFO mapreduce.Job:  map 97% reduce 28%
    2022-08-06 11:40:28,229 INFO mapreduce.Job:  map 98% reduce 28%
    2022-08-06 11:40:32,825 INFO mapreduce.Job:  map 99% reduce 28%
    2022-08-06 11:40:34,829 INFO mapreduce.Job:  map 99% reduce 29%
    2022-08-06 11:40:36,837 INFO mapreduce.Job:  map 100% reduce 29%
    2022-08-06 11:40:40,843 INFO mapreduce.Job:  map 100% reduce 33%
    2022-08-06 11:41:34,917 INFO mapreduce.Job:  map 100% reduce 46%
    2022-08-06 11:41:40,925 INFO mapreduce.Job:  map 100% reduce 59%
    2022-08-06 11:41:46,932 INFO mapreduce.Job:  map 100% reduce 67%
    2022-08-06 11:41:52,940 INFO mapreduce.Job:  map 100% reduce 68%
    2022-08-06 11:41:58,948 INFO mapreduce.Job:  map 100% reduce 69%
    2022-08-06 11:42:04,955 INFO mapreduce.Job:  map 100% reduce 70%
    2022-08-06 11:42:10,963 INFO mapreduce.Job:  map 100% reduce 71%
    2022-08-06 11:42:16,971 INFO mapreduce.Job:  map 100% reduce 72%
    2022-08-06 11:42:22,979 INFO mapreduce.Job:  map 100% reduce 74%
    2022-08-06 11:42:28,986 INFO mapreduce.Job:  map 100% reduce 75%
    2022-08-06 11:42:34,994 INFO mapreduce.Job:  map 100% reduce 76%
    2022-08-06 11:42:41,001 INFO mapreduce.Job:  map 100% reduce 77%
    2022-08-06 11:42:48,254 INFO mapreduce.Job:  map 100% reduce 79%
    2022-08-06 11:42:59,295 INFO mapreduce.Job:  map 100% reduce 80%
    2022-08-06 11:43:05,303 INFO mapreduce.Job:  map 100% reduce 81%
    2022-08-06 11:43:11,310 INFO mapreduce.Job:  map 100% reduce 82%
    2022-08-06 11:43:17,318 INFO mapreduce.Job:  map 100% reduce 83%
    2022-08-06 11:43:29,333 INFO mapreduce.Job:  map 100% reduce 84%
    2022-08-06 11:44:07,514 INFO mapreduce.Job:  map 100% reduce 85%
    2022-08-06 11:44:44,023 INFO mapreduce.Job:  map 100% reduce 86%
    2022-08-06 11:44:50,030 INFO mapreduce.Job:  map 100% reduce 87%
    2022-08-06 11:45:08,052 INFO mapreduce.Job:  map 100% reduce 89%
    2022-08-06 11:45:14,060 INFO mapreduce.Job:  map 100% reduce 90%
    2022-08-06 11:45:20,070 INFO mapreduce.Job:  map 100% reduce 91%
    2022-08-06 11:45:26,078 INFO mapreduce.Job:  map 100% reduce 92%
    2022-08-06 11:45:32,088 INFO mapreduce.Job:  map 100% reduce 93%
    2022-08-06 11:45:58,149 INFO mapreduce.Job:  map 100% reduce 94%
    2022-08-06 11:46:04,157 INFO mapreduce.Job:  map 100% reduce 95%
    2022-08-06 11:46:10,165 INFO mapreduce.Job:  map 100% reduce 96%
    2022-08-06 11:46:17,174 INFO mapreduce.Job:  map 100% reduce 97%
    2022-08-06 11:46:23,204 INFO mapreduce.Job:  map 100% reduce 98%
    2022-08-06 11:46:29,213 INFO mapreduce.Job:  map 100% reduce 99%
    2022-08-06 11:46:35,221 INFO mapreduce.Job:  map 100% reduce 100%
    2022-08-06 11:46:36,400 INFO mapred.ClientServiceDelegate: Application state 
    is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 11:46:37,450 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:38,450 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:39,451 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:40,452 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:41,452 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:42,453 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:43,454 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:44,455 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:45,455 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:46,456 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:46,567 INFO mapred.ClientServiceDelegate: Application state 
    is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 11:46:47,567 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:48,568 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:49,569 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:50,569 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:51,570 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:52,570 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:53,571 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:54,572 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:55,572 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:56,573 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:56,679 INFO mapred.ClientServiceDelegate: Application state 
    is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 11:46:57,680 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:58,681 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:46:59,682 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:00,682 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:01,683 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:02,683 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:03,684 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:04,684 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:05,685 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:06,685 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 11:47:06,786 ERROR streaming.StreamJob: Error Launching job : java.net.ConnectException: Your endpoint configuration is wrong; For more details see:  http://wiki.apache.org/hadoop/UnsetHostnameOrPort
    Streaming Command Failed!

OBS:

    Houve Falha de conexão no fim mas o job deu como SUCCEEDED no servidor de verificação de status da job, na porta 8088, vide anexo nesta pasta