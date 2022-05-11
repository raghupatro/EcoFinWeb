from urllib import response
from django.http import Http404, HttpResponse
from django.shortcuts import render
import requests,json

# Creating views here.
def home(request): 

    # IMF DATA

    # url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    # key = 'CompactData/IFS/M.GB.PMP_IX' # adjust codes here 
    # response = (requests.get(f'{url}{key}').json()) # Navigate to series in API-returned JSON data

    # with open('data.json', 'w') as jsonfile:
        # json.dump(response, jsonfile)
    f = open('data.json')
    response = json.load(f)

    jsonData = response
    obsData = jsonData['CompactData']['DataSet']['Series']['Obs']

    extData = []

    # Extracting useful data from json response and creating a new python dict object list extData[]. 
    for i in obsData:
        extData.append(dict({"time":i['@TIME_PERIOD'],"obsValue":i['@OBS_VALUE']}))

    # Converting extracted data to json format.
    extDataJson = json.dumps(extData) 

    # Converting extracted data to json object.
    extDataObj = json.loads(extDataJson)    

    # Passing extDataJson and extDataObj datas to (home.html) template.
    return render(request,'EcoFin/imf.html',{'extDataJson':extDataJson,'extDataObj':extDataObj})

def wb(request,country="all",indicator="GDPG"):

    # WORLD BANK DATA

    GDPG = "NY.GDP.MKTP.KD.ZG" # GDP growth (annual %)
    GDPC = "NY.GDP.PCAP.CD" # GDP Per Capita (annual %)
    GDPCG = "NY.GDP.PCAP.KD.ZG" # GDP Per Capita Growth Rate (annual %)
    PP = "SP.POP.TOTL" # Population
    PG = "SP.POP.GROW" # Population growth (annual %)
    UNER = "SL.UEM.TOTL.ZS" # Unemployment Rate (annual %)
    ISRP = "FP.CPI.TOTL.ZG" # Inflation Rate Consumer Prices
    TR = "FI.RES.TOTL.CD" # Total Reserves
    CAB = "BN.CAB.XOKA.CD" # Current Account Balance
    EXP = "GC.XPN.TOTL.GD.ZS" # Expense

    if(indicator=="GDPG"):
        indicator=GDPG
    elif(indicator=="GDPC"):
        indicator=GDPC
    elif(indicator=="GDPCG"):
        indicator=GDPCG        
    elif(indicator=="PG"):
        indicator=PG
    elif(indicator=="PP"):
        indicator=PP    
    elif(indicator=="UNER"):
        indicator=UNER
    elif(indicator=="ISRP"):
        indicator=ISRP
    elif(indicator=="TR"):
        indicator=TR 
    elif(indicator=="CAB"):
        indicator=CAB
    elif(indicator=="EXP"):
        indicator=EXP                       
    else:
        return HttpResponse("404, Page not found !!!")       

    url = "http://api.worldbank.org/v2/country/"+country+"/indicator/"+indicator+"?format=json&per_page=200"
    response = requests.get(url).json()
    response = json.dumps(response)
    responseObj = json.loads(response)
    # print(response)

    # print(responseObj[1][1]['date']) 
    # print(responseObj[1][1]['value'])

    return render(request,'EcoFin/wb.html',{"response":response,"responseObj":responseObj})    