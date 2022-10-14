from .import views
from django.urls import path

app_name = 'percapitaApp'
urlpatterns = [
    path('percapita/',views.purchaseView,name='percapita'),
    path('itemsinserted/',views.purchaseItemsInfo,name='itemsinfo'),
]