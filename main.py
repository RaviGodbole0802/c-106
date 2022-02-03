from statistics import *
from numpy import DataSource
import plotly_express as px
import csv
import numpy as np



with open ("data.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
 

def getDataSource (data_path):
    icecream_sales=[]
    colddrink_sales=[]
    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            icecream_sales.append(float(row["Temperature"])) 
            colddrink_sales.append(float(row["Ice-cream Sales"]))
    return{"x":icecream_sales,"y":colddrink_sales}

def findCorrelation (datasource):
    correlation= np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation bw temp vs Ice cream sales:- \n ---->", correlation[0,1] )

def setup():
    data_path="data.csv"
    dataSource= getDataSource(data_path)
    findCorrelation(dataSource)
setup()


    