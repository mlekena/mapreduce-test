#!/bin/sh
echo "Running Parking Violations Log Analysis"
DATA_FILE_PATH="TestData.csv"
PROJECT_NAME="NycDataAnalysis"
IN_HADOOP_INPUT_PATH="../${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="../${PROJECT_NAME}/output/"
MAPPER_PATH="./mapper"
REDUCER_PATH="./reducer"
P1="When.py"
P2="YearType.py"
P3="Location.py"
P4="Color.py"
SH_PATH="../../"

${SH_PATH}start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUT_HADOOP_OUTPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -mkdir -p $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal $DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -ls $IN_HADOOP_INPUT_PATH

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file $MAPPER_PATH$P1 -mapper $MAPPER_PATH$P1 \
-file $REDUCER_PATH$P1 -reducer $REDUCER_PATH$P1 \
-input $IN_HADOOP_INPUT_PATH* -output ${OUT_HADOOP_OUTPUT_PATH}when

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file $MAPPER_PATH$P2 -mapper $MAPPER_PATH$P2 \
-file $REDUCER_PATH$P2 -reducer $REDUCER_PATH$P2 \
-input $IN_HADOOP_INPUT_PATH* -output ${OUT_HADOOP_OUTPUT_PATH}yt

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file $MAPPER_PATH$P3 -mapper $MAPPER_PATH$P3 \
-file $REDUCER_PATH$P3 -reducer $REDUCER_PATH$P3 \
-input $IN_HADOOP_INPUT_PATH* -output ${OUT_HADOOP_OUTPUT_PATH}loc

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-file $MAPPER_PATH$P4 -mapper $MAPPER_PATH$P4 \
-file $REDUCER_PATH$P4 -reducer $REDUCER_PATH$P4 \
-input $IN_HADOOP_INPUT_PATH* -output ${OUT_HADOOP_OUTPUT_PATH}color

/usr/local/hadoop/bin/hdfs dfs -ls $OUT_HADOOP_OUTPUT_PATH
echo "####################################################################"
echo "####################################################################"
echo
echo "### OUTPUT FOR PART 1       Modupe Lekena, Dylan Smith, Suzanne Zhen"
echo
echo "####################################################################"
echo "####################################################################"
echo
echo "### PART 1.1 Hours"
echo
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}when/part-00000
echo "############################################################"
echo 
echo "############################################################"
echo
echo "### PART 1.2 Car Years and Types"
echo
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}yt/part-00000
echo "############################################################"
echo 
echo "############################################################"
echo
echo "### PART 1.3 Locations"
echo
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}loc/part-00000
echo "############################################################"
echo 
echo "############################################################"
echo
echo "### PART 1.4 Colors"
echo
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}color/part-00000
echo "############################################################"
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
${SH_PATH}stop.sh
