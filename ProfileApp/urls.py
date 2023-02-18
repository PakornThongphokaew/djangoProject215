from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edcation/', views.edcation, name='education'),
    path('idol/', views.idol, name='idol'),
    path('product/', views.product, name='product'),
    path('pinterest/', views.pinterest, name='pinterest'),
    path('showmydata/', views.showmydata, name='showmydata'),
    path('inputProduct/', views.inputProduct, name='inputProduct'),
    path('listProduct/', views.listProduct, name='listProduct')
]