def getFibs(count):
    fibs = [1] 
    while len(fibs) < count:
           
        if (len(fibs) == 1):
            nextValue = fibs[0] * 2
        else:
            nextValue = fibs[len(fibs) - 1] + fibs[len(fibs) - 2] 
        fibs.append(nextValue)
    return fibs
    
fibs = getFibs(15);

for x in fibs:
    print(x);

