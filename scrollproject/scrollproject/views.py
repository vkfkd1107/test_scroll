from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

def home(request):
    numbers=[]
    for i in range(0,1000):
        numbers.append(i)
    print(numbers)
    context={
        'numbers':numbers
    }
    return render(request,'home.html')