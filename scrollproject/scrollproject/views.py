from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from django.views.generic import ListView

# def home(request):

#     numbers=range(0,1000)
#     print(numbers)

#     paginator=Paginator(numbers,50)
#     page_num=int(request.GET.get("page",1))
    
#     if page_num > paginator.num_pages:
#         raise Http404
    
#     numbers=paginator.page(page_num)    

#     context={
#         'numbers':numbers
#     }
#     return render(request,'home.html', context)

def home(request):
    numbers=range(0,1000)
    paginator=Paginator(numbers,25)

    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)

    context={
        'page_obj':page_obj
    }

    return render(request,'home.html',context)