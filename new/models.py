from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

profession = (
    ('Owner','Owner'),
    ('Dealer','Dealer'),
    ('Worker','Worker')

)
class Employees(models.Model):
    name = models.CharField(max_length=100)
    dp = models.ImageField(upload_to='pics')
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    role = models.CharField(choices=profession,default='Owner',max_length=50)

class Timeline(models.Model):
    year = models.IntegerField()
    tag = models.CharField(max_length=30)
    desc = models.CharField(max_length=400)

chemical_type = (
    ('Special_Ink','Special_Ink'),
    ('Screen_Chemicals','Screen_Chemicals'),
    ('other','other'),
)

class Product(models.Model):
    pname = models.CharField(max_length=100)
    ppic = models.ImageField(upload_to='pics')
    ptype = models.CharField(choices=chemical_type ,default='other',max_length=50)
    pdesc = models.CharField(max_length=1000)

other_type = (
    ('Biochromate_based_emusion','Biochromate_based_emusion'),
    ('diazo_based','diazo_based'),
    ('Pure_photopolymer','Pure_photopolymer'),
    ('-','-'),
)
class Product_other(models.Model):
    pname = models.CharField(max_length=100)
    ppic = models.ImageField(upload_to='pics')
    pdesc = models.CharField(max_length=1000)
    potype = models.CharField(choices=other_type ,default='-',max_length=50)


active = (
    (1,1),
    (0,0)
)
class Home(models.Model):
    pic = models.ImageField(upload_to='pics')
    tag = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    active = models.IntegerField(choices=active ,default=0)
