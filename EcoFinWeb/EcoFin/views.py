import re
from urllib import response
from xml.etree.ElementTree import tostring
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
import requests
import json
from urllib3 import HTTPResponse


def imfAPI(database, frequency, countries, indicators, startPeriod, endPeriod):
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/'+database+'/' + \
        frequency+'.'+countries+'.'+indicators+ \
        '?startPeriod='+startPeriod+'&endPeriod='+endPeriod
    responseIMF = requests.get(url).json()
    jsonData = responseIMF
    series = jsonData['CompactData']['DataSet']['Series']
    extData = []
    for s in series:
        newSeries = []
        countryCode = s['@REF_AREA']
        indicatorCode = s['@INDICATOR']
        timeSeries = []
        for i in s['Obs']:
            timeSeries.append(
                dict({"time": i['@TIME_PERIOD'], "value": i['@OBS_VALUE']}))
        newSeries.append(dict(
            {"countryCode": countryCode, "indicatorCode": indicatorCode, "timeSeries": timeSeries}))
        extData.append(newSeries)
    return extData

# Creating views here.


def home(request):

    # IMF DATA
    # startPeriod = str(2010)
    # endPeriod = str(2022)
    # indicators = 'NGDP_RPCH'
    # countries = 'IN+BD+ID+TL+VN'
    # frequency = 'A'
    # database = 'APDREO'

    extData2 = imfAPI('IFS', 'A', 'IN+BD+BR+TR+VN',
                      'AIP_IX', str(2010), str(2022))
    extData3 = imfAPI('APDREO', 'A', 'IN+BD+ID+TL+VN',
                      'NGDP_RPCH', str(2010), str(2022))
    extData4 = imfAPI('DOT', 'M', 'IN+BD+ID+TL+VN',
                      'TXG_FOB_USD.W00', str(2010), str(2022))

    # with open('data.json', 'w') as jsonfile:
    #     json.dump(response, jsonfile)
    # print(response)
    # f = open('data.json')
    # response = json.load(f)

    extDataJson2 = json.dumps(extData2)
    extDataObj2 = json.loads(extDataJson2)

    extDataJson3 = json.dumps(extData3)
    extDataObj3 = json.loads(extDataJson3)

    extDataJson4 = json.dumps(extData4)
    extDataObj4 = json.loads(extDataJson4)

    return render(request, 'EcoFin/imf.html', {'extDataJson2': extDataJson2, 'extDataObj2': extDataObj2,
                                               'extDataJson3': extDataJson3, 'extDataObj3': extDataObj3,
                                               'extDataJson4': extDataJson4, 'extDataObj4': extDataObj4,})


def dashboard(request):

    country1 = "ind"
    country2 = "ind"
    country3 = "ind"
    country4 = "ind"
    country5 = "ind"
    country6 = "ind"
    country7 = "ind"
    country8 = "ind"
    country9 = "ind"
    country10 = "ind"
    country11 = "ind"
    country12 = "ind"
    country13 = "ind"

    indicator1 = "GDPG"
    indicator2 = "GDPC"
    indicator3 = "GDPCG"
    indicator4 = "PP"
    indicator5 = "PG"
    indicator6 = "UNER"
    indicator7 = "ISRP"
    indicator8 = "TR"
    indicator9 = "CAB"
    indicator10 = "EXP"
    indicator11 = "CPI"
    indicator12 = "GDPG"
    indicator13 = "GDPC"

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

    indicator1 = indicatorFind(indicator1)
    indicator2 = indicatorFind(indicator2)
    indicator3 = indicatorFind(indicator3)
    indicator4 = indicatorFind(indicator4)
    indicator5 = indicatorFind(indicator5)
    indicator6 = indicatorFind(indicator6)
    indicator7 = indicatorFind(indicator7)
    indicator8 = indicatorFind(indicator8)
    indicator9 = indicatorFind(indicator9)
    indicator10 = indicatorFind(indicator10)
    indicator11 = indicatorFind(indicator11)
    indicator12 = indicatorFind(indicator12)
    indicator13 = indicatorFind(indicator13)

    url1 = "http://api.worldbank.org/v2/country/"+country1+"/indicator/" + \
        indicator1+"?format=json&per_page=200&mrv=10&frequency=Y"
    response1 = requests.get(url1).json()
    response1 = json.dumps(response1)
    responseObj1 = json.loads(response1)

    url2 = "http://api.worldbank.org/v2/country/"+country2+"/indicator/" + \
        indicator2+"?format=json&per_page=200&mrv=10&frequency=Y"
    response2 = requests.get(url2).json()
    response2 = json.dumps(response2)
    responseObj2 = json.loads(response2)

    url3 = "http://api.worldbank.org/v2/country/"+country3+"/indicator/" + \
        indicator3+"?format=json&per_page=200&mrv=10&frequency=Y"
    response3 = requests.get(url3).json()
    response3 = json.dumps(response3)
    responseObj3 = json.loads(response3)

    url4 = "http://api.worldbank.org/v2/country/"+country4+"/indicator/" + \
        indicator4+"?format=json&per_page=200&mrv=10&frequency=Y"
    response4 = requests.get(url4).json()
    response4 = json.dumps(response4)
    responseObj4 = json.loads(response4)

    url5 = "http://api.worldbank.org/v2/country/"+country5+"/indicator/" + \
        indicator5+"?format=json&per_page=200&mrv=10&frequency=Y"
    response5 = requests.get(url5).json()
    response5 = json.dumps(response5)
    responseObj5 = json.loads(response5)

    url6 = "http://api.worldbank.org/v2/country/"+country6+"/indicator/" + \
        indicator6+"?format=json&per_page=200&mrv=10&frequency=Y"
    response6 = requests.get(url6).json()
    response6 = json.dumps(response6)
    responseObj6 = json.loads(response6)

    url7 = "http://api.worldbank.org/v2/country/"+country7+"/indicator/" + \
        indicator7+"?format=json&per_page=200&mrv=10&frequency=Y"
    response7 = requests.get(url7).json()
    response7 = json.dumps(response7)
    responseObj7 = json.loads(response7)

    url8 = "http://api.worldbank.org/v2/country/"+country8+"/indicator/" + \
        indicator8+"?format=json&per_page=200&mrv=10&frequency=Y"
    response8 = requests.get(url8).json()
    response8 = json.dumps(response8)
    responseObj8 = json.loads(response8)

    url9 = "http://api.worldbank.org/v2/country/"+country9+"/indicator/" + \
        indicator9+"?format=json&per_page=200&mrv=10&frequency=Y"
    response9 = requests.get(url9).json()
    response9 = json.dumps(response9)
    responseObj9 = json.loads(response9)

    url10 = "http://api.worldbank.org/v2/country/"+country10+"/indicator/" + \
        indicator10+"?format=json&per_page=200&mrv=10&frequency=Y"
    response10 = requests.get(url10).json()
    response10 = json.dumps(response10)
    responseObj10 = json.loads(response10)

    url11 = "http://api.worldbank.org/v2/country/"+country11+"/indicator/" + \
        indicator11+"?format=json&per_page=200&mrv=10&frequency=Y"
    response11 = requests.get(url11).json()
    response11 = json.dumps(response11)
    responseObj11 = json.loads(response11)

    url12 = "http://api.worldbank.org/v2/country/"+country12+"/indicator/" + \
        indicator12+"?format=json&per_page=200&mrv=10&frequency=Y"
    response12 = requests.get(url12).json()
    response12 = json.dumps(response12)
    responseObj12 = json.loads(response12)

    url13 = "http://api.worldbank.org/v2/country/"+country13+"/indicator/" + \
        indicator13+"?format=json&per_page=200&mrv=10&frequency=Y"
    response13 = requests.get(url13).json()
    response13 = json.dumps(response13)
    responseObj13 = json.loads(response13)

    response = {
        "Title": "At a Glance: Indian Economy and Financial Markets",
        "Body": "",
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
        "responseObj6": responseObj6,
        "response7": response7,
        "responseObj7": responseObj7,
        "response8": response8,
        "responseObj8": responseObj8,
        "response9": response9,
        "responseObj9": responseObj9,
        "response10": response10,
        "responseObj10": responseObj10,
        "response11": response11,
        "responseObj11": responseObj11,
        "response12": response12,
        "responseObj12": responseObj12,
        "response13": response13,
        "responseObj13": responseObj13,
    }

    return render(request, 'EcoFin/dashboard.html', {"res": response, "activeHome": "active"})


def about(request):
    response = {
        "Title": "About Us",
        "Body": "About Us",
    }
    return render(request, 'EcoFin/about.html', {"res": response, "activeAbout": "active"})


def contact(request):
    response = {
        "Title": "Contact Us",
        "Body": "Contact Us",
    }
    return render(request, 'EcoFin/contact.html', {"res": response, "activeContact": "active"})


def gdp(request):
    response = {
        "Title": "Gross Domestic Product (GDP)",
        "Body": "Gross Domestic Product (GDP)",
    }
    return render(request, 'EcoFin/gdp.html', {"res": response})


def inflation(request):
    response = {
        "Title": "Inflation",
        "Body": "Infilation",
    }
    return render(request, 'EcoFin/inflation.html', {"res": response})


def businessPerformance(request):
    response = {
        "Title": "Business Performance",
        "Body": "Business Performance",
    }
    return render(request, 'EcoFin/businessPerformance.html', {"res": response})


def tradeForex(request):
    response = {
        "Title": "Trade and Forex",
        "Body": "Trade and Forex",
    }
    return render(request, 'EcoFin/tradeForex.html', {"res": response})


def unemployment(request):
    response = {
        "Title": "Unemployment",
        "Body": "Unemployment",
    }
    return render(request, 'EcoFin/unemployment.html', {"res": response})


def fiscalSituation(request):
    response = {
        "Title": "Fiscal Situation",
        "Body": "Fiscal Situation",
    }
    return render(request, 'EcoFin/fiscalSituation.html', {"res": response})


def interestRatesBond(request):
    response = {
        "Title": "Interest Rates & Bond",
        "Body": "Interest Rates & Bond",
    }
    return render(request, 'EcoFin/interestRatesBond.html', {"res": response})


def equityMarkets(request):
    response = {
        "Title": "Equity Markets",
        "Body": "Equity Markets",
    }
    return render(request, 'EcoFin/equityMarkets.html', {"res": response})


def commodityMarkets(request):
    response = {
        "Title": "Ccommodity Markets",
        "Body": "Commodity Markets",
    }
    return render(request, 'EcoFin/commodityMarkets.html', {"res": response})


def foreignInvestment(request):
    response = {
        "Title": "Foreign Investment",
        "Body": "Foreign Investment",
    }
    return render(request, 'EcoFin/foreignInvestment.html', {"res": response})


def moneyCredit(request):
    response = {
        "Title": "Money & Credit",
        "Body": "Money & Credit",
    }
    return render(request, 'EcoFin/moneyCredit.html', {"res": response})


def realEstate(request):
    response = {
        "Title": "Real Estate",
        "Body": "Real Estate",
    }
    return render(request, 'EcoFin/realEstate.html', {"res": response})


def ventureCapitalIPO(request):
    response = {
        "Title": "Venture Capital & IPOs",
        "Body": "Venture Capital & IPOs",
    }
    return render(request, 'EcoFin/ventureCapitalIPO.html', {"res": response})
