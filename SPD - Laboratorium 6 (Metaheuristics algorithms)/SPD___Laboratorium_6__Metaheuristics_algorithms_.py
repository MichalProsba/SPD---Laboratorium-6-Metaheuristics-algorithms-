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
import matplotlib.pyplot as plt
import numpy as np

seed = 9572817
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

###################################################################################################
#Wykres w zaleznosci od ilosci zadan
NA = [] 
NEH = []
SA = []
TA = []
N = []

seed = 145534
machines = 6
list_task = [3,4,5,6,7,8,9,11,12,13,14,15]

for tasks in list_task:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.SimulatedAnnealing()
    SA.append(sa_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.TabuSearch()
    TA.append(tb_no_idle.UB)

    N.append(tasks)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, SA, color="blue", label='Simulated_annealing', linewidth=1, alpha=0.5)
plt.plot(N, TA, color="black", label='Tabu search', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba zadań")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby zadań")
plt.grid(True)
plt.show()

####################################################################################################
##Wykres w zaleznosci od ilosci maszyn

NA = [] 
NEH = []
SA = []
TA = []
N = []

seed = 9572817
tasks = 7
list_machines = [3,4,5,6,7,8,9]
for machines in list_machines:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.SimulatedAnnealing()
    SA.append(sa_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.TabuSearch()
    TA.append(tb_no_idle.UB)

    N.append(machines)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, SA, color="blue", label='Simulated_annealing', linewidth=1, alpha=0.5)
plt.plot(N, TA, color="black", label='Tabu search', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba maszyn")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby maszyn")
plt.grid(True)
plt.show()


####################################################################################################
##Wykres w zaleznosci od ilosci seed

NA = [] 
NEH = []
SA = []
TA = []
N = []

tasks = 7
machines = 4
list_seed = [123,321, 456, 789, 1100, 1234, 1461, 1701, 2123]
for seed in list_seed:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.SimulatedAnnealing()
    SA.append(sa_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.TabuSearch()
    TA.append(tb_no_idle.UB)

    N.append(seed)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, SA, color="blue", label='Simulated_annealing', linewidth=1, alpha=0.5)
plt.plot(N, TA, color="black", label='Tabu search', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba ziarna")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby ziarna")
plt.grid(True)
plt.show()

####################################################################################################
##Wykres w zaleznosci od wykonywanych ruchów Simulated annealing

NA = [] 
NEH = []
SA1 = []
SA2 = []
SA3 = []
SA4 = []
TA = []
N = []

seed = 8785744
machines = 7
list_task = [3,4,5,6,7,8,9,11,13,15,17,19]
for tasks in list_task:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.Moves = 1
    sa_no_idle.SimulatedAnnealing()
    SA1.append(sa_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.Moves = 2
    sa_no_idle.SimulatedAnnealing()
    SA2.append(sa_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.Moves = 3
    sa_no_idle.SimulatedAnnealing()
    SA3.append(sa_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.Moves = 4
    sa_no_idle.SimulatedAnnealing()
    SA4.append(sa_no_idle.UB)

    N.append(tasks)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, SA1, color="blue", label='Simulated annealing - swap', linewidth=1, alpha=0.5)
plt.plot(N, SA2, color="cyan", label='Simulated annealing - insert', linewidth=1, alpha=0.5)
plt.plot(N, SA3, color="magenta", label='Simulated annealing - reverse', linewidth=1, alpha=0.5)
plt.plot(N, SA4, color="black", label='Simulated annealing - adjacent swap', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba zadań")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby zadań")
plt.grid(True)
plt.show()

####################################################################################################
##Wykres w zaleznosci od wspolczynnika alpha Simulated annealing

NA = [] 
NEH = []
SA1 = []
SA2 = []
SA3 = []
SA4 = []
TA = []
N = []

seed = 8785744
machines = 7
list_task = [3,4,5,6,7,8,9,11,13,15,17,19]
for tasks in list_task:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.alpha = 0.99
    sa_no_idle.SimulatedAnnealing()
    SA1.append(sa_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.alpha = 0.95
    sa_no_idle.SimulatedAnnealing()
    SA2.append(sa_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.alpha = 0.9
    sa_no_idle.SimulatedAnnealing()
    SA3.append(sa_no_idle.UB)

    sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
    sa_no_idle.alpha = 0.8
    sa_no_idle.SimulatedAnnealing()
    SA4.append(sa_no_idle.UB)

    N.append(tasks)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, SA1, color="blue", label='Simulated annealing - alpha = 0.99', linewidth=1, alpha=0.5)
plt.plot(N, SA2, color="cyan", label='Simulated annealing - alpha = 0.95', linewidth=1, alpha=0.5)
plt.plot(N, SA3, color="magenta", label='Simulated annealing - alpha = 0.90', linewidth=1, alpha=0.5)
plt.plot(N, SA4, color="black", label='Simulated annealing - alpha = 0.80', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba zadań")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby zadań")
plt.grid(True)
plt.show()


####################################################################################################
##Wykres w zaleznosci od wykonywanych ruchów - Tabu search

NA = [] 
NEH = []
TA1 = []
TA2 = []
TA3 = []
TA4 = []
TA = []
N = []

seed = 8785744
machines = 7
list_task = [3,4,5,6,7,8,9,11,13,15,17,19]
for tasks in list_task:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Moves = 1
    tb_no_idle.TabuSearch()
    TA1.append(tb_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Moves = 2
    tb_no_idle.TabuSearch()
    TA2.append(tb_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Moves = 3
    tb_no_idle.TabuSearch()
    TA3.append(tb_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Moves = 4
    tb_no_idle.TabuSearch()
    TA4.append(tb_no_idle.UB)

    N.append(tasks)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, TA1, color="blue", label='Tabu search - swap', linewidth=1, alpha=0.5)
plt.plot(N, TA2, color="cyan", label='Tabu search - insert', linewidth=1, alpha=0.5)
plt.plot(N, TA3, color="magenta", label='Tabu search - reverse', linewidth=1, alpha=0.5)
plt.plot(N, TA4, color="black", label='Tabu search - adjacent swap', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba zadań")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby zadań")
plt.grid(True)
plt.show()

####################################################################################################
##Wykres w zaleznosci od cadencji - Tabu search

NA = [] 
NEH = []
TA1 = []
TA2 = []
TA3 = []
TA4 = []
TA = []
N = []

seed = 8785744
machines = 7
list_task = [3,4,5,6,7,8,9,11,13,15,17,19]
for tasks in list_task:

    natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
    NA.append(natural_permutation_no_idle.UB)

    neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
    neh_no_idle.DoNEH()
    NEH.append(neh_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Cadance = (int)(tb_no_idle.n/8)
    tb_no_idle.TabuSearch()
    TA1.append(tb_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Cadance = (int)(tb_no_idle.n/4)
    tb_no_idle.TabuSearch()
    TA2.append(tb_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Cadance = (int)(tb_no_idle.n/2)
    tb_no_idle.TabuSearch()
    TA3.append(tb_no_idle.UB)

    tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
    tb_no_idle.Cadance = (int)(tb_no_idle.n/1)
    tb_no_idle.TabuSearch()
    TA4.append(tb_no_idle.UB)

    N.append(tasks)

plt.plot(N, NA, color="red", label='Natural permutation', linewidth=1, alpha=0.5)
plt.plot(N, NEH, color="green", label='NEH_Algorithm', linewidth=1, alpha=0.5)
plt.plot(N, TA1, color="blue", label='Tabu search - Cadence = n/8', linewidth=1, alpha=0.5)
plt.plot(N, TA2, color="cyan", label='Tabu search - Cadence = n/4', linewidth=1, alpha=0.5)
plt.plot(N, TA3, color="magenta", label='Tabu search - Cadence = n/2', linewidth=1, alpha=0.5)
plt.plot(N, TA4, color="black", label='Tabu search - Cadence = n', linewidth=1, alpha=0.5)
plt.legend()
plt.xlabel("Liczba zadań")
plt.ylabel("Cmax")
plt.title("Wykres Cmax w zależności od liczby zadań")
plt.grid(True)
plt.show()






























####################################################################################################
#str1 = "===================================================================\n"
#print (str1 + "NATURAL PERMUTATION NO IDLE")
#natural_permutation_no_idle = Natural_permutation_no_idle(seed, tasks, machines)
##print(natural_permutation)
#print(natural_permutation_no_idle.UB)

#print (str1 + "NEH ALGORITHM NO IDLE")
#neh_no_idle = NEH_Algorithm_no_idle(seed, tasks, machines)
#neh_no_idle.DoNEH()
##print(neh)
#print(neh_no_idle.UB)

#str1 = "===================================================================\n"
#print (str1 + "SIMULATED ANNEALING NO IDLE")
#sa_no_idle = Simulated_annealing_algorithm_no_idle(seed, tasks, machines)
#sa_no_idle.SimulatedAnnealing()
##print(sa)
#print(sa_no_idle.UB)

#print (str1 + "TABU SEARCH NO IDLE")
#tb_no_idle = Tabu_search_algorithm_no_idle(seed, tasks, machines)
#tb_no_idle.TabuSearch()
##print(tb)
#print(tb_no_idle.UB)

#print (str1 + "PORÓWNANIA")
#print("SIMULATED ANNEALING: " + str (round(((neh_no_idle.UB-sa_no_idle.UB)* 100.0/neh_no_idle.UB),2)) + "%")
#print("TABU SEARCH: " + str (round(((neh_no_idle.UB-tb_no_idle.UB)* 100.0/neh_no_idle.UB),2 )) + "%")

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