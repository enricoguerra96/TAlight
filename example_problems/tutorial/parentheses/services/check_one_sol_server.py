#!/usr/bin/env python3
from sys import stderr, exit

from TALinputs import TALinput
from multilanguage import Env, Lang, TALcolors

from parentheses_lib import recognize

# METADATA OF THIS TAL_SERVICE:
problem="parentheses"
service="check_one_sol_server"
args_list = [
    ('input_formula',str),
    ('n',str),
    ('silent',bool),
    ('lang',str),
]

ENV =Env(problem, service, args_list)
TAc =TALcolors(ENV)
LANG=Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"))
    
# START CODING YOUR SERVICE:

if not recognize(ENV["input_formula"], TAc, LANG):
    exit(0)
len_input = len(ENV["input_formula"])
assert len_input % 2 == 0
if ENV['n'] != 'free' and 2*int(ENV['n']) != len_input:
    TAc.print(LANG.render_feedback("different_lengths", f"No! Your string represents a well-formed formula but has length {len_input}. Therefore the number of pairs of parentheses can not be {ENV['n']} since 2*{ENV['n']} != {len_input}."), "red", ["bold"])
    exit(0)

if not ENV["silent"]:
    TAc.OK()
    TAc.print(LANG.render_feedback("ok", f' Your string is a well-formed formula with {len_input} pairs of parentheses.'), "yellow", ["bold"])

exit(0)
