from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('errorPage',views.errorPage,name="error"),
    path('imfData',views.imfData,name="imfData"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('gdp',views.gdp,name="gdp"),
    path('inflation',views.inflation,name="inflation"),
    path('businessPerformance',views.businessPerformance,name="businessPerformance"),
    path('tradeForex',views.tradeForex,name="tradeForex"),
    path('unemployment',views.unemployment,name="unemployment"),
    path('fiscalSituation',views.fiscalSituation,name="fiscalSituation"),
    path('interestRatesBond',views.interestRatesBond,name="interestRatesBond"),
    path('equityMarkets',views.equityMarkets,name="equityMarkets"),
    path('commodityMarkets',views.commodityMarkets,name="commodityMarkets"),
    path('foreignInvestment',views.foreignInvestment,name="foreignInvestment"),
    path('moneyCredit',views.moneyCredit,name="moneyCredit"),
    path('realEstate',views.realEstate,name="realEstate"),
    path('ventureCapitalIPO',views.ventureCapitalIPO,name="ventureCapitalIPO"),
]