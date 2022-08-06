COMMAND:

    hadoop jar  $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -input /user/italo/projeto/input/words.txt -output /user/italo/projeto/a/output/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file MapReduce/a/mapper.py -file MapReduce/a/reducer.py

LOG:

    2022-08-06 10:52:09,892 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
    packageJobJar: [MapReduce/a/mapper.py, MapReduce/a/reducer.py, /tmp/hadoop-unjar8769587561294430760/] [] /tmp/streamjob617406548408073167.jar tmpDir=null
    2022-08-06 10:52:12,292 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 10:52:12,923 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 10:52:13,492 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/italo/.staging/job_1659792899936_0001
    2022-08-06 10:52:14,395 INFO mapred.FileInputFormat: Total input files to process : 1
    2022-08-06 10:52:14,502 INFO mapreduce.JobSubmitter: number of splits:32
    2022-08-06 10:52:14,632 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1659792899936_0001
    2022-08-06 10:52:14,632 INFO mapreduce.JobSubmitter: Executing with tokens: []
    2022-08-06 10:52:15,062 INFO conf.Configuration: resource-types.xml not found
    2022-08-06 10:52:15,064 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
    2022-08-06 10:52:15,764 INFO impl.YarnClientImpl: Submitted application application_1659792899936_0001
    2022-08-06 10:52:15,866 INFO mapreduce.Job: The url to track the job: http://DESKTOP-QCCMFLA.localdomain:8088/proxy/application_1659792899936_0001/
    2022-08-06 10:52:15,870 INFO mapreduce.Job: Running job: job_1659792899936_0001
    2022-08-06 10:52:37,044 INFO mapreduce.Job: Job job_1659792899936_0001 running in uber mode : false
    2022-08-06 10:52:37,045 INFO mapreduce.Job:  map 0% reduce 0%
    2022-08-06 10:53:01,060 INFO mapreduce.Job:  map 3% reduce 0%
    2022-08-06 10:53:11,472 INFO mapreduce.Job:  map 9% reduce 0%
    2022-08-06 10:53:18,143 INFO mapreduce.Job:  map 13% reduce 0%
    2022-08-06 10:53:20,245 INFO mapreduce.Job:  map 14% reduce 0%
    2022-08-06 10:53:22,251 INFO mapreduce.Job:  map 15% reduce 0%
    2022-08-06 10:53:23,254 INFO mapreduce.Job:  map 19% reduce 0%
    2022-08-06 10:53:44,332 INFO mapreduce.Job:  map 20% reduce 0%
    2022-08-06 10:53:45,334 INFO mapreduce.Job:  map 22% reduce 0%
    2022-08-06 10:53:49,562 INFO mapreduce.Job:  map 29% reduce 0%
    2022-08-06 10:53:54,587 INFO mapreduce.Job:  map 30% reduce 0%
    2022-08-06 10:53:56,592 INFO mapreduce.Job:  map 31% reduce 0%
    2022-08-06 10:53:57,596 INFO mapreduce.Job:  map 35% reduce 0%
    2022-08-06 10:53:58,599 INFO mapreduce.Job:  map 38% reduce 0%
    2022-08-06 10:54:17,654 INFO mapreduce.Job:  map 44% reduce 0%
    2022-08-06 10:54:18,656 INFO mapreduce.Job:  map 46% reduce 13%
    2022-08-06 10:54:20,295 INFO mapreduce.Job:  map 48% reduce 13%
    2022-08-06 10:54:24,305 INFO mapreduce.Job:  map 49% reduce 13%
    2022-08-06 10:54:29,317 INFO mapreduce.Job:  map 50% reduce 13%
    2022-08-06 10:54:30,320 INFO mapreduce.Job:  map 52% reduce 14%
    2022-08-06 10:54:32,326 INFO mapreduce.Job:  map 53% reduce 14%
    2022-08-06 10:54:36,339 INFO mapreduce.Job:  map 53% reduce 18%
    2022-08-06 10:54:49,139 INFO mapreduce.Job:  map 57% reduce 18%
    2022-08-06 10:54:51,143 INFO mapreduce.Job:  map 58% reduce 18%
    2022-08-06 10:54:55,152 INFO mapreduce.Job:  map 62% reduce 18%
    2022-08-06 10:54:57,157 INFO mapreduce.Job:  map 63% reduce 18%
    2022-08-06 10:54:59,162 INFO mapreduce.Job:  map 64% reduce 18%
    2022-08-06 10:55:00,164 INFO mapreduce.Job:  map 66% reduce 19%
    2022-08-06 10:55:01,167 INFO mapreduce.Job:  map 68% reduce 19%
    2022-08-06 10:55:07,418 INFO mapreduce.Job:  map 69% reduce 23%
    2022-08-06 10:56:23,168 INFO mapreduce.Job:  map 70% reduce 23%
    2022-08-06 10:56:28,184 INFO mapreduce.Job:  map 77% reduce 23%
    2022-08-06 10:56:34,195 INFO mapreduce.Job:  map 82% reduce 23%
    2022-08-06 10:56:37,201 INFO mapreduce.Job:  map 83% reduce 23%
    2022-08-06 10:56:39,205 INFO mapreduce.Job:  map 84% reduce 23%
    2022-08-06 10:56:40,207 INFO mapreduce.Job:  map 84% reduce 27%
    2022-08-06 10:56:46,221 INFO mapreduce.Job:  map 84% reduce 28%
    2022-08-06 10:56:58,407 INFO mapreduce.Job:  map 87% reduce 28%
    2022-08-06 10:57:16,198 INFO mapreduce.Job:  map 92% reduce 28%
    2022-08-06 10:57:22,217 INFO mapreduce.Job:  map 93% reduce 28%
    2022-08-06 10:57:23,219 INFO mapreduce.Job:  map 95% reduce 28%
    2022-08-06 10:57:27,226 INFO mapreduce.Job:  map 98% reduce 28%
    2022-08-06 10:57:28,228 INFO mapreduce.Job:  map 100% reduce 30%
    2022-08-06 10:57:34,239 INFO mapreduce.Job:  map 100% reduce 33%
    2022-08-06 10:58:04,291 INFO mapreduce.Job:  map 100% reduce 42%
    2022-08-06 10:58:10,345 INFO mapreduce.Job:  map 100% reduce 56%
    2022-08-06 10:58:16,354 INFO mapreduce.Job:  map 100% reduce 67%
    2022-08-06 11:00:51,584 INFO mapreduce.Job:  map 100% reduce 100%
    2022-08-06 11:00:51,695 INFO mapred.ClientServiceDelegate: Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 11:00:52,707 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:53,708 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:54,708 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:55,709 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:56,709 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:57,710 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:58,711 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:00:59,711 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:00,712 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:01,712 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:01,815 INFO mapred.ClientServiceDelegate: Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 11:01:02,816 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:03,816 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:04,817 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:05,817 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:06,818 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:07,818 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:08,819 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:09,819 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:10,820 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:11,820 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:11,923 INFO mapred.ClientServiceDelegate: Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 11:01:12,924 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:13,924 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:14,925 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:15,925 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:16,926 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:17,927 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:18,927 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:19,928 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:20,928 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:21,929 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)2022-08-06 11:01:22,029 ERROR streaming.StreamJob: Error Launching job : java.net.ConnectException: Your endpoint configuration is wrong; For more details see:  http://wiki.apache.org/hadoop/UnsetHostnameOrPort
    Streaming Command Failed!

OBS:

    Houve Falha de conexão mas o job deu como SUCCEEDED no servidor de verificação de status da job, na porta 8088, vide anexo nesta pasta