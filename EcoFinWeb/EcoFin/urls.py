from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('wb/<slug:country1>;<slug:country2>;<slug:country3>;<slug:country4>;<slug:country5>/<slug:indicator>',views.wb,name="worldBank")
]