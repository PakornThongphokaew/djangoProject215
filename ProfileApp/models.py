from django.db import models
class Product(models.Model):
    id = models.CharField(max_length=6, default='', primary_key=True)
    name = models.CharField(max_length=50, default='')
    brand = models.CharField(max_length=50, default='')
    amount = models.CharField(max_length=50, default='')
    type = models.CharField(max_length=50, default='')
    age = models.CharField(max_length=50, default='')
    weight = models.CharField(max_length=50, default='')

    def sName(self):
        if self.name == 'dry cat food':
            sName = 599
        elif self.name == 'wet cat food':
            sName = 799
        elif self.name == 'kitten':
            sName = 399
        elif self.name == '1 year or more':
            sName = 199
        else:
            sName = 299
        return sName

    def sBrand(self):
        if self.brand == 'Purina One':
            sBrand = 100
        elif self.brand == 'Proplan':
            sBrand = 200
        elif self.brand == 'Royal Canin Skin Hairball':
            sBrand = 100
        elif self.brand == 'Kaniva':
            sBrand = 100
        else:
            sBrand = 100
        return sBrand

    def sAmount(self):
        if self.amount == '1':
            sAmount = 0
        elif self.amount == '2':
            sAmount = 0
        elif self.amount == '3':
            sAmount = 0
        elif self.amount == '4':
            sAmount = 0
        else:
            sAmount = 0
        return sAmount

    def sType(self):
        if self.type == 'successfully cooked':
            sType = 99
        elif self.type == 'fish fillets':
            sType = 89
        elif self.type == 'Boiled Chicken Breast':
            sType = 79
        else:
            sType = 59
        return sType

    def sAge(self):
        if self.age == '1':
            sAge = 120
        elif self.age == '2':
            sAge = 130
        elif self.age == '3':
            sAge = 140
        else:
            sAge = 150
        return sAge

    def sWegiht(self):
        if self.weight == '1':
            sWegiht = 200
        elif self.weight == '2':
            sWegiht = 210
        elif self.weight == '5':
            sWegiht = 220
        else:
            sWegiht = 230
        return sWegiht

    def sSum(self):
        sSum = self.sName()+self.sBrand()+self.sAmount()+self.sType()+self.sAge()+self.sWegiht()
        return sSum

    def sDiscount(self):
        if self.sSum() <300:
            sDiscount = self.sSum()*3/100
        elif self.sSum() < 500:
            sDiscount = self.sSum() * 5 / 100
        else:
            sDiscount = self.sSum() * 10 / 100
        return sDiscount

    def sTotal(self):
        sTotal = self.sSum()-self.sDiscount()
        return sTotal