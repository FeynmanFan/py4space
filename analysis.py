def loadData():
    data = [];
	#load the data from the file
    f = open("numbers.txt")
    for x in f:
        data.append(int(x));
    
    return data;
    
data = loadData()

print (f'Sum of set: {sum(data)}')

if any(map(lambda x: x == 17, data)):
    print ("Contains seventeen")
    
print (f"Average value: {sum(data) / len(data)}")
        

