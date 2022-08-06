COMMAND:

    hadoop jar  $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -input /user/italo/projeto/input/words.txt -output /user/italo/projeto/b/output/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file MapReduce/b/mapper.py -file MapReduce/b/reducer.py

LOG:

    2022-08-06 11:52:57,120 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
    2022-08-06 11:52:59,392 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 11:52:59,984 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 11:53:00,539 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/italo/.staging/job_1659792899936_0003
    2022-08-06 11:53:01,227 INFO mapred.FileInputFormat: Total input files to process : 1
    2022-08-06 11:53:01,314 INFO mapreduce.JobSubmitter: number of splits:32
    2022-08-06 11:53:01,429 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1659792899936_0003
    2022-08-06 11:53:01,429 INFO mapreduce.JobSubmitter: Executing with tokens: []
    2022-08-06 11:53:01,839 INFO conf.Configuration: resource-types.xml not found
    2022-08-06 11:53:01,840 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
    2022-08-06 11:53:01,983 INFO impl.YarnClientImpl: Submitted application application_1659792899936_0003
    2022-08-06 11:53:02,104 INFO mapreduce.Job: The url to track the job: http://DESKTOP-QCCMFLA.localdomain:8088/proxy/application_1659792899936_0003/
    2022-08-06 11:53:02,110 INFO mapreduce.Job: Running job: job_1659792899936_0003
    2022-08-06 11:53:15,273 INFO mapreduce.Job: Job job_1659792899936_0003 running in uber mode : false
    2022-08-06 11:53:15,274 INFO mapreduce.Job:  map 0% reduce 0%
    2022-08-06 11:53:36,924 INFO mapreduce.Job:  map 2% reduce 0%
    2022-08-06 11:53:37,929 INFO mapreduce.Job:  map 3% reduce 0%
    2022-08-06 11:53:38,932 INFO mapreduce.Job:  map 6% reduce 0%
    2022-08-06 11:53:48,479 INFO mapreduce.Job:  map 7% reduce 0%
    2022-08-06 11:53:57,080 INFO mapreduce.Job:  map 8% reduce 0%
    2022-08-06 11:54:05,681 INFO mapreduce.Job:  map 9% reduce 0%
    2022-08-06 11:54:12,380 INFO mapreduce.Job:  map 11% reduce 0%
    2022-08-06 11:54:23,714 INFO mapreduce.Job:  map 12% reduce 0%
    2022-08-06 11:54:54,338 INFO mapreduce.Job:  map 13% reduce 0%
    2022-08-06 11:55:07,638 INFO mapreduce.Job:  map 14% reduce 0%
    2022-08-06 11:55:08,640 INFO mapreduce.Job:  map 15% reduce 0%
    2022-08-06 11:55:09,643 INFO mapreduce.Job:  map 16% reduce 0%
    2022-08-06 11:55:10,647 INFO mapreduce.Job:  map 17% reduce 0%
    2022-08-06 11:55:11,651 INFO mapreduce.Job:  map 19% reduce 0%
    2022-08-06 11:55:27,700 INFO mapreduce.Job:  map 25% reduce 0%
    2022-08-06 11:55:29,705 INFO mapreduce.Job:  map 29% reduce 0%
    2022-08-06 11:55:30,709 INFO mapreduce.Job:  map 31% reduce 0%
    2022-08-06 11:55:31,715 INFO mapreduce.Job:  map 34% reduce 0%
    2022-08-06 11:55:33,722 INFO mapreduce.Job:  map 38% reduce 0%
    2022-08-06 11:55:51,462 INFO mapreduce.Job:  map 41% reduce 13%
    2022-08-06 11:55:56,481 INFO mapreduce.Job:  map 44% reduce 13%
    2022-08-06 11:55:57,484 INFO mapreduce.Job:  map 45% reduce 13%
    2022-08-06 11:56:05,797 INFO mapreduce.Job:  map 47% reduce 13%
    2022-08-06 11:56:19,200 INFO mapreduce.Job:  map 48% reduce 13%
    2022-08-06 11:56:24,209 INFO mapreduce.Job:  map 49% reduce 13%
    2022-08-06 11:56:43,437 INFO mapreduce.Job:  map 50% reduce 13%
    2022-08-06 11:56:45,444 INFO mapreduce.Job:  map 51% reduce 13%
    2022-08-06 11:56:46,446 INFO mapreduce.Job:  map 52% reduce 14%
    2022-08-06 11:56:48,450 INFO mapreduce.Job:  map 53% reduce 14%
    2022-08-06 11:56:52,460 INFO mapreduce.Job:  map 53% reduce 18%
    2022-08-06 11:57:08,635 INFO mapreduce.Job:  map 57% reduce 18%
    2022-08-06 11:57:11,855 INFO mapreduce.Job:  map 59% reduce 18%
    2022-08-06 11:57:14,993 INFO mapreduce.Job:  map 60% reduce 18%
    2022-08-06 11:57:31,503 INFO mapreduce.Job:  map 62% reduce 18%
    2022-08-06 11:57:38,526 INFO mapreduce.Job:  map 64% reduce 18%
    2022-08-06 11:57:43,537 INFO mapreduce.Job:  map 65% reduce 18%
    2022-08-06 11:57:44,539 INFO mapreduce.Job:  map 67% reduce 19%
    2022-08-06 11:57:48,546 INFO mapreduce.Job:  map 68% reduce 19%
    2022-08-06 11:57:50,551 INFO mapreduce.Job:  map 69% reduce 22%
    2022-08-06 11:57:57,597 INFO mapreduce.Job:  map 69% reduce 23%
    2022-08-06 11:58:42,618 INFO mapreduce.Job:  map 70% reduce 23%
    2022-08-06 11:59:36,392 INFO mapreduce.Job:  map 71% reduce 23%
    2022-08-06 12:00:59,953 INFO mapreduce.Job:  map 72% reduce 23%
    2022-08-06 12:02:34,995 INFO mapreduce.Job:  map 73% reduce 23%
    2022-08-06 12:02:40,841 INFO mapreduce.Job:  map 75% reduce 23%
    2022-08-06 12:02:49,565 INFO mapreduce.Job:  map 78% reduce 23%
    2022-08-06 12:03:05,573 INFO mapreduce.Job:  map 79% reduce 23%
    2022-08-06 12:03:24,876 INFO mapreduce.Job:  map 80% reduce 23%
    2022-08-06 12:03:30,169 INFO mapreduce.Job:  map 81% reduce 24%
    2022-08-06 12:03:32,187 INFO mapreduce.Job:  map 82% reduce 24%
    2022-08-06 12:03:33,190 INFO mapreduce.Job:  map 83% reduce 24%
    2022-08-06 12:03:39,190 INFO mapreduce.Job:  map 84% reduce 27%
    2022-08-06 12:03:43,199 INFO mapreduce.Job:  map 84% reduce 28%
    2022-08-06 12:04:12,432 INFO mapreduce.Job:  map 85% reduce 28%
    2022-08-06 12:04:29,738 INFO mapreduce.Job:  map 87% reduce 28%
    2022-08-06 12:04:43,709 INFO mapreduce.Job:  map 90% reduce 28%
    2022-08-06 12:05:04,926 INFO mapreduce.Job:  map 91% reduce 28%
    2022-08-06 12:05:10,565 INFO mapreduce.Job:  map 92% reduce 28%
    2022-08-06 12:05:20,436 INFO mapreduce.Job:  map 93% reduce 28%
    2022-08-06 12:05:40,123 INFO mapreduce.Job:  map 94% reduce 28%
    2022-08-06 12:06:36,863 INFO mapreduce.Job:  map 95% reduce 28%
    2022-08-06 12:07:13,144 INFO mapreduce.Job:  map 96% reduce 28%
    2022-08-06 12:07:16,150 INFO mapreduce.Job:  map 97% reduce 28%
    2022-08-06 12:07:17,151 INFO mapreduce.Job:  map 99% reduce 28%
    2022-08-06 12:07:18,153 INFO mapreduce.Job:  map 99% reduce 31%
    2022-08-06 12:07:19,155 INFO mapreduce.Job:  map 100% reduce 31%
    2022-08-06 12:07:24,162 INFO mapreduce.Job:  map 100% reduce 68%
    2022-08-06 12:07:30,171 INFO mapreduce.Job:  map 100% reduce 73%
    2022-08-06 12:07:36,180 INFO mapreduce.Job:  map 100% reduce 79%
    2022-08-06 12:07:41,187 INFO mapreduce.Job:  map 100% reduce 84%
    2022-08-06 12:07:47,196 INFO mapreduce.Job:  map 100% reduce 89%
    2022-08-06 12:07:53,205 INFO mapreduce.Job:  map 100% reduce 94%
    2022-08-06 12:07:59,213 INFO mapreduce.Job:  map 100% reduce 100%
    2022-08-06 12:08:00,321 INFO mapred.ClientServiceDelegate: Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 12:08:01,349 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:02,349 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:03,350 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:04,350 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:05,351 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:06,351 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:07,351 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:08,352 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:09,352 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:10,353 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:10,456 INFO mapred.ClientServiceDelegate: Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 12:08:11,456 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:12,457 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:13,457 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:14,458 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:15,458 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:16,459 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:17,459 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:18,460 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:19,460 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:20,461 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:20,563 INFO mapred.ClientServiceDelegate: Application state is completed. FinalApplicationStatus=SUCCEEDED. Redirecting to job history server
    2022-08-06 12:08:21,564 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 0 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:22,564 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 1 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:23,565 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 2 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:24,565 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 3 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:25,566 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 4 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:26,566 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 5 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:27,567 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 6 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:28,567 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 7 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:29,568 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 8 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:30,568 INFO ipc.Client: Retrying connect to server: 0.0.0.0/0.0.0.0:10020. Already tried 9 time(s); retry policy is RetryUpToMaximumCountWithFixedSleep(maxRetries=10, sleepTime=1000 MILLISECONDS)
    2022-08-06 12:08:30,669 ERROR streaming.StreamJob: Error Launching job : java.net.ConnectException: Your endpoint configuration is wrong; For more details see:  http://wiki.apache.org/hadoop/UnsetHostnameOrPort
    Streaming Command Failed!

OBS:

    Houve Falha de conexão no fim mas o job deu como SUCCEEDED no servidor de verificação de status da job, na porta 8088, vide anexo nesta pasta