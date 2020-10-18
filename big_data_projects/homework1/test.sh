#!/bin/sh
# Author: mlekena
# This script starts mapreduce and calls the appropriate mapper and reducer scripts.
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /homework1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /homework1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /homework1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/access.log /homework1/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../big_data_projects/homework1/mapper.py -mapper "../../big_data_projects/homework1/mapper.py $1" \
-file ../../big_data_projects/homework1/reducer.py -reducer ../../big_data_projects/homework1/reducer.py \
-input /homework1/input/* -output /homework1/output/

/usr/local/hadoop/bin/hdfs dfs -ls /homework1/output/
echo "###################### RESULTS #############################" 
/usr/local/hadoop/bin/hdfs dfs -cat /homework1/output/part-00000
echo "############################################################" 
/usr/local/hadoop/bin/hdfs dfs -rm -r /homework1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /homework1/output/
../../stop.sh
