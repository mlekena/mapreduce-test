#!/bin/sh
echo "Running NBA Shot Log Analysis"
DATA_FILE_PATH="test_data.csv"
PROJECT_NAME="nbashotlogKMCZ"
IN_HADOOP_INPUT_PATH="/${PROJECT_NAME}/input/"
OUT_HADOOP_OUTPUT_PATH="/${PROJECT_NAME}/output/"
MAPPER_ONE_PATH="./app_czones/kmcz_mapper.py"
MAPPER_TWO_PATH="./app_czones/kmcz_mapper_kmean.py"
REDUCER_ONE_PATH="./app_czones/kmcz_reducer.py"
REDUCER_TWO_PATH="./app_czones/kmcz_reducer_kmean.py"
UTILS_PATH="./app_czones/utils_belt.py"
SOURCE="./app_czones"

HDFS="/usr/local/hadoop/bin/hdfs"
../../start.sh

$HDFS dfs -rm -r $IN_HADOOP_INPUT_PATH
$HDFS dfs -rm -r $OUT_HADOOP_OUTPUT_PATH
$HDFS dfs -mkdir -p $IN_HADOOP_INPUT_PATH
$HDFS dfs -copyFromLocal $DATA_FILE_PATH $IN_HADOOP_INPUT_PATH
$HDFS dfs -ls $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
-files $SOURCE \
-mapper $MAPPER_ONE_PATH -reducer $REDUCER_ONE_PATH \
-input $IN_HADOOP_INPUT_PATH* -output $OUT_HADOOP_OUTPUT_PATH

$HDFS dfs -rm -r $IN_HADOOP_INPUT_PATH
TEMP_INPUT=$OUT_HADOOP_OUTPUT_PATH

N=2
for counter in {1..$N}
do
    if [ ! $HDFS dfs -test -f $TEMP_INPUT/_SUCCESS ]; then 
      break
    fi
    $HDFS dfs -rm $TEMP_INPUT/_SUCCESS
    /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.9.2.jar \
    -files $SOURCE \
    -mapper $MAPPER_TWO_PATH -reducer $REDUCER_TWO_PATH \
    -input $TEMP_INPUT* -output ${OUT_HADOOP_OUTPUT_PATH}$i/
    # $HDFS dfs -rm -r $TEMP_INPUT
    TEMP_INPUT=${OUT_HADOOP_OUTPUT_PATH}$i/
done

if [ ! $HDFS dfs -test -f ${TEMP_INPUT}_SUCCESS]; then
    echo "DROPPING OUTPUT TO LOCAL DISK"
    $HDFS dfs -cat ${TEMP_INPUT}part-00000
fi 

for count in {1..$N}
do
    $HDFS dfs -cat ${TEMP_INPUT}$COUNT
done
$HDFS dfs -rm -r $TEMP_INPUT

/usr/local/hadoop/bin/hdfs dfs -ls $OUT_HADOOP_OUTPUT_PATH
echo "############################################################" 
/usr/local/hadoop/bin/hdfs dfs -cat ${OUT_HADOOP_OUTPUT_PATH}part-00000
# echo "This player the above fear score of "shots_made_near"/"total_shots_made_near"
echo "############################################################" 
echo "PRINTING THE FILES"
/usr/local/hadoop/bin/hdfs dfs -rm -r $IN_HADOOP_INPUT_PATH
/usr/local/hadoop/bin/hdfs dfs -rm -r ${OUT_HADOOP_OUTPUT_PATH}
../../stop.sh
