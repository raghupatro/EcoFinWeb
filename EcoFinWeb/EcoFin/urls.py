from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('wb/<slug:country1>;<slug:country2>;<slug:country3>;<slug:country4>;<slug:country5>/<slug:indicator1>/<slug:indicator2>/<slug:indicator3>/<slug:indicator4>/<slug:indicator5>',views.wb,name="worldBank")
]