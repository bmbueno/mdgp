import argparse as parser
import numpy as np
import random as rand
import math

# Global Variables

logpath = 'resultados/'

# Group Class
class Group:
    def __init__(self, min, max):
        self.currentPeople = []
        self.BKS = 0.0
        self.min = min
        self.max = max
        self.bksContributionByPerson = [] # Cada pessoa contribui com +X BKS no grupo
        self.indexOfLeastContributingPerson = 0 # Indicates least contributing person's in the group currently

    def calculateBKS(self, personRelations):
        # Calculate the BKS of the group and select contribution by person and etc.
        self.currentPeople.sort()
        self.BKS = 0.0
        self.bksContributionByPerson = [0.0] * len(self.currentPeople) # Starting all bks contributions with 0.
        for i in range(0, len(self.currentPeople), 1):
            for j in range(i + 1, len(self.currentPeople), 1):
                personOne = self.currentPeople[i]
                personTwo = self.currentPeople[j]
                bks = self.getBKSValue(personOne, personTwo, personRelations)
                self.bksContributionByPerson[i] += bks
                self.bksContributionByPerson[j] += bks
                self.BKS += bks

        self.indexOfLeastContributingPerson = 0
        for i in range(0,len(self.currentPeople), 1):
            if self.bksContributionByPerson[i] < self.bksContributionByPerson[self.indexOfLeastContributingPerson]:
                self.indexOfLeastContributingPerson = i

        print(self.indexOfLeastContributingPerson)
        print(self.currentPeople[self.indexOfLeastContributingPerson])
            
        

            
        

    def getBKSValue(self, personOne, personTwo, personRelations) -> float:
        valueBKS = 0.0

        for relation in personRelations:
            if relation[0] == personOne and relation[1] == personTwo:
                valueBKS = relation[2]
                return valueBKS



# Simulated Annealing
class SimulatedAnnealing:
    def __init__(self, numberOfPersons, numberOfGroups, lowerBounds, upperBounds, personRelations, seed):
        prettyPrintLine('Simulated Annealing')

        # Model Variables
        self.numberOfPersons = numberOfPersons
        self.numberOfGroups = numberOfGroups
        self.lowerBounds = lowerBounds
        self.upperBounds = upperBounds
        self.personRelations = personRelations
        self.seed = seed

        # Problem Variables
        self.maxElapsedTime = 60 * 5
        self.maxNumberOfIterations = 25

        # Initializing Solution
        self.groups = []
        for i in range(self.numberOfGroups):
            group = Group(self.lowerBounds[i], self.upperBounds[i])
            self.groups.append(group)

        self.currentSolutionBKS = 0

        self.createInitialSolution()

        self.runEpisode()

    def createInitialSolution(self):
        rand.seed(self.seed)
        self.availablePersons = rand.sample(range(0, self.numberOfPersons), self.numberOfPersons)

        self.createGroup(True) # Guarantee Min of Groups
        self.createGroup(False) # Guarantee Max of Groups

        for group in self.groups:
            # Calculate BKS of group
            group.calculateBKS(self.personRelations)
            self.currentSolutionBKS += group.BKS

        prettyPrintLine('Test')
        print(self.groups[0].currentPeople)
        self.groups[0].calculateBKS(self.personRelations)


    def createGroup(self, isMin):
        for person in self.availablePersons[:]:
            for group in self.groups:
                comparisonType = group.min if isMin else group.max
                if len(group.currentPeople) < comparisonType:
                    group.currentPeople.append(person)
                    self.availablePersons.remove(person)
                    break
    
    def runEpisode(self):
        # Step one - Vars (max iterations, time elapsed)
        # Step two - Open file to save logs
        # Step three - Save best BKS for initial solution.
        # Step four - Start time elaped
        # Step five - Start Simulated Annealing
            # Step six - generate random neighboor switching 2 persons from each group. (See smarter way to chose neighboors)
            # Step seven - Calculate temp BKS for new solution
            # Step eight - Test
                # Step nine - If good solution accept it and go to next iteration
                # Step ten - If worst solution accept it with SA probability
        # Step eleven - Stop elapsed time
        # Step twelve - Save all the shit in a log file
        print('oi')

# Parsing and Modeling
def parseFile() -> parser.Namespace:
    prettyPrintLine('Parsing Data')
    myParser = parser.ArgumentParser(description = 'Parser for mdgp problem')

    myParser.add_argument('-f', '--file', help = 'File to be parsed', nargs = 1, type = parser.FileType('r')) 
    myParser.add_argument('-o', '--output', help = 'Should create output file', action = 'store_true') 
    myParser.add_argument('-s', '--seed', help = 'Seed for the problem', type = str)

    args = myParser.parse_args()

    printDone()

    return args

def createProblemModel(args) -> (int, int, list, list, list):
    prettyPrintLine('Creating Model')
    file = open(args.file[0].name)
    shouldCreateOutputFile = args.output
    seed = args.seed

    firstLine = file.readline()
    firstLine = firstLine.strip()
    firstLine = firstLine.split()

    numberOfPersons = int(firstLine[0])
    numberOfGroups = int(firstLine[1])
    sizeGroup = firstLine[3:]
    lowerBounds = []
    upperBounds = []
    for i in range(0,len(sizeGroup),2):
        lowerBounds.append(int(sizeGroup[i]))
        upperBounds.append(int(sizeGroup[i+1]))
    
    lines = file.readlines()

    personRelations = []
    for line in lines:
        line = line.strip()
        line = line.split()
        personRelations.append((int(line[0]),int(line[1]),float(line[2])))

    printDone()

    return numberOfPersons, numberOfGroups, lowerBounds, upperBounds, personRelations, seed

# AUX Functions
def prettyPrintLine(string):
    print('\n######### {} #########'.format(string))

def printDone():
    print('DONE')

# Main
if __name__ == "__main__":
    parsedData = parseFile()
    model = createProblemModel(parsedData)

    SimulatedAnnealing(model[0], model[1], model[2], model[3], model[4], model[5])
