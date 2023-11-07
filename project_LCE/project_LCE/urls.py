from django.contrib import admin
from django.urls import path, include

# 2306161647 김용록 MVT 패턴을 위해 urls.py 파일 추가. 매핑.
from .import views
urlpatterns = [
   path('',views.index,name="Home"),
      # 처음 실행시 views에 index로 가게 설정
      
   #path('signup/',views.signup,name="signup"),
   #path('',views.handlesignup,name="creation"),

   path('handlesignup',views.index),
      # views에 index와 매핑

   # 2311070903 김용록 다른 디렉토리(project_LCE)에 연결하기 위해 include 문 추가.
   path('',include('project_LCE.urls')),
]
