import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    sizeOfTV_sales=[]
    averageTime_sales=[]
    with open(data_path) as f: 
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            sizeOfTV_sales.append(float(row["Size of TV"]))
            averageTime_sales.append(float(row["Average_Time"]))
    return{"x":sizeOfTV_sales,"y":averageTime_sales}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print ("correlation between tv size and tv time:-->",correlation[0,1])
    
def setup():
    data_path="tv.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()







