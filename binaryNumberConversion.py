bits = [[0,2147483648],[0,1073741824],[0,536870912],[0,268435456],[0,134217728],
[0,67108864],[0,33554432],[0,16777216],[0,8388608],[0,4194304],[0,2097152],[0,1048576],[0,524288],
[0,262144],[0,131072],[0,65536],[0,32768],[0,16384],[0,8192],[0,4096],[0,2048],[0,1024],[0,512],[0,256],
[0,128],[0,64],[0,32],[0,16],[0, 8],[0, 4],[0, 2],[0, 1]]

#print(len(bits))

input = int(input())

def invert(string):
    newString = ''

    for i in range(len(string)):
        if string[i] == '0':
            newString += '1'
        else:
            newString += '0'

    return newString

def decToBinary(bits, input):

    suma = 0
    outputString = ""
    currentString = ""

    if input  >= -2147483648 and input <= 2147483648:

        for i in bits:
            if suma + i[1] <= abs(input):
                suma += i[1]
                i[0] = 1

            outputString += str(i[0])

        if input < 0:

            for i in range(len(outputString) - 1, -1, -1):

                currentString += outputString[i]

                if outputString[i] == '1':
                    outputString = invert(outputString[0:i])
                    currentString = currentString[::-1]
                    break


    return outputString + currentString

output = decToBinary(bits, input)

if output == "":
    print("Number in not valid")
else:
    print(output)