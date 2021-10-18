#!/usr/bin/env python3
from sys import argv, exit, stderr
import os

INPUT_FOLDER = argv[1]
INPUT_FORMAT = argv[2]
if INPUT_FORMAT == "dat":
    GENERATOR="./instance-generators/dat-generator.sh"
if INPUT_FORMAT == "txt":
    GENERATOR="./instance-generators/txt-generator.sh"

os.system(f"rm -rf {INPUT_FOLDER}")
os.system(f"mkdir {INPUT_FOLDER}")

def my_system_run(command_string):
    print("makeInputs.py:"+command_string)
    if os.system(command_string) != 0:
        print("\nIl seguente comando lanciato da makeInputs.py ha avuto qualche problema.\nmakeInputs.py:"+command_string+"\nEsecuzione di makeInputs.py interrotta a questo punto.")
        exit(1)

# Goal 1 instances:

# A few inputs hard-coded in the generator (could have been in separated files and here we could simply copy them):
my_system_run(f"cat examples/input_1.{INPUT_FORMAT} > {INPUT_FOLDER}/input_1.{INPUT_FORMAT}")

#parameters for generator.cpp:
# <M> <N> <not-solvable> <seed>
# not-solvable = 0 generate a solvable instance, not-solvable = 1 no solution

# Goal 2 instances:
for i in range(2,5):
    my_system_run(f"{GENERATOR} {i} {7-i} 1 {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal2-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")


# Goal 3 instances:
for i in range(5,8):
    my_system_run(f"{GENERATOR} {10-i} {i-3} 0 {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal3-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 4 instances:
for i in range(8,10):
    my_system_run(f"{GENERATOR} 10 10 {i%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal4-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 5 instances:
for i in range(10,12):
    my_system_run(f"{GENERATOR} 20 20 {(i+1)%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal5-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 6 instances:
for i in range(12,14):
    my_system_run(f"{GENERATOR} 30 30 {i%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal6-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 7 instances:
for i in range(14,16):
    my_system_run(f"{GENERATOR} 50 50 {(i+1)%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal7-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 8 instances:
for i in range(16,18):
    my_system_run(f"{GENERATOR} 100 100 {(i+1)%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal8-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 9 instances:
for i in range(18,20):
    my_system_run(f"{GENERATOR} 200 200 {i%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal8-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

# Goal 10 instances:
for i in range(20,22):
    my_system_run(f"{GENERATOR} 300 300 {(i+1)%2} {777+i} > {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")
#    my_system_run(f"./instance-generators/check_is_goal10-instance.py < {INPUT_FOLDER}/input_{i}.{INPUT_FORMAT}")

