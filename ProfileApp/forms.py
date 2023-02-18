from django import forms
from ProfileApp.models import *

name_choice = [('dry cat food', 'dry cat food'),
               # แบบเม็ด
               ('wet cat food', 'wet cat food'),
               # แบบเปียก
               ('kitten food', 'kitten food'),
               # แมวเด็ก
               ('1 year or more', '1 year or more'),
               # แมวที่มีอายุ 1 ปีขึ้นไป
               ('7 year or more', '7 year or more')]
# แมวที่มีอายุ 1 ปีขึ้นไป

brand_choice = [('Purina One', 'Purina One'),
                ('Proplan', 'Proplan'),
                ('Royal Canin Skin Hairball', 'Royal Canin Skin Hairball'),
                ('Kaniva', 'Kaniva'),
                ('Me – O Gold Indoor', 'Me – O Gold Indoor')]

amount_choice = [('1', '1'),
                 ('2', '2'),
                 ('3', '3'),
                 ('4', '4'),
                 ('5', '5')]


type_choice = [('successfully cooked', 'successfully cooked'),
               # ปรุงสำเร็จ
               ('fish fillets', 'fish fillets'),
               # คลุกเนื้อปลา
               ('Boiled Chicken Breast', 'Boiled Chicken Breast'),
               # อกไก่ต้มคลุก
               ('cat licking snacks', 'cat licking snacks')]
# ขนมแมวเลีย

age_choice = [('1 year', '1 year'),
              ('2 year', '2 year'),
              ('3 year', '3 year'),
              ('7 year', '7 year')]

weight_choice = [('1 kg', '1 kg'),
                 ('2 kg', '2 kg'),
                 ('5 kg', '5 kg'),
                 ('7 kg', '7 kg')]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','name', 'brand', 'amount', 'type', 'age', 'weight')
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=name_choice),
            'brand': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=brand_choice),
            'amount': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=amount_choice),
            'type': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=type_choice),
            'age': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=age_choice),
            'weight': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=weight_choice),
        }
        labels = {
            'id': 'ID',
            'name': 'Name',
            'brand': 'Brand',
            'amount': 'Amount',
            'type': 'Type',
            'aeg': 'Aeg',
            'weight': 'Weight',
        }

