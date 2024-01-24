myfile = open("scores.csv", "r")
data = myfile.read()
myfile.close()
data = data.split("\n")
for i in range(len(data)):
    data[i] = data[i].split(",")
    data[i][1] = int(data[i][1])

swapped = True
while swapped == True:
    swapped = False
    for i in range(1, len(data)):
        if data[i - 1][1] > data[i][1] :
            temp = data[i - 1]
            data[i - 1] = data[i]
            data[i] = temp
            swapped = True

print(data)