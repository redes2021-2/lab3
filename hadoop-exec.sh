#! /bin/bash
hadoop jar /home/hadoop/Pspd/lab3-teste/hadoop-streaming-2.7.3.jar \
-input /word_count_in_python/word_count_data.txt \
-output /word_count_in_python/output \
-mapper /home/hadoop/Pspd/lab3-teste/mapper.py \
-reducer /home/hadoop/Pspd/lab3-teste/reducer.py
