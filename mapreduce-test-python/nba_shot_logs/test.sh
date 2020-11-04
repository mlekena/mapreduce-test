#!/bin/sh
echo "Running NBA Shot Log Analysis"
DATA_FILE_PATH="test_data.csv"
PROJECT_NAME="nbashotlog"
IN_HADOOP_INPUT_PATH="/${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="/${PROJECT_NAME}/output/"
MAPPER_ONE_PATH="./mapper.py"
REDUCER_ONE_PATH="./reducer.py"

../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUT_HADOOP_OUTPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -mkdir -p $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal $DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -ls $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file $MAPPER_ONE_PATH -mapper $MAPPER_ONE_PATH \
-file $REDUCER_ONE_PATH -reducer $REDUCER_ONE_PATH \
-input $IN_HADOOP_INPUT_PATH* -output $OUT_HADOOP_OUTPUT_PATH

/usr/local/hadoop/bin/hdfs dfs -ls $OUT_HADOOP_OUTPUT_PATH
echo "############################################################" 
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}part-00000
echo "This player the above fear score of "shots_made_near"/"total_shots_made_near"
echo "############################################################" 
echo "PRINTING THE FILES"
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
../../stop.sh
