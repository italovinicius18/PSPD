COMMAND:

    hadoop jar  $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -input /user/italo/projeto/input/words.txt -output /user/italo/projeto/d/output/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file MapReduce/d/mapper.py -file MapReduce/d/reducer.py

LOG:

    2022-08-06 12:13:41,298 WARN streaming.StreamJob: -file option is deprecated, please use generic option -files instead.
    2022-08-06 12:13:43,653 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 12:13:44,383 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /0.0.0.0:8032
    2022-08-06 12:13:44,984 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/italo/.staging/job_1659792899936_0004
    2022-08-06 12:13:45,668 INFO mapred.FileInputFormat: Total input files to process : 1
    2022-08-06 12:13:45,745 INFO mapreduce.JobSubmitter: number of splits:32
    2022-08-06 12:13:45,872 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1659792899936_0004
    2022-08-06 12:13:45,872 INFO mapreduce.JobSubmitter: Executing with tokens: []
    2022-08-06 12:13:46,380 INFO conf.Configuration: resource-types.xml not found
    2022-08-06 12:13:46,381 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
    2022-08-06 12:13:46,549 INFO impl.YarnClientImpl: Submitted application application_1659792899936_0004
    2022-08-06 12:13:46,701 INFO mapreduce.Job: The url to track the job: http://DESKTOP-QCCMFLA.localdomain:8088/proxy/application_1659792899936_0004/
    2022-08-06 12:13:46,703 INFO mapreduce.Job: Running job: job_1659792899936_0004
    2022-08-06 12:13:58,880 INFO mapreduce.Job: Job job_1659792899936_0004 running in uber mode : false
    2022-08-06 12:13:58,881 INFO mapreduce.Job:  map 0% reduce 0%
    2022-08-06 12:14:22,124 INFO mapreduce.Job:  map 3% reduce 0%
    2022-08-06 12:14:24,130 INFO mapreduce.Job:  map 5% reduce 0%
    2022-08-06 12:14:27,147 INFO mapreduce.Job:  map 6% reduce 0%
    2022-08-06 12:14:36,664 INFO mapreduce.Job:  map 7% reduce 0%
    2022-08-06 12:14:45,843 INFO mapreduce.Job:  map 9% reduce 0%
    2022-08-06 12:14:52,215 INFO mapreduce.Job:  map 10% reduce 0%
    2022-08-06 12:14:58,177 INFO mapreduce.Job:  map 11% reduce 0%
    2022-08-06 12:15:00,182 INFO mapreduce.Job:  map 12% reduce 0%
    2022-08-06 12:15:02,193 INFO mapreduce.Job:  map 13% reduce 0%
    2022-08-06 12:15:03,227 INFO mapreduce.Job:  map 14% reduce 0%
    2022-08-06 12:15:04,231 INFO mapreduce.Job:  map 15% reduce 0%
    2022-08-06 12:15:06,240 INFO mapreduce.Job:  map 17% reduce 0%
    2022-08-06 12:15:07,242 INFO mapreduce.Job:  map 18% reduce 0%
    2022-08-06 12:15:08,246 INFO mapreduce.Job:  map 19% reduce 0%
    2022-08-06 12:15:22,291 INFO mapreduce.Job:  map 23% reduce 0%
    2022-08-06 12:15:23,295 INFO mapreduce.Job:  map 25% reduce 0%
    2022-08-06 12:15:24,298 INFO mapreduce.Job:  map 28% reduce 0%
    2022-08-06 12:15:25,301 INFO mapreduce.Job:  map 32% reduce 0%
    2022-08-06 12:15:26,304 INFO mapreduce.Job:  map 35% reduce 0%
    2022-08-06 12:15:27,307 INFO mapreduce.Job:  map 36% reduce 0%
    2022-08-06 12:15:28,310 INFO mapreduce.Job:  map 38% reduce 0%
    2022-08-06 12:15:43,359 INFO mapreduce.Job:  map 42% reduce 13%
    2022-08-06 12:15:45,364 INFO mapreduce.Job:  map 44% reduce 13%
    2022-08-06 12:15:48,510 INFO mapreduce.Job:  map 45% reduce 13%
    2022-08-06 12:16:07,888 INFO mapreduce.Job:  map 46% reduce 13%
    2022-08-06 12:16:47,612 INFO mapreduce.Job:  map 48% reduce 13%
    2022-08-06 12:16:56,631 INFO mapreduce.Job:  map 49% reduce 13%
    2022-08-06 12:17:08,932 INFO mapreduce.Job:  map 50% reduce 13%
    2022-08-06 12:17:13,957 INFO mapreduce.Job:  map 51% reduce 13%
    2022-08-06 12:17:15,963 INFO mapreduce.Job:  map 52% reduce 13%
    2022-08-06 12:17:16,966 INFO mapreduce.Job:  map 53% reduce 13%
    2022-08-06 12:17:17,968 INFO mapreduce.Job:  map 53% reduce 18%
    2022-08-06 12:17:36,011 INFO mapreduce.Job:  map 57% reduce 18%
    2022-08-06 12:17:37,013 INFO mapreduce.Job:  map 61% reduce 18%
    2022-08-06 12:17:42,244 INFO mapreduce.Job:  map 63% reduce 18%
    2022-08-06 12:17:44,251 INFO mapreduce.Job:  map 67% reduce 18%
    2022-08-06 12:17:46,256 INFO mapreduce.Job:  map 69% reduce 18%
    2022-08-06 12:17:48,261 INFO mapreduce.Job:  map 69% reduce 23%
    2022-08-06 12:18:37,164 INFO mapreduce.Job:  map 70% reduce 23%
    2022-08-06 12:18:39,168 INFO mapreduce.Job:  map 72% reduce 23%
    2022-08-06 12:18:46,180 INFO mapreduce.Job:  map 73% reduce 23%
    2022-08-06 12:18:51,189 INFO mapreduce.Job:  map 75% reduce 23%
    2022-08-06 12:18:52,191 INFO mapreduce.Job:  map 78% reduce 23%
    2022-08-06 12:18:53,193 INFO mapreduce.Job:  map 79% reduce 23%
    2022-08-06 12:18:55,196 INFO mapreduce.Job:  map 83% reduce 24%
    2022-08-06 12:18:56,198 INFO mapreduce.Job:  map 84% reduce 24%
    2022-08-06 12:19:01,208 INFO mapreduce.Job:  map 84% reduce 28%
    2022-08-06 12:19:14,232 INFO mapreduce.Job:  map 93% reduce 28%
    2022-08-06 12:19:15,233 INFO mapreduce.Job:  map 95% reduce 28%
    2022-08-06 12:19:17,238 INFO mapreduce.Job:  map 98% reduce 28%
    2022-08-06 12:19:18,240 INFO mapreduce.Job:  map 100% reduce 28%
    2022-08-06 12:19:19,242 INFO mapreduce.Job:  map 100% reduce 33%
    2022-08-06 12:19:25,253 INFO mapreduce.Job:  map 100% reduce 68%
    2022-08-06 12:19:31,262 INFO mapreduce.Job:  map 100% reduce 72%
    2022-08-06 12:19:37,272 INFO mapreduce.Job:  map 100% reduce 76%
    2022-08-06 12:19:43,282 INFO mapreduce.Job:  map 100% reduce 80%
    2022-08-06 12:19:49,291 INFO mapreduce.Job:  map 100% reduce 84%
    2022-08-06 12:19:55,301 INFO mapreduce.Job:  map 100% reduce 87%
    2022-08-06 12:20:01,310 INFO mapreduce.Job:  map 100% reduce 91%
    2022-08-06 12:20:07,319 INFO mapreduce.Job:  map 100% reduce 95%
    2022-08-06 12:20:13,329 INFO mapreduce.Job:  map 100% reduce 99%
    2022-08-06 12:20:15,333 INFO mapreduce.Job:  map 100% reduce 100%
    2022-08-06 12:20:16,338 INFO mapreduce.Job: Job job_1659792899936_0004 completed successfully
    2022-08-06 12:20:16,608 INFO mapreduce.Job: Counters: 55
            File System Counters
                    FILE: Number of bytes read=3771327174
                    FILE: Number of bytes written=5666208831
                    FILE: Number of read operations=0
                    FILE: Number of large read operations=0
                    FILE: Number of write operations=0
                    HDFS: Number of bytes read=4294088194
                    HDFS: Number of bytes written=43804
                    HDFS: Number of read operations=101
                    HDFS: Number of large read operations=0
                    HDFS: Number of write operations=2
                    HDFS: Number of bytes read erasure-coded=0
            Job Counters
                    Killed map tasks=1
                    Launched map tasks=32
                    Launched reduce tasks=1
                    Data-local map tasks=32
                    Total time spent by all maps in occupied slots (ms)=1629346
                    Total time spent by all reduces in occupied slots (ms)=289645
                    Total time spent by all map tasks (ms)=1629346
                    Total time spent by all reduce tasks (ms)=289645
                    Total vcore-milliseconds taken by all map tasks=1629346
                    Total vcore-milliseconds taken by all reduce tasks=289645
                    Total megabyte-milliseconds taken by all map tasks=1668450304
                    Total megabyte-milliseconds taken by all reduce tasks=296596480
            Map-Reduce Framework
                    Map input records=500000000
                    Map output records=152247557
                    Map output bytes=1581168263
                    Map output materialized bytes=1885663569
                    Input split bytes=3456
                    Combine input records=0
                    Combine output records=0
                    Reduce input groups=3045
                    Reduce shuffle bytes=1885663569
                    Reduce input records=152247557
                    Reduce output records=3045
                    Spilled Records=456742671
                    Shuffled Maps =32
                    Failed Shuffles=0
                    Merged Map outputs=32
                    GC time elapsed (ms)=110854
                    CPU time spent (ms)=2374010
                    Physical memory (bytes) snapshot=15233908736
                    Virtual memory (bytes) snapshot=85529432064
                    Total committed heap usage (bytes)=13256097792
                    Peak Map Physical memory (bytes)=501616640
                    Peak Map Virtual memory (bytes)=2610110464
                    Peak Reduce Physical memory (bytes)=753487872
                    Peak Reduce Virtual memory (bytes)=2610135040
            Shuffle Errors
                    BAD_ID=0
                    CONNECTION=0
                    IO_ERROR=0
                    WRONG_LENGTH=0
                    WRONG_MAP=0
                    WRONG_REDUCE=0
            File Input Format Counters
                    Bytes Read=4294084738
            File Output Format Counters
                    Bytes Written=43804
    2022-08-06 12:20:16,608 INFO streaming.StreamJob: Output directory: /user/italo/projeto/d/output/