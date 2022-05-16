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

def dashboard(request):

    country1="ind"
    country2="ind"
    country3="ind"
    country4="ind"
    country5="ind"
    country6="ind"
    indicator1="GDPG"
    indicator2="GDPC"
    indicator3="GDPCG"
    indicator4="TR"
    indicator5="CAB"
    indicator6="CPI"

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

    def indicatorFind(indicator):
        if(indicator == "GDPG"):
            indicator = GDPG
            return indicator
        elif(indicator == "GDPC"):
            indicator = GDPC
            return indicator
        elif(indicator == "GDPCG"):
            indicator = GDPCG
            return indicator
        elif(indicator == "PG"):
            indicator = PG
            return indicator
        elif(indicator == "PP"):
            indicator = PP
            return indicator
        elif(indicator == "UNER"):
            indicator = UNER
            return indicator
        elif(indicator == "ISRP"):
            indicator = ISRP
            return indicator
        elif(indicator == "TR"):
            indicator = TR
            return indicator
        elif(indicator == "CAB"):
            indicator = CAB
            return indicator
        elif(indicator == "EXP"):
            indicator = EXP
            return indicator
        elif(indicator == "CPI"):
            indicator = CPI
            return indicator
        else:
            return HttpResponse("404, Page not found !!!")

    indicator1=indicatorFind(indicator1)
    indicator2=indicatorFind(indicator2)
    indicator3=indicatorFind(indicator3)
    indicator4=indicatorFind(indicator4)
    indicator5=indicatorFind(indicator5)
    indicator6=indicatorFind(indicator6)

    url1 = "http://api.worldbank.org/v2/country/"+country1+"/indicator/" + \
        indicator1+"?format=json&per_page=200&mrv=5&frequency=Y"
    response1 = requests.get(url1).json()
    response1 = json.dumps(response1)
    responseObj1 = json.loads(response1)

    url2 = "http://api.worldbank.org/v2/country/"+country2+"/indicator/" + \
        indicator2+"?format=json&per_page=200&mrv=5&frequency=Y"
    response2 = requests.get(url2).json()
    response2 = json.dumps(response2)
    responseObj2 = json.loads(response2)

    url3 = "http://api.worldbank.org/v2/country/"+country3+"/indicator/" + \
        indicator3+"?format=json&per_page=200&mrv=5&frequency=Y"
    response3 = requests.get(url3).json()
    response3 = json.dumps(response3)
    responseObj3 = json.loads(response3)

    url4 = "http://api.worldbank.org/v2/country/"+country4+"/indicator/" + \
        indicator4+"?format=json&per_page=200&mrv=5&frequency=Y"
    response4 = requests.get(url4).json()
    response4 = json.dumps(response4)
    responseObj4 = json.loads(response4)

    url5 = "http://api.worldbank.org/v2/country/"+country5+"/indicator/" + \
        indicator5+"?format=json&per_page=200&mrv=5&frequency=Y"
    response5 = requests.get(url5).json()
    response5 = json.dumps(response5)
    responseObj5 = json.loads(response5)

    url6 = "http://api.worldbank.org/v2/country/"+country6+"/indicator/" + \
        indicator6+"?format=json&per_page=200&mrv=5&frequency=Y"
    response6 = requests.get(url6).json()
    response6 = json.dumps(response6)
    responseObj6 = json.loads(response6)

    # print(response1)
    # print(response2)
    # print(response3)
    # print(response4)
    # print(response5)
    # print(response6)

    # print(indicator1)
    # print(indicator2)
    # print(indicator3)
    # print(indicator4)
    # print(indicator5)
    # print(indicator6)

    # print(country1+" "+country2+" "+country3+" "+country4+" "+country5+" "+country6)

    response = {
        "Title":"Indian Economy & Financial Markets at a Glance",
        "Body":"",
        "response1": response1, 
        "responseObj1": responseObj1, 
        "response2": response2, 
        "responseObj2": responseObj2, 
        "response3": response3, 
        "responseObj3": responseObj3, 
        "response4": response4, 
        "responseObj4": responseObj4, 
        "response5": response5, 
        "responseObj5": responseObj5, 
        "response6": response6, 
        "responseObj6": responseObj6
    }

    return render(request, 'EcoFin/dashboard.html', {"res":response,"activeHome":"active"})

def about(request):
    response = {
        "Title":"About Us",
        "Body":"About Us",
    }
    return render(request,'EcoFin/about.html',{"res":response,"activeAbout":"active"})

def contact(request):
    response = {
        "Title":"Contact Us",
        "Body":"Contact Us",
    }
    return render(request,'EcoFin/contact.html',{"res":response,"activeContact":"active"})    

def gdp(request):
    response = {
        "Title":"Gross Domestic Product (GDP)",
        "Body":"Gross Domestic Product (GDP)",
    }
    return render(request, 'EcoFin/gdp.html', {"res":response})

def inflation(request):
    response = {
        "Title":"Inflation",
        "Body":"Infilation",
    }
    return render(request, 'EcoFin/inflation.html', {"res":response})

def businessPerformance(request):
    response = {
        "Title":"Business Performance",
        "Body":"Business Performance",
    }
    return render(request, 'EcoFin/businessPerformance.html', {"res":response})

def tradeForex(request):
    response = {
        "Title":"Trade and Forex",
        "Body":"Trade and Forex",
    }
    return render(request, 'EcoFin/tradeForex.html', {"res":response})

def unemployment(request):
    response = {
        "Title":"Unemployment",
        "Body":"Unemployment",
    }
    return render(request, 'EcoFin/unemployment.html', {"res":response})

def fiscalSituation(request):
    response = {
        "Title":"Fiscal Situation",
        "Body":"Fiscal Situation",
    }
    return render(request, 'EcoFin/fiscalSituation.html', {"res":response})

def interestRatesBond(request):
    response = {
        "Title":"Interest Rates & Bond",
        "Body":"Interest Rates & Bond",
    }
    return render(request, 'EcoFin/interestRatesBond.html', {"res":response})

def equityMarkets(request):
    response = {
        "Title":"Equity Markets",
        "Body":"Equity Markets",
    }
    return render(request, 'EcoFin/equityMarkets.html', {"res":response}) 

def commodityMarkets(request):
    response = {
        "Title":"Ccommodity Markets",
        "Body":"Commodity Markets",
    }
    return render(request, 'EcoFin/commodityMarkets.html', {"res":response})

def foreignInvestment(request):
    response = {
        "Title":"Foreign Investment",
        "Body":"Foreign Investment",
    }
    return render(request, 'EcoFin/foreignInvestment.html', {"res":response})

def moneyCredit(request):
    response = {
        "Title":"Money & Credit",
        "Body":"Money & Credit",
    }
    return render(request, 'EcoFin/moneyCredit.html', {"res":response})

def realEstate(request):
    response = {
        "Title":"Real Estate",
        "Body":"Real Estate",
    }
    return render(request, 'EcoFin/realEstate.html', {"res":response})   

def ventureCapitalIPO(request):
    response = {
        "Title":"Venture Capital & IPOs",
        "Body":"Venture Capital & IPOs",
    }
    return render(request, 'EcoFin/ventureCapitalIPO.html', {"res":response})                      