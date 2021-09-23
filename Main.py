import csv
import numpy as np

def getDataSource(gg):
    size=[]
    watch = []
    
    with open(gg,newline="") as f:  
        reader = csv.DictReader(f)
        for d in reader:
            size.append(float(d["Temperature"]))
            watch.append(float(d["Ice-cream Sales"]))
            return{"x":size,"y":watch}
        
def getCorrelation(data):
    sus = np.corrcoef(data["x"],data["y"])
    print("correlation is: \n--->",sus[0,1])
    
def setup():
    gg = "2.csv"
    data = getDataSource(gg)
    getCorrelation(data)
    
setup()    