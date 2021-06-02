from Natural_permutation_no_idle import Natural_permutation_no_idle
from NEH_Algorithm_no_idle import NEH_Algorithm_no_idle
import random
import copy
import math

class Simulated_annealing_algorithm_no_idle(Natural_permutation_no_idle):
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)

        #Algorytm neh jako start
        neh_no_idle = NEH_Algorithm_no_idle(seed, n, m)
        neh_no_idle.DoNEH()
        self.Pi  = list(neh_no_idle.Pi)
        self.Pi_star  = list(neh_no_idle.Pi)
        self.T = neh_no_idle.UB
        self.Tend = 0.1 * neh_no_idle.UB

        self.alpha = 0.98
        self.era = 50

        self.Moves = 1

    def SimulatedAnnealing(self):
        while(self.T > self.Tend):
            for k in range(0,self.era):
                i = random.randint(0, self.n-1)
                j = random.randint(0, self.n-1)
                self.Pi_new = list(self.Move(i, j))
                if self.CalculateCustomCmax(self.Pi_new) > self.CalculateCustomCmax(self.Pi):
                    self.r = random.random()
                    if r >= math.exp((self.CalculateCustomCmax(self.Pi) - self.CalculateCustomCmax(self.Pi_new))/T):
                        self.Pi_new=copy.deepcopy(self.Pi)
                self.Pi = list(self.Pi_new)
                if self.CalculateCustomCmax(self.Pi) < self.CalculateCustomCmax(self.Pi_star):
                    self.Pi_star = list(self.Pi_new)
            self.ReduceTemperature()
        self.Pi = list(self.Pi_star)
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = self.C[self.n-1][self.m-1]

    def ReduceTemperature(self):
        self.T = copy.deepcopy(self.T*self.alpha)

    def Move(self, i, j):
        if self.Moves == 1:
            x = self.Pi[i]
            self.Pi[i] = self.Pi[j]
            self.Pi[j] = x
        elif self.Moves == 2:
            x = self.Pi[i]
            del self.Pi[i]
            self.Pi.insert(j,x)
        elif self.Moves == 3:
            tmp = []
            tmp_index = 0
            if i < j:
                tmp_index = i
                while i < j:
                    tmp.append(self.Pi[i])
                    i = i + 1
            else:
                tmp_index = j
                while j < i:
                    tmp.append(self.Pi[j])
                    j = j + 1
            tmp.reverse()
            b = 0
            while tmp_index < i:
                self.Pi[tmp_index] = tmp[b]
                b = b + 1
                tmp_index = tmp_index +1
        elif self.Moves == 4:
            x = self.Pi[i]
            if i < (self.n - 1):
                self.Pi[i] = self.Pi[i+1]
                self.Pi[i+1] = x
            else:
                self.Pi[i] = self.Pi[i-1]
                self.Pi[i-1] = x
        return self.Pi

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)
