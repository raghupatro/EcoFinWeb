from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path('wb/<slug:country>/<slug:indicator>',views.wb,name="worldBank")
]