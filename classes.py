import dataloader as dl
import numpy as num
import scipy.stats as stats



class statResult:
    mean: float = 0.0
    count = 0
    sd = 0.0
    mode = 0.0
    median = 0.0
    conf95plus = 0.0
    conf95min = 0.0
    
    def __init__(self, data):
        self.mean = sum(data) / len(data);
        self.count = len(data);
        self.median = num.median(data);
        self.mode = float(stats.mode(data, keepdims = True)[0]);
        self.sd = num.std(data)

    def __str__(self):
        return f"Mean: {format(self.mean, '.2f')}\nCount: {self.count}\nMedian: {self.median}\nMode: {self.mode}\nSD: {format(self.sd, '.2f')}";
        
f = dl.loadData()        
res = statResult(f);
print (res);