#!/usr/bin/env python3
from sys import stderr, exit
from time import monotonic

from TALinputs import TALinput
from multilanguage import Env, Lang, TALcolors

from piastrelle_lib import Par

# METADATA OF THIS TAL_SERVICE:
problem="piastrelle"
service="eval_num_sol_server"
args_list = [
    ('answ_modulus',int),
    ('goal',str),
    ('code_lang',str),
    ('lang',str),
]

ENV =Env(problem, service, args_list)
TAc =TALcolors(ENV)
LANG=Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"))

# START CODING YOUR SERVICE:
MAX_N_PAIRS = 14
if ENV["code_lang"]=="compiled":
    MAX_N_PAIRS += 1
instances = list(range(MAX_N_PAIRS + 1))
if ENV["goal"] == "efficient":
    MAX_N_PAIRS = 1000
    if ENV["answ_modulus"] == 0:
        MAX_N_PAIRS = 100
    if ENV["code_lang"]=="compiled":
        MAX_N_PAIRS *= 2
    scaling_factor = 1.2
    n = instances[-1]
    while True:
        n = 1 + int(n * scaling_factor)
        if n > MAX_N_PAIRS:
            break
        instances.append(n)

p = Par(MAX_N_PAIRS, nums_modulus=ENV["answ_modulus"])

def one_test(n):
    assert n <= MAX_N_PAIRS
    risp_correct = p.num_sol(n)
    TAc.print(n, "yellow", ["bold"])
    start = monotonic()
    risp = TALinput(int, 1, TAc=TAc)[0]
    end = monotonic()
    t = end - start # è un float, in secondi
    if ENV["answ_modulus"] == 0:
        if risp != risp_correct:
            TAc.print(LANG.render_feedback("not-equal", f'# No. Your solution is NOT correct. The number of well-formed tilings of a corridor of dimension 1x {n} is:\n {risp_correct}. Not {risp}.'), "red", ["bold"])                        
            exit(0)
    elif (risp % ENV["answ_modulus"]) != (risp_correct % ENV["answ_modulus"]):
        TAc.print(LANG.render_feedback("not-equiv", f'No. You solution is not correct. The number of well-formed tilings of a corridor of dimension 1x{n} is {risp_correct}. Taken modulus {ENV["answ_modulus"]} this value boils down to {risp_correct % ENV["answ_modulus"]}. Not {risp}.'), "red", ["bold"])                
        exit(0)
    return t   
        
for n in instances:
   time = one_test(n)
   print(f"#Correct! [took {time} secs on your machine]")
   if time > 1:
       if n > 13:
           TAc.print(LANG.render_feedback("seems-correct-weak", f'# Ok. :)  Your solution correctly computes the number of well formed tilings of a corridor of dimension 1x{n}.'), "green")
       TAc.print(LANG.render_feedback("not-efficient", f'# No. Your solution is not efficient. Run on your machine, it took more than one second to compute the number of well-formed tilings of a corridor of dimension 1x{n} .'), "red", ["bold"])        
       exit(0)
       
TAc.print(LANG.render_feedback("seems-correct-strong", f'# Ok. :)  Your solution appears to be correct (checked on several instances).'), "green")
TAc.print(LANG.render_feedback("efficient", f'# Ok. :)  Your solution is efficient: its running time is logarithmic in the number of tilings it counts.'), "green")

exit(0)
