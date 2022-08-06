import time

init = time.time()

from operator import add
from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .appName("PythonWordCountWithLength6and8and11")\
        .getOrCreate()

def check_word(word):
    if len(word) == 6 or len(word) == 8 or len(word) == 11:
        return True
    else:
        return False

lines = spark.read.text('projeto/input/words.txt').rdd.map(lambda r: r[0])
counts = lines.flatMap(lambda x: x.split(' ')) \
            .filter(check_word) \
            .map(lambda x: (x,1)) \
            .reduceByKey(add)
output = counts.collect()

with open('outputSpark.txt', 'w+') as f:
    for (word, count) in output:
        f.write("%s: %i\n" % (word, count))

spark.stop()

end = time.time()

print("Tempo de execução: %.2f segundos" % (end - init))