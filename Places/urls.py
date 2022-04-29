from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('contact/', views.contacts.as_view(), name='contact'),
    path('forts/', views.forts.as_view(), name='forts'),
    path('wildlife/', views.wildlife.as_view(), name='wildlife'),
    path('lake/', views.lake.as_view(), name='lake'),
    path('museum/', views.museum.as_view(), name='museum'),
    path('religiousplace/', views.religiousplace.as_view(), name='religiousplace'),
    path('others/', views.Others.as_view(), name='Others'),
    path('travelagency/', views.travelagency.as_view(), name='travelagency'),
    path('travelagent/<int:myid>', views.travelagencyview.as_view(), name='travelagencyview'),
    path('places/<int:myid>', views.placeview.as_view(), name='placeview'),
    path('places/addcomment/<int:myid>', views.addcomment.as_view(), name='addcomment'),
    path('jaipur/', views.jaipur.as_view(), name='jaipur'),
    path('udaipur/', views.udaipur.as_view(), name='udaipur'),
    path('jaisalmer/', views.jaisalmer.as_view(), name='jaisalmer'),
] 
