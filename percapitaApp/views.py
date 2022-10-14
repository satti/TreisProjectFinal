#from turtle import home
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from percapitaApp.models import itemPurchase
from treisApp.views import homeView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def purchaseView(request):
    if request.method == 'POST':
        #value = request.POST['item1']
        #print(value)
        repr = request.POST['iter']
        for i in range (1,int(repr)):
            #print(value,"i value is:",i)
            user = User.objects.get(id=request.user.id)
            item = request.POST.get('item'+str(i))
            qty = request.POST.get('qty'+str(i))
            price = request.POST.get('price'+str(i))
            invno = request.POST.get('bill'+str(i))
            invdate = request.POST.get('date'+str(i))
            itemPurchase.objects.create(user=user,item=item,quantity=qty,price=price,ino=invno,dop=invdate)
        return redirect(homeView)
    else:
        return render(request,'purchase.html',{})


@login_required
def purchaseItemsInfo(request):
    items = itemPurchase.objects.filter(user_id=request.user.id)
    return render(request,'purchaseitemsinfo.html',{'items':items})