from django.shortcuts import render

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



