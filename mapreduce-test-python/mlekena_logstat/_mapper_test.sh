cat secondStageData.txt | ./second_phase_mapper.py
echo "RUNNING REDUCER TEST" 
cat secondPhaseReducerData.txt | ./second_phase_reducer.py 
