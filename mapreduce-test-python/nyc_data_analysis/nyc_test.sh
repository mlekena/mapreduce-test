#!/bin/sh
echo "Running Parking Violations Log Analysis -- When"
#DATA_FILE_PATH="Parking_Violations_Issued_-_Fiscal_Year_2021.csv"
DATA_FILE_PATH="test_data.csv"
PROJECT_NAME="Project1Tix"
IN_HADOOP_INPUT_PATH="/${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="/${PROJECT_NAME}/output/"
MAPPER_ONE_PATH="./mapperWhen.py"
REDUCER_ONE_PATH="./reducerWhen.py"
START_PATH="../../"
END_PATH=$START_PATH
${START_PATH}start.sh
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
echo "############################################################"
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
${END_PATH}stop.sh

# #!/bin/sh
# echo "Running Parking Violations Log Analysis -- When, from within Project Folder"
# DATA_FILE_PATH="_test_data.csv"
# PROJECT_NAME="nyc_data_analysis"
# IN_HADOOP_INPUT_PATH="../${PROJECT_NAME}/input/"
# OUT_HADOOP_OUTPUT_PATH="../${PROJECT_NAME}/output/"
# MAPPER_ONE_PATH="./mapperWhen.py"
# REDUCER_ONE_PATH="./reducerWhen.py"
# START_PATH="../../"
# END_PATH=$START_PATH
# ${START_PATH}start.sh
# /usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
# /usr/local/hadoop/bin/hdfs dfs -rm -r $OUT_HADOOP_OUTPUT_PATH
# /usr/local/hadoop/bin/hdfs dfs -mkdir -p $IN_HADOOP_INPUT_PATH
# /usr/local/hadoop/bin/hdfs dfs -copyFromLocal $DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
# /usr/local/hadoop/bin/hdfs dfs -ls $IN_HADOOP_INPUT_PATH
# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
# -file $MAPPER_ONE_PATH -mapper $MAPPER_ONE_PATH \
# -file $REDUCER_ONE_PATH -reducer $REDUCER_ONE_PATH \
# -input $IN_HADOOP_INPUT_PATH* -output $OUT_HADOOP_OUTPUT_PATH
# /usr/local/hadoop/bin/hdfs dfs -ls $OUT_HADOOP_OUTPUT_PATH
# echo "############################################################"
# /usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}part-00000
# echo "############################################################"
# /usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
# /usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
# ${END_PATH}stop.sh
