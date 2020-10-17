#!/bin/sh
echo "REMEMBER, SUBMIT AFTER CORRECTING PATHS TO EXPECT OR SUBMIT ALL OF mlekena-logstat."
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /logstat2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/mlekena_logstat/mapper.py -mapper ../../mapreduce-test-python/mlekena_logstat/mapper.py \
-file ../../mapreduce-test-python/mlekena_logstat/reducer.py -reducer ../../mapreduce-test-python/mlekena_logstat/reducer.py \
-input /logstat2/input/* -output /logstat2/output/

/usr/local/hadoop/bin/hdfs dfs -ls /logstat2/output/
echo "############################################################" 
/usr/local/hadoop/bin/hdfs dfs -cat /logstat2/output/part-00000
echo "############################################################" 
echo "I AM ABOUT TO DRY RUN REMOVING FILES FROM THE OUTPUT SCRIPT"
echo "LETS PRINT THE FILES INSTEAD"
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /logstat2/output/
../../stop.sh
