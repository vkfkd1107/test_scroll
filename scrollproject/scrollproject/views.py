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
    # 주석은 혼자 정리하려고 적어놓은거니 지우셔도 상관없습니다
    # 혹시 주석이나 코드에 잘못된 부분이 있으면 기재해주시거나 알려주시면 감사하겠습니다
    # 깃은 초대해드렸으니 진행 시 풀리퀘해주시면 됩니다

    # 버튼을 누를때마다 이 print문이 실행되는 것을 볼 수 있다
    # 즉, 버튼을 누를때마다 여기로 와서 '다음페이지를 가져와/이전 페이지를 가져와/...' 하는 요청이 여기로 들어오는 것 을 알 수 있음
    print('home')
    # 내가 보낼 정보(숫자)를 1000개까지 설정
    numbers=range(0,1000)

    # 내가 보낼 정보(숫자)를 25개씩 끊을 것이다
    paginator=Paginator(numbers,25)

    # 페이지숫자를 가져옴. 페이지숫자가 설정되있지 않다면 1로 설정
    # request를 통해 페이지 정보를 가져온다.
    # html파일의 ?뒤의 page는 내가 가져오는 정보의 이름. 
    # 그래서 내가 get요청으로 'page'라는 이름의 정보를 가져오는 것을 요청할 수 있다
    # ?page=뒤의 {{여기가 내가 가져오는 정보}}
    # 그래서 이 page_num변수는 내가 next를 누른다면 a태그의 href를 타고 page_obj.next_page_number을 가져올 수 있다
    # 즉, next버튼을 누르면 다음페이지숫자를 가져온다
    # 다른 first나 previous도 마찬가지로 작동한다
    # js로 구현한다면 무언가를 했을때 여기로 그 정보(page_obj.next_page_number)를 보내는 이벤트를 구현하면 될 것 같다
    page_num=request.GET.get('page',1)

    # page_obj : 템플릿에 보낼 아이템(예: 0~24 / 25~49)
    # 내가 설정한 보낼 정보들(paginator)과 받은 페이지 정보(page_num)로 최종적으로 보낼 아이템들이다
    page_obj=paginator.get_page(page_num)

    context={
        'page_obj':page_obj
    }

    return render(request,'home.html',context)