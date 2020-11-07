#!/bin/sh
echo "Running NBA Shot Log Analysis"
DATA_FILE_PATH="test_data.csv"
PROJECT_NAME="nbashotlogKMCZ"
IN_HADOOP_INPUT_PATH="/${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="/${PROJECT_NAME}/output/"
MAPPER_ONE_PATH="./kmcz_mapper.py"
MAPPER_TWO_PATH="./kmcz_mapper_kmean.py"
REDUCER_ONE_PATH="./kmcz_reducer.py"
REDUCER_TWO_PATH="./kmcz_reducer_kmean.py"
UTILS_PATH="./utils_belt.py"
SOURCE="${MAPPER_ONE_PATH},${MAPPER_TWO_PATH},${REDUCER_ONE_PATH},${REDUCER_TWO_PATH},${UTILS_PATH}"

../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r $OUT_HADOOP_OUTPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -mkdir -p $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal $DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -ls $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-files $SOURCE \
-mapper $MAPPER_ONE_PATH -reducer $REDUCER_ONE_PATH \
-input $IN_HADOOP_INPUT_PATH* -output $OUT_HADOOP_OUTPUT_PATH

for i in {1..3}
do 
echo i
done

/usr/local/hadoop/bin/hdfs dfs -ls $OUT_HADOOP_OUTPUT_PATH
echo "############################################################" 
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}part-00000
# echo "This player the above fear score of "shots_made_near"/"total_shots_made_near"
echo "############################################################" 
echo "PRINTING THE FILES"
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
../../stop.sh
