from django.shortcuts import render

# Create your views here.

def about(resquest):
    return render(resquest, 'about.html')

def contact(resquest):
    return render(resquest, 'contact.html')