Na execução de cada script mapreduce em Python, eu testei em dois arquivos distintos e de duas formas diferentes

No teste local:

    Utilizei o arquivo input/test.txt (40,9 MB) e executei o comando "cat input/test.txt | python mapper.py | sort -k1,1 | python reducer.py" no python local e coloquei a saída nos arquivos outPy.txt de cada pasta

No teste remoto (Hadoop):

    Utilizei o arquivo input/words.txt (3,99 GB), criei as respectivas pastas no hdfs e assim executei o comando "hadoop jar  $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -input /user/italo/projeto/input/words.txt -output /user/italo/projeto/a/output/ -mapper "python3 mapper.py" -reducer "python3 reducer.py" -file MapReduce/a/mapper.py -file MapReduce/a/reducer.py", ao ter acabado a job eu fiz um "hdfs dfs -cat /user/italo/projeto/a/output/part-00000 > MapReduce/a/outputHadoop.txt" para a respectiva pasta local verificando a saída

O motivo de eu ter feito deste jeito foi para efeitos de teste, verificando se o código escrito estava correto ou não na máquina local para que quando estivesse correto, pudesse ser executado pelo hadoop