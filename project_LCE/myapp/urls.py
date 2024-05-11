from django.contrib import admin
from django.urls import path, include

# 202405112255 김용록 views 분할 
from .import views_hospital
from .import views_banking


########################################################################################################################
# 2306161647 김용록 MVT 패턴을 위해 urls.py 파일 추가. 매핑.

urlpatterns = [
   path('',views_banking.index,name="Home"),
      # 처음 실행시 views에 index로 가게 설정
      
   #path('signup/',views.signup,name="signup"),
   #path('',views.handlesignup,name="creation"),

   path('handlesignup',views_banking.index),
      # views에 index와 매핑


########################################################################################################################
   # 202311190531 bank 메인페이지로 가기 위한 url 경로 양식
   path('transaction/create/', views_banking.create_transaction, name='create_transaction'),
 
   # 202311190223 김용록 계좌연결2
   path('account/<int:account_id>/', views_banking.account_detail, name='account_detail'),



########################################################################################################################
   # 202405101717 RPA 메인페이지로 가기 위한 url 경로 양식
   path('transaction/create/', views_hospital.hospital_main, name='hospital_main'),

] 

