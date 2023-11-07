from django.shortcuts import render,redirect
from django.http import HttpResponse

# view의 역활은 Spring에서 Controller와 같다.
# view에서 가져오거나 전달할 것 처리하고 url에서 매핑해준다. 이후에 html에서 템플릿 작성

# Create your views here.
def index(request):
    return render(request, 'index.html')
