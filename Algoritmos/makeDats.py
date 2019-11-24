
def makeDats(fileName):

    file = open(fileName + '.txt', 'r')
    fileDat = open(fileName + '.dat','w')

    fileDat.write('data;\n')
    firstLine = file.readline()

    firstLine = firstLine.strip()       # retira /n's
    firstLine = firstLine.split()       # str -> lista

    fileDat.write('set M := ')
    for i in range(int(firstLine[1])):
        fileDat.write('\n' + '    ' + str(i))
    
    fileDat.write('\n;\n')

    fileDat.write('set N := ')
    for i in range(int(firstLine[0])):
        fileDat.write('\n' + '    ' + str(i))

    sizeGroup = firstLine[3:]

    fileDat.write('\n;\n')

    fileDat.write('param a := ')
    j = 0
    for i in range(0,len(sizeGroup),2):
        fileDat.write('\n    ' + str(j) + ' ' + sizeGroup[i])
        j = j + 1        
    fileDat.write('\n;\n')

    fileDat.write('param b := ')
    j = 0
    for i in range(1,len(sizeGroup),2):
        fileDat.write('\n    ' + str(j) + ' ' + sizeGroup[i])
        j = j + 1        
    fileDat.write('\n;\n')


    lines = file.readlines()

    fileDat.write('param d := \n')
    for line in lines:
        fileDat.write('    ' + line)
    fileDat.write(';\n')   

    fileDat.close()
    file.close() 

if __name__ == "__main__":
     makeDats('Geo_n010_ss_10')
     makeDats('Geo_n030_ds_08')
     makeDats('Geo_n060_ss_04')
     makeDats('RanInt_n010_ds_07')
     makeDats('RanInt_n010_ss_10')
     makeDats('RanInt_n012_ss_03')
     makeDats('RanInt_n030_ss_05')
     makeDats('RanInt_n060_ds_03')
     makeDats('RanReal_n010_ss_10')
     makeDats('RanReal_n060_ss_04')
    