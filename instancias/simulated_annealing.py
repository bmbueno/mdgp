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
        self.bks = 0
        self.min = min
        self.max = max
        self.bksContributionByPerson = [] # Cada pessoa contribui com +X BKS no grupo, esse array vai apontar qual é a pessoa com menos contribuição de BKS.
        

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
        self.elapsedTime = 0
        self.maxElapsedTime = 60 * 5
        self.maxNumberOfIterations = 25

        # Initializing Solution
        self.availablePersons = []
        self.availablePersons.extend(range(0, self.numberOfPersons))
        self.groups = []
        for i in range(self.numberOfGroups):
            group = Group(self.lowerBounds, self.upperBounds)
            self.groups.append(group)

        self.currentSolutionBKS = 0

        self.createInitialSolution()   

    def createInitialSolution(self):
        rand.seed(self.seed)
        randomizedPersons = rand.sample(range(0, self.numberOfPersons), self.numberOfPersons)
        print(randomizedGroup)

        
        #for person in randomizedPersons:
        #    self.availablePersons.remove(person)
        #    for group in self.groups:
        #        if group.

        # Primeiro garantir que os minimos de todos os grupos estao OK
        # Depois caso eu ainda tenha pessoas disponiveis eu garanto todos os maximos dos grupos.
        # Nao vou precisar me preocupar futuramente com essas restrições qnd tiver fazendo swap de pessoas em um grupo.


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
