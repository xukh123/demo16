from django.shortcuts import render
from django.http import HttpResponse
from apps.home.models import *

def index(request):
    navigations=Navigation.objects.all()
    categories=Category.objects.all()
    for category in categories:
        categories.subs=category.submenu_set.all()
        for sub in category.subs:
            sub.subs2=sub.submenu2_set.all()
    banners=Banner.objects.all()
    return render(request,'index.html',{'navigations':navigations,'banners':banners})

# Create your views here.
