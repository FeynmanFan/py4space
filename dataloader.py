def loadData(fileName = "numbers.txt"):
    data = [];
	#load the data from the file
    try:
        f = open(fileName)
    except Exception as error:
        print(f"An exception occurred while trying to open '{fileName}'")
        print(f"Exception details: {error}")
    else:
        for x in f:
            data.append(int(x));
        f.close()
        return data;
        
