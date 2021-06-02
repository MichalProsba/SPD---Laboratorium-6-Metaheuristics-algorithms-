from Generator import RandomNumberGenerator
from Natural_permutation import Natural_permutation
from Natural_permutation_no_idle import Natural_permutation_no_idle

from Johnson_algorithm import Johnson_algorithm
from Johnson_algorithm3 import Johnson_algorithm3

from NEH_Algorithm import NEH_Algorithm
from NEH_Algorithm_no_idle import NEH_Algorithm_no_idle 

from Simulated_annealing_algorithm import Simulated_annealing_algorithm
from Simulated_annealing_algorithm_no_idle import Simulated_annealing_algorithm_no_idle

from Tabu_search_algorithm import Tabu_search_algorithm
from Tabu_search_algorithm_no_idle import Tabu_search_algorithm_no_idle
from ABC import ABC
import random

#seed = 11123
#tasks = 6
#machines = 5

seed = 123456
tasks = 20
machines = 5

#print (str1 + "JOHNSON ALGORITHM")
#johnson3 = Johnson_algorithm3(seed, tasks, machines)
#print(johnson3)

#print (str1 + "NEH PLUS 4 ALGORITHM")
#neh = NEH_Algorithm(seed, tasks, machines)
#neh.DoNEHPlus4()
#print(neh)

#print (str1 + "NEH PLUS 1 ALGORITHM")
#neh = NEH_Algorithm(seed, tasks, machines)
#neh.DoNEHPlus1()
#print(neh)

#str1 = "===================================================================\n"
#print (str1 + "NATURAL PERMUTATION")
#natural_permutation = Natural_permutation(seed, tasks, machines)
##print(natural_permutation)
#print(natural_permutation.UB)

#print (str1 + "NEH ALGORITHM")
#neh = NEH_Algorithm(seed, tasks, machines)
#neh.DoNEH()
##print(neh)
#print(neh.UB)

#print (str1 + "SIMULATED ANNEALING")
#sa = Simulated_annealing_algorithm(seed, tasks, machines)
#sa.SimulatedAnnealing()
##print(sa)
#print(sa.UB)

#print (str1 + "TABU SEARCH")
#tb = Tabu_search_algorithm(seed, tasks, machines)
#tb.TabuSearch()
##print(tb)
#print(tb.UB)

#print (str1 + "PORÓWNANIA")
#print("SIMULATED ANNEALING: " + str (round(((sa.UB-neh.UB)* 100.0/neh.UB),2)) + "%")
#print("TABU SEARCH: " + str (round(((tb.UB-neh.UB)* 100.0/neh.UB),2 )) + "%")

str1 = "===================================================================\n"
print (str1 + "NATURAL PERMUTATION NO IDLE")
natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
#print(natural_permutation)
print(natural_permutation_no_idle.UB)

print (str1 + "NEH ALGORITHM NO IDLE")
neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
neh_no_idle.DoNEH()
#print(neh)
print(neh_no_idle.UB)

str1 = "===================================================================\n"
print (str1 + "SIMULATED ANNEALING NO IDLE")
sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
sa_no_idle.SimulatedAnnealing()
#print(sa)
print(sa_no_idle.UB)

print (str1 + "TABU SEARCH NO IDLE")
tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
tb_no_idle.TabuSearch()
#print(tb)
print(tb_no_idle.UB)

print (str1 + "PORÓWNANIA")
print("SIMULATED ANNEALING: " + str (round(((neh_no_idle.UB-sa_no_idle.UB)* 100.0/neh_no_idle.UB),2)) + "%")
print("TABU SEARCH: " + str (round(((neh_no_idle.UB-tb_no_idle.UB)* 100.0/neh_no_idle.UB),2 )) + "%")



#print (str1 + "TABU SEARCH")
#tbnw = Tabu_search_no_wait_algorithm(seed, tasks, machines)
#tbnw.TabuSearch()
#print(tbnw)
#print(tbnw.UB)

#print (str1 + "ABC")
#abc = ABC(seed, tasks, machines)
#abc.DoABC()
#print(abc)

#str1 = "===================================================================\n"
#print (str1 + "NATURAL PERMUTATION NO IDLE")
#natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
#print(natural_permutation_no_idle)