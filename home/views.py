# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def add(request):
    a=0
    b=0
    c=0
    if request.POST:
        a=int(request.POST['t1'])
        b=int(request.POST['t2'])
        c=a+b
        print("sum=",c)
    return render(request,'formadd.html',{'vara':a,'varb':b,'res' : c})

def sub(request):
    a=0
    b=0
    c=0
    if request.POST:

        a=int(request.POST["t3"])
        b=int(request.POST["t4"])
        c=a-b
        print("diff=",c)
    return render(request,'formsub.html',{'vara':a,'varb':b,'res' : c})

def more(request):
    a=0
    b=0
    c=0
    if request.POST :

        a=int(request.POST["t3"])
        b=int(request.POST["t4"])
        if "add" in request.POST:
            c=a+b
        if "sub" in request.POST:
            c=a-b
        if "mul" in request.POST:
            c=a*b
        if "div" in request.POST:
            c=a/b
        
    return render(request,'more.html',{'vara':a,'varb':b,'res' : c})


def details(request):
    student={"Name":[],"Class":[],"Mark":{"Maths":[],"Graphics":[],"OS":[]}}
    if request.POST :
        sname=request.POST['name']
        sclass=request.POST['class']
        sgraphics=request.POST['graphics']
        sos=request.POST['os']
        smaths=request.POST['maths']
        student["Name"].append(sname)
        student["Class"].append(sclass)
        student["Mark"]["Maths"].append(sgraphics)
        student["Mark"]["Graphics"].append(sos)
        student["Mark"]["OS"].append(smaths)
    return render(request,'details.html',{"student":student})
