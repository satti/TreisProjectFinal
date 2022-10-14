from django.contrib import admin
from percapitaApp.models import itemPurchase

# Register your models here.

class itemPurchaseAdmin(admin.ModelAdmin):
    model: itemPurchase
    list_display = ('item','quantity',)

admin.site.register(itemPurchase,itemPurchaseAdmin)
