from django.shortcuts import render, redirect

from ProfileApp.forms import ProductForm
from ProfileApp.models import Product

def edcation(request):
    return render(request, 'education.html')

def pinterest(request):
    return render(request, 'pinterest.html')

def profile(request):
    return render(request, 'profile.html')

def idol(request):
    return render(request, 'idol.html')

def product(request):
    return render(request, 'product.html')

def showmydata(request):
    name = "Pakorn"
    sername = "Thobgphokaew"
    nickname = "fork"
    weight = "65"
    height = "174"
    gender = "man"
    education = "Bachelor's degree"
    status = "sod"
    work = "unemployed"
    old = '20'
    products =[
        ['CHIEF001', 'static/images/omoto01.jpg','OMOTOGreen','2700$'],
        ['CHIEF002', 'static/images/omoto02.jpg', 'OMOTOBlue','2800$'],
        ['CHIEF003', 'static/images/omoto03.jpg', 'OMOTORaed', '2900$'],
        ['CHIEF004', 'static/images/omoto04.jpg', 'OMOTOSilver', '3000$'],
        ['CHIEF005', 'static/images/omoto05.jpg', 'OMOTOPurple', '3100$'],
        ['Rein005', 'static/images/mastas05.jpg', 'Mustadog', '399$'],
        ['Rein TOURNAMENT006', 'static/images/mastas06.jpg', 'Mustadoc', '399$'],
        ['Power Up007', 'static/images/mastas07.jpg', 'Okumaov', '299$'],
        ['Power Up008', 'static/images/mastas08.jpg', 'Okumaoz', '299$'],
        ['Dava009', 'static/images/mastas09.jpg', 'Justrow', '189$'],
    ]
    context = {'name':name, 'sername':sername,'nickname':nickname,'weight':weight,
               'height':height, 'gender':gender,'education':education,'status':status,'work':work,'old':old,'product':products}
    return render(request,'showmydata.html',context)

lstOurProduct = []

def listProduct(request):
    context = {'product':lstOurProduct}
    return render(request, 'listProduct.html',context)

def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            brand = form.get('brand')
            amount = form.get('amount')
            type = form.get('type')
            age = form.get('age')
            weight = form.get('weight')

            if name == 'dry cat food':
                sName = 599
            elif name == 'wet cat food':
                sName = 799
            elif name == 'kitten food':
                sName = 399
            elif name == '1 year or more':
                sName = 199
            else:
                sName = 299

            if brand == 'Purina One':
                sBrand = 100
            elif brand == 'Proplan':
                sBrand = 200
            elif brand == 'Royal Canin Skin Hairball':
                sBrand = 100
            elif brand == 'Kaniva':
                sBrand = 100
            else:
                sBrand = 300

            if amount == '1':
                sAmount = 0
            elif amount == '2':
                sAmount = 0
            elif amount == '3':
                sAmount = 0
            elif amount == '4':
                sAmount = 0
            else:
                sAmount = 0

            if type == 'successfully cooked':
                sType = 99
            elif type == 'fish fillets':
                sType = 89
            elif type == 'Boiled Chicken Breast':
                sType = 79
            else:
                sType = 59

            if age == '1':
                sAge = 120
            elif age == '2':
                sAge = 130
            elif age == '3':
                sAge = 140
            else:
                sAge = 150

            if weight == '1':
                sWeight = 210
            elif weight == '2':
                sWeight = 220
            elif weight == '5':
                sWeight = 230
            else:
                sWeight = 240

            sSum = sName + sBrand + sAmount + sType + sAge + sWeight

            if sSum < 300:
                sDiscount = sSum * 3 / 100
            elif sSum < 500:
                sDiscount = sSum * 5 / 100
            else:
                sDiscount = sSum * 10 / 100

            sTotal = sSum - sDiscount

            ProductList = Product(id, name, brand, amount, type, age, weight)
            lstOurProduct.append(ProductList)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form': form}
        return render(request, 'inputProduct.html', context)