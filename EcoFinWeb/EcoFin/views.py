from urllib import response
from django.http import Http404, HttpResponse
from django.shortcuts import render
import requests
import json

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
        extData.append(
            dict({"time": i['@TIME_PERIOD'], "obsValue": i['@OBS_VALUE']}))

    # Converting extracted data to json format.
    extDataJson = json.dumps(extData)

    # Converting extracted data to json object.
    extDataObj = json.loads(extDataJson)

    # Passing extDataJson and extDataObj datas to (home.html) template.
    return render(request, 'EcoFin/imf.html', {'extDataJson': extDataJson, 'extDataObj': extDataObj})


def wb(request, country1="all",country2="all",country3="all",country4="all",country5="all", indicator="GDPG"):

    # WORLD BANK DATA

    GDPG = "NY.GDP.MKTP.KD.ZG"  # GDP growth (annual %)
    GDPC = "NY.GDP.PCAP.CD"  # GDP Per Capita (annual %)
    GDPCG = "NY.GDP.PCAP.KD.ZG"  # GDP Per Capita Growth Rate (annual %)
    PP = "SP.POP.TOTL"  # Population
    PG = "SP.POP.GROW"  # Population growth (annual %)
    UNER = "SL.UEM.TOTL.ZS"  # Unemployment Rate (annual %)
    ISRP = "FP.CPI.TOTL.ZG"  # Inflation Rate Consumer Prices
    TR = "FI.RES.TOTL.CD"  # Total Reserves
    CAB = "BN.CAB.XOKA.CD"  # Current Account Balance
    EXP = "GC.XPN.TOTL.GD.ZS"  # Expense
    CPI = "FP.CPI.TOTL"  # Consumer Price Index

    if(indicator == "GDPG"):
        indicator = GDPG
    elif(indicator == "GDPC"):
        indicator = GDPC
    elif(indicator == "GDPCG"):
        indicator = GDPCG
    elif(indicator == "PG"):
        indicator = PG
    elif(indicator == "PP"):
        indicator = PP
    elif(indicator == "UNER"):
        indicator = UNER
    elif(indicator == "ISRP"):
        indicator = ISRP
    elif(indicator == "TR"):
        indicator = TR
    elif(indicator == "CAB"):
        indicator = CAB
    elif(indicator == "EXP"):
        indicator = EXP
    elif(indicator == "CPI"):
        indicator = CPI
    else:
        return HttpResponse("404, Page not found !!!")

    url1 = "http://api.worldbank.org/v2/country/"+country1+"/indicator/" + \
        indicator+"?format=json&per_page=200&mrv=5&frequency=Y"
    response1 = requests.get(url1).json()
    response1 = json.dumps(response1)
    responseObj1 = json.loads(response1)

    url2 = "http://api.worldbank.org/v2/country/"+country2+"/indicator/" + \
        indicator+"?format=json&per_page=200&mrv=5&frequency=Y"
    response2 = requests.get(url2).json()
    response2 = json.dumps(response2)
    responseObj2 = json.loads(response2)

    url3 = "http://api.worldbank.org/v2/country/"+country3+"/indicator/" + \
        indicator+"?format=json&per_page=200&mrv=5&frequency=Y"
    response3 = requests.get(url3).json()
    response3 = json.dumps(response3)
    responseObj3 = json.loads(response3)

    url4 = "http://api.worldbank.org/v2/country/"+country4+"/indicator/" + \
        indicator+"?format=json&per_page=200&mrv=5&frequency=Y"
    response4 = requests.get(url4).json()
    response4 = json.dumps(response4)
    responseObj4 = json.loads(response4)

    url5 = "http://api.worldbank.org/v2/country/"+country5+"/indicator/" + \
        indicator+"?format=json&per_page=200&mrv=5&frequency=Y"
    response5 = requests.get(url5).json()
    response5 = json.dumps(response5)
    responseObj5 = json.loads(response5)

    # print(response1)
    # print(response2)
    # print(response3)
    # print(response4)
    # print(response5)

    print(country1+" "+country2+" "+country3+" "+country4+" "+country5)

    return render(request, 'EcoFin/wb.html', {"response1": response1, "responseObj1": responseObj1, "response2": response2, "responseObj2": responseObj2, "response3": response3, "responseObj3": responseObj3})
