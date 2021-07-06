
from django.shortcuts import render
from .models import Employees,Timeline,Product,Home,Product_other


def about(request):
    ab = Timeline.objects.all()
    return render(request, 'new/about.html', {'ab': ab})


def contact(request):
    return render(request, 'new/contact.html')


def index(request):
    hom = Home.objects.all()
    return render(request,  'new/index.html', {'hom': hom})


def portfolio(request):
    pro = Product.objects.all()
    return render(request, 'new/portfolio.html', {'pro': pro})


def team(request):
    emps = Employees.objects.all()
    return render(request,'new/team.html', {'emps': emps})

def view_product(request, myid):
    v = Product.objects.filter(id=myid)
    return render(request, 'new/view_product.html', {'v': v[0]})


def view_screen_chemicals(request):
    v = Product_other.objects.all()
    return render(request, 'new/view_screen_chemicals.html', {'v': v})

def view_other_product(request, myid):
    v = Product_other.objects.filter(id=myid)
    return render(request, 'new/view_other_product.html', {'v': v[0]})
