#!/bin/sh
echo "Running NBA Shot Log Analysis"
DATA_FILE_PATH="_test_data.csv"
PROJECT_NAME="nba_shot_log"
IN_HADOOP_INPUT_PATH="/${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="/${PROJECT_NAME}/output/"

../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUT_HADOOP_OUTPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -mkdir -p $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file ../../mapreduce-test-python/mlekena_logstat/mapper.py -mapper ../../mapreduce-test-python/mlekena_logstat/mapper.py \
-file ../../mapreduce-test-python/mlekena_logstat/reducer.py -reducer ../../mapreduce-test-python/mlekena_logstat/reducer.py \
-input $IN_HADOOP_INPUT_PATH* -output $OUT_HADOOP_OUTPUT_PATH

/usr/local/hadoop/bin/hdfs dfs -ls $OUT_HADOOP_OUTPUT_PATH
echo "############################################################" 
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}part-00000
echo "############################################################" 
echo "I AM ABOUT TO DRY RUN REMOVING FILES FROM THE OUTPUT SCRIPT"
echo "LETS PRINT THE FILES INSTEAD"
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_OUTPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
../../stop.sh
