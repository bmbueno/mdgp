
def getData(fileName):

    file = open(fileName, 'r')

    firstLine = file.readline()

    firstLine = firstLine.strip()       # retira /n's
    firstLine = firstLine.split()       # str -> lista

    m = int(firstLine[0])               # primeiro termo, numero de pessoas
    n = int(firstLine[1])               # segundo termo, numero de grupos
    sizeGroup = firstLine[3:]           # demais termos, limite sup e inf dos grupos

    a = []
    b = []

    for i in range(0,len(sizeGroup),2):
        a.append(int(sizeGroup[i])) 
        b.append(int(sizeGroup[i+1]))

    lines = file.readlines()

    d = []

    for line in lines:
        line = line.strip()
        line = line.split()
        d.append((int(line[0]),int(line[1]),float(line[2])))

        
    return [m,n,a,b,d]

def main():
    
    data = getData('Geo_n010_ss_10.txt')
    print data[4]

if __name__ == "__main__":
    main()