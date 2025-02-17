#!/usr/bin/env python3
from sys import exit
import random
from ast import literal_eval as make_tuple

from TALinputs import TALinput
from multilanguage import Env, Lang, TALcolors

import graph_coloring_utilities as Utilities


# METADATA OF THIS TAL_SERVICE:
problem="graph_coloring"
service="eval_recognize_proper_colorings"
args_list = [
    ('num_nodes',int),
    ('num_arcs',int),
    ('seed',str),
    ('coloring',str),
    ('commitment',str),
    ('goal',str),
    ('lang',str),    
]

ENV = Env(problem, service, args_list)
TAc = TALcolors(ENV)
LANG = Lang(ENV, TAc, lambda fstring: eval(f"f'{fstring}'"))
TAc.print(LANG.print_opening_msg(), "green")

# START CODING YOUR SERVICE:


if ENV["seed"] == 'random_seed':
    seed = random.randint(100000,999999)    
else:
    seed = int(ENV["seed"])
print(LANG.render_feedback("assigned-instance", f"# The assigned instance is:\n#   number of nodes: {ENV['num_nodes']}\n#   number of arcs: {ENV['num_arcs']}\n#   Seed: "), end="")
TAc.print(seed, "yellow")
print("#start")


num_matches = 10
matchWin = 0
numNodes = ENV["num_nodes"]
numArcs = ENV["num_arcs"]
random.seed(seed)
matchDone = 1
while matchDone <= num_matches:
    internalSeed = random.randint(100000,999999)
    print(LANG.render_feedback("new-match", f"# match {matchDone} of {num_matches}. Instance:\n#   number of nodes: {numNodes}\n#   number of arcs: {numArcs}\n#   seed: "), end="")
    TAc.print(internalSeed, "yellow")
    graph = Utilities.generateGraph(numNodes, numArcs, internalSeed)
    colors = [0 for i in range(len(graph))]
    rightColors = []
    colorsNum = 4
    while not rightColors:
        rightColors = Utilities.graphColoring(graph, colorsNum, 0, colors)
        colorsNum += 1

    print(LANG.render_feedback("graph", "graph: "))
    for i in range(len(graph)):
        print(f"{i}:  ", end="")
        print(*graph[i], sep = ", ")

    newColors = None
    wrongArcs = None
    print(LANG.render_feedback("coloring", "coloring: "), end="")
    if ENV['coloring'] == 'improper' or (ENV['coloring'] == 'surprise' and bool(random.randint(0, 1))):
        newColors, wrongArcs = Utilities.breakGraphColoring(graph, rightColors, internalSeed)
        print(*newColors, sep = ", ")
    else:  
        print(*rightColors, sep = ", ")
    if ENV['commitment'] == "yes_no":
        print(LANG.render_feedback("yes_no_eval", "# ? is the coloring proper? (yes/no): "))
        buffer = TALinput(
            str,
            num_tokens=1,
            regex=r"^(yes|no)$",
            regex_explained="yes or no",
            TAc=TAc
        )
        userInput = buffer[0]
        if (wrongArcs and userInput == 'no') or (not wrongArcs and userInput == 'yes'):
            TAc.OK()
            print('\n')
            matchWin += 1
        else:
            TAc.NO()
            print('\n')
    else:
        print(LANG.render_feedback("give_violated_arc_eval", '# ? if the coloring is proper then insert "yes". Otherwise, provide a violated arc (in the format (endpoint1,endpoint2)) as certificate for your "no":'))
        buffer = TALinput(
            str,
            num_tokens=1,
            regex=r"^(\s*yes\s*|\(([0-9][0-9]{0,2}|1000),([0-9][0-9]{0,2}|1000)\))$",
            regex_explained="the 'yes' string or a violated arc in the form of an ordered pair of its endpoints (two numbers in [0," + str(numNodes - 1) + "] separated by comma and enclosed in a pair of parentheses. For example: '(3,4)'.",
            TAc=TAc
        )
        if "".join(buffer[0].split()) == 'yes':
            if not wrongArcs:
                TAc.OK()
                print('\n')
                matchWin += 1
            else:
                TAc.print(LANG.render_feedback("wrong-proper", f"NO! There are violated arcs like {wrongArcs.pop()}"), "red", ["bold"])
        else:
            inputArcs = make_tuple(buffer[0])
            if not wrongArcs and inputArcs:
                TAc.print(LANG.render_feedback("wrong-not-proper", f"NO! The coloring is proper!"), "red", ["bold"])
            elif inputArcs not in wrongArcs and inputArcs[::-1] not in wrongArcs:
                    TAc.print(LANG.render_feedback("wrong-proper", f"NO! There are violated arcs like {wrongArcs.pop()}"), "red", ["bold"])
            else:
                TAc.OK()
                matchWin += 1
    matchDone += 1
    if ENV['goal'] == 'linear':
        numNodes = round(numNodes * 1.2)
        numArcs = round(numArcs * 1.2)

print('#end')
print(LANG.render_feedback("matches-statistics", f"# Statistics:\n#   Matches won: {matchWin}/{num_matches}"))
