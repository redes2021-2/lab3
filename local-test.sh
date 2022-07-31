#! /bin/bash
cat word_count_data.txt | python3 mapper.py | sort | python3 reducer.py
