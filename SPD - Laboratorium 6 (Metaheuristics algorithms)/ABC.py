from Natural_permutation import Natural_permutation
import random
import copy
import math

class ABC(Natural_permutation):
    def __init__ (self, seed, n, m):
        super().__init__(seed, n, m)

        self.MaxIteration = 100
        self.FoodSource = 50
        self.N = (int)(self.FoodSource/2)
        self.D = self.n

        self.limit = 5
        self.trial = []

        for i in range(0, self.N):
            self.trial.append(i)

        self.Pi_star = list(self.Pi)
        self.Pi_new = []  
        self.Position = []
        self.CmaxPosition = []
        self.FitnessPosition = []
        self.ProbabilitiPosition = []
        self.FitnessSum = 0
        
        self.PositionBest = []
        self.CmaxBest = []
        self.FitnessBest = []
        self.ProbabilityBest = []

        #Generate Initial population randomly
        for j in range(0, self.N):
            l = random.randint(0, self.n-1)
            r = random.randint(0, self.n-1)
            #FoodSource
            self.Position.append(list(self.Move(l, r)))
        for j in self.Position:
            #Minimalize
            self.CmaxPosition.append(self.CalculateCustomCmax(j))
            #Maximalize
        for j in self.CmaxPosition:
            self.FitnessPosition.append(self.Fitness(j))
        for j in range(0,len(self.CmaxPosition)):
            self.ProbabilitiPosition.append(0)

    def DoABC(self):
        for x in range(0, self.MaxIteration):
            #self.Position.clear()
            #self.CmaxPosition.clear()
            #self.FitnessPosition.clear()
            #self.ProbabilitiPosition.clear()
            #Employed bee Phase
            for j in range(0, self.N):
               l = random.randint(0, self.n-1)
               r = random.randint(0, self.n-1)
               Pi_new = list(self.Move(l, r))
               #Perform Greedy Selection
               if self.CalculateCustomCmax(Pi_new) < self.CmaxPosition[j]:
                   self.Position[j] = list(self.Move(l, r))
                   self.CmaxPosition[j] = self.CalculateCustomCmax(self.Position[j])
                   self.FitnessPosition[j] = self.Fitness(self.CmaxPosition[j])
               else:
                    self.trial[j] = self.trial[j] + 1

            #Calculate probabilities
            for i in self.FitnessPosition:
                self.FitnessSum = self.FitnessSum + i
            q = 0
            for i in self.FitnessPosition:
                self.ProbabilitiPosition[q] = (i/self.FitnessSum)
                q = q + 1

            #Onlooker bee phase
            for i in range(0, len(self.ProbabilitiPosition)):
                r = random.random()
                if(r < self.ProbabilitiPosition[i]):
                       l = random.randint(0, self.n-1)
                       r = random.randint(0, self.n-1)
                       Pi_new = list(self.Move(l, r))
                       #Perform Greedy Selection
                       if self.CalculateCustomCmax(Pi_new) < self.CmaxPosition[j]:
                           self.Position[i] = list(self.Move(l, r))
                           self.CmaxPosition[i] = self.CalculateCustomCmax(self.Position[j])
                           self.FitnessPosition[i] = self.Fitness(self.CmaxPosition[j])
                       else:
                            self.trial[i] = self.trial[i] + 1
            #Memory the best solution so far
            bestIndex = self.MinIndex()
            if self.CalculateCustomCmax(self.Pi) > self.CalculateCustomCmax(self.Position[bestIndex]):
                self.Pi = list(self.Position[bestIndex])
            #self.CmaxBest.append(Position[bestIndex])
            #self.FitnessBest.append(FinessPosition[bestIndex])
            #self.ProbabilityBest.append(ProbabilityPosition[bestIndex])
            #Scoutt phase
            for p in range(0,len(self.trial)):
                 if(self.trial[p] > self.limit):
                    l = random.randint(0, self.n-1)
                    r = random.randint(0, self.n-1)
                    self.Position[p] = (list(self.Move(l, r)))
                    self.CmaxPosition[p] = self.CalculateCustomCmax(self.Position[p])
                    self.FitnessPosition[p] = self.Fitness(self.CmaxPosition[p])
        self.CalculateCmax()
        self.CalculateSmax()
        self.UB = self.C[self.n-1][self.m-1]        
                

    def Move(self, i, j):
        Pi = list(self.Pi)
        x = Pi[i]
        del Pi[i]
        Pi.insert(j,x)
        return Pi

    def Swap(self, i):
        Pi = list(self.Pi)
        x = Pi[i]
        Pi[i] = Pi[i+1]
        Pi[i+1] = x
        return Pi

    def MinIndex(self):
        Min = 100000
        MinIndex = 0
        for i in range(0,len(self.ProbabilitiPosition)):
            if Min > self.ProbabilitiPosition[i]:
                Min = self.ProbabilitiPosition[i]
                MinIndex = i
        return MinIndex

    def Fitness(self, Cmax):
        return 1/(1+Cmax)

    def __str__(self):
        str1 = "===================================================================\n"
        return str1 + " Pi=" + str(self.Pi) + "\n" + str1 + "\n P=" + str(self.P) + "\n" + str1 + "\n S=" + str(self.S) + "\n" + str1 + "\n C=" + str(self.C) + "\n" + str1 + str(self.UB)