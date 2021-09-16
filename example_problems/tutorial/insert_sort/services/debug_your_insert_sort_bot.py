from sys import exit
import re
import random

from example_problems.tutorial.insert_sort.services.insert_sort_lib import InsertSort
from multilanguage import Env, Lang, TALcolors
from TALinputs import TALinput
from sys import stdout, stderr, exit, argv


# METADATA OF THIS TAL_SERVICE:
problem = "insert_sort"
service = "debug_your_insert_sort_bot"
args_list = [
    ('feedback', str),
    ('lang', str),
]


# START CODING YOUR SERVICE:
#Prendo array dello studente e bot dello studente
input_array = list(map(int, argv[2:]))
insert_sort = InsertSort(input_array)

with open(argv[1], 'r') as f:
    # Raggruppare righe con LOG_, dare in pasto l'array dell'utente a insertSort e vedere se i log si assomigliano





"""
    log_array = [""]
    
    
    def input_array_format(n: int, array: str):
        arraylista = array.lstrip(" ").split(" ")
        if len(arraylista) != n:
            return print("#Error: " + str(n) + " is not the right length, should be " + str(len(arraylista)))
    
        return print("Your array: " + str(arraylista))
    
    
    def insert_sort(array_inp: list):
        log_array.append("LOG_input_array " + str(array_inp))
        for i in range(1, len(array_inp)):
            j = i - 1
            log_array.append("LOG_memory_load_from_pos " + str(j))
            key = array_inp[i]
            while j >= 0 and array_inp[j] > key:
                cond = [True if j >= 0 and array_inp[j] > key else False]
                log_array.append("LOG_compare_what_in_pos" + str(j) + " less_than_what_in_memory " + str(cond))
                array_inp[j + 1] = array_inp[j]
                log_array.append("LOG_copy_from_pos " + str(j) + " to_pos " + str(j+1))
                j -= 1
            array_inp[j + 1] = key
            log_array.append("LOG_memory_write_on_pos " + str(j+1))
    
        log_array.append("LOG_output_array " + str(array_inp))
        return array_inp
    
    
    print(f"#Waiting for your n-dimensional array.\n#Format: [n,array]. Each value of the array must be separated by "
          f"spaces. "
          " Only integer numbers.")
    
    array = input()
    pattern = re.compile(r"^[0-9]+,[\s]*[0-9]+(\s+[0-9]+)*$")
    if not pattern.match(str(array)):
        print("#INVALID INPUT FORMAT.\n#Format: [n, array]. Each value of the array must be separated by spaces. Only "
              "integer numbers.")
        exit()
    
    arraylist = array.split(",")
    input_array_format(int(arraylist[0]), arraylist[1])
    print("Now, you can use ONLY those primitives: "
          "LOG_input_array <n> <input_array_of_length_n>"
          "LOG_memory_load_from_pos <i>"
          "LOG_memory_write_on_pos <i>"
          "LOG_copy_from_pos <i> to_pos <j>"
          "LOG_compare_what_in_pos <i> less_than_what_in_memory <outcome>"
          "LOG_output_array <n> <output_array_of_length_n>"
"""
