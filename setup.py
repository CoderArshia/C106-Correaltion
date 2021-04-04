import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    icecream_sales=[]
    coldDrink_sales=[]
    with open(data_path) as f: 
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            icecream_sales.append(float(row["Ice-cream Sales"]))
            coldDrink_sales.append(float(row["Cold drink sales"]))
    return{"x":icecream_sales,"y":coldDrink_sales}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print ("correlation between temperature and icecream sales:-->",correlation[0,1])
    
def setup():
    data_path="temperature.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()







