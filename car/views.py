from django.shortcuts import render
from . models import Cars,Orders,Contact
from math import *

# Create your views here.

def home(request):
    allcars = []
    catcars = Cars.objects.values('category', 'car_id')
    cats = {item['category'] for item in catcars}
    for cat in cats:
        prod = Cars.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 3 + ceil((n / 3) - (n // 3))
        allcars.append([prod, range(1, nslides), nslides])
        params = {'allprods': allcars}


    return render(request,'home.html',params)

def checkout(request):
    if request.method == "POST":
        name = request.POST['name']
        items_json = request.POST['itemsJson']
        email = request.POST['email']
        address = request.POST['address1'] + "----" + request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        mobile = request.POST['mobile']
        order = Orders(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,mobile=mobile,items_json=items_json)
        order.save()
        thank = True
        return render(request,'checkout.html',{'thank':thank})

    return render(request,'checkout.html')

def about(request):
    return render(request,'about.html')


def contact(request):
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            desc = request.POST['desc']
            print(name, email, phone, desc)
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            thanks = True
            return render(request, 'contact.html', {'thanks': thanks})

        return render(request, 'contact.html')
