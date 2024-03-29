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

   # 202311190223 김용록 계좌연결2
   path('account/<int:account_id>/', views.account_detail, name='account_detail'),

   # 202311190531 김용록 양식
   path('transaction/create/', views.create_transaction, name='create_transaction'),
 

] 

