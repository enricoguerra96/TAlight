#!/usr/bin/env python3
from sys import stderr, exit
import re
from time import monotonic

from TALinputs import TALinput
from multilanguage import Env, Lang, TALcolors

from increasing_subsequence_lib import *
# METADATA OF THIS TAL_SERVICE:
problem="increasing_subseq"
service="eval_num_occurrences_of_S_in_T"
args_list = [
    ('seed',str),
    ('goal',str),
    ('code_lang',str),
    ('answ_modulus',int),
    ('lang',str)
]
ENV =Env(problem, service, args_list)
TAc =TALcolors(ENV)
LANG=Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"))
cert = ENV['cert']
seed = ENV['seed']

# START CODING YOUR SERVICE:
max_val = 100
if ENV['seed']=='random_seed': 
    seed_service = random.randint(100000,999999)
else:
    seed_service = int(ENV['seed'])
random.seed(seed_service)
TAc.print(LANG.render_feedback("seed-service",f"# The service is running with seed={seed_service}"), "green")
TAc.print(LANG.render_feedback("explain-protocol","# Each instance gives you a sequence of numbers T and then, on the next row, a sequence of numbers S. You should say how may occurences of S in T."), "green")
MAX_M_correct = 20 # len_T
MAX_N_correct = 20 # len_S
NUM_instances_correct = 20
if ENV["code_lang"]=="compiled":
    MAX_M_correct += 2
    MAX_N_correct += 2    
instances = []
# creo i descrittori di istanza per le istanze che è necessario superare per ottenere conferma di correttezza:
for i in range(NUM_instances_correct):
    instances.append({
        "m": MAX_M_correct - i%5,      
        "n": MAX_N_correct - i%MAX_N_correct,
        "max_val": max_val,
        "yes": 1,
        "seed": seed_service + i })   
# creo ulteriori istanze per le valutazioni di efficienza:
MAX_M_quadratic = 10000 # len_T
MAX_N_quadratic =   100 # len_S
if ENV["goal"] == "quadratic":
    if ENV["code_lang"]=="compiled":
        MAX_M_quadratic *= 20
        MAX_N_quadratic *= 20
    # crescita graduale (rischio soluzione esponenziale):
    for i in range(MAX_M_correct+1, 2*MAX_M_correct):
        instances.append({
            "m": i,      
            "n": i//2,
            "max_val": max_val,
            "yes": 1,
            "seed": seed_service + i + NUM_instances_correct })
    
    # crescita geometrica (ora sappiamo che la soluzione è polinomiale):    
    scaling_factor = 1.5
    tmp = instances[-1]
    m = tmp["m"]
    n = tmp["n"]
    s = tmp["seed"]
    while True:
        m = 1 + int(m * scaling_factor)
        n = 1 + int(n * scaling_factor)
        seed_instance = seed_service + m + n
        if (m > MAX_M_quadratic) or (n > MAX_N_quadratic):
            break
        instances.append({
        "m": m,      
        "n": n,
        "max_val": max_val,
        "yes": 1,
        "seed": seed_service + m + n })

MAX_M_quasi_linear = 10000 # len_T
MAX_N_quasi_linear =   100 # len_S
if ENV["goal"] == "quasi_linear":
    if ENV["code_lang"]=="compiled":
        MAX_M_efficient *= 20
        MAX_N_efficient *= 20
    # crescita graduale (rischio soluzione esponenziale):
    for i in range(MAX_M_correct+1, 2*MAX_M_correct):
        instances.append({
            "m": i,      
            "n": i//2,
            "max_val": max_val,
            "yes": 1,
            "seed": seed_service + i + NUM_instances_correct })
    
    # crescita geometrica (ora sappiamo che la soluzione è polinomiale):    
    scaling_factor = 1.5
    tmp = instances[-1]
    m = tmp["m"]
    n = tmp["n"]
    s = tmp["seed"]
    while True:
        m = 1 + int(m * scaling_factor)
        n = 1 + int(n * scaling_factor)
        seed_instance = seed_service + m + n
        if (m > MAX_M_quasi_linear) or (n > MAX_N_quasi_linear):
            break
        instances.append({
        "m": m,      
        "n": n,
        "max_val": max_val,
        "yes": 1,
        "seed": seed_service + m + n })


def one_test(m,n,max_val,yes_instance,seed):
    TAc.print(LANG.render_feedback("seed-all-run",f"#Check on Instance (m={m},n={n},max_val={max_val},yes_instance={yes_instance},seed {seed}): "), "yellow", ["bold"])
    T,S,seed = gen_subseq_instance(m, n, max_val, yes_instance, seed)
    TAc.print(" ".join(map(str,T)), "yellow", ["bold"])
    TAc.print(" ".join(map(str,S)), "yellow", ["bold"])

    n_occurences = count_occurences(T,S)
    start = monotonic()
    #risp = input(str,num_tokens=1,regex="^(0|1|y|n|Y|N|yes|no|YES|NO|Yes|No)$")
    risp = input()

    end = monotonic()

    t = end - start

    if n_occurences != int(risp):
        TAc.print(f"#NO, it isn't the number of occurences of S in T. The correct number is {n_occurences}. To retry this test use seed: {seed_service}", "red")
        exit(0)
    return t   
    
count = 0
for instance in instances:
    time = one_test(instance["m"], instance["n"], instance["max_val"], instance["yes"], instance["seed"])
    count +=1
    print(f"#Correct! [took {time} seconds on your machine]")
    if time > 50:
        if count > NUM_instances_correct:
            TAc.print(LANG.render_feedback("seems-correct-weak", f'# Ok. ♥ Your solution answers correctly on a first set of instances (with |T|, the length of T, up to {instance["m"]}.'), "green")
        TAc.print(LANG.render_feedback("not-efficient", f'# No. You solution is NOT {ENV["goal"]}. When run on your machine, it took more than one second to answer on an instance where |T|={instance["m"]} and |S|={instance["n"]}.'), "red", ["bold"])        
        exit(0)

TAc.print(LANG.render_feedback("seems-correct-strong", f'# Ok. ♥  Your solution appears to be correct (checked on several instances).'), "green")
TAc.print(LANG.render_feedback("efficient", f'# Ok. ♥ Your solution is {ENV["goal"]}: its running time is linear in the length of T and S.'), "green")

exit(0)
