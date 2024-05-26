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
   # 202311190531 bank 메인페이지로 가기 위한 url 경로 양식(URL 패턴을 지정, 라우트 정의할 때, 필요)
   path('transaction/create/', views_banking.create_transaction, name='create_transaction'),
 
   # 202311190223 김용록 계좌연결2
   path('account/<int:account_id>/', views_banking.account_detail, name='account_detail'),



########################################################################################################################
   # 202405101717 김용록 RPA 메인페이지로 가기 위한 url 경로 양식(path는 브라우저에 뜨는 url)
   path('hospital/main/', views_hospital.hospital_main, name='hospital_main'),

   #  202405151955 김용록 바코드 실시간 출력 
   path('barcode_data/', views_hospital.barcode_data, name='barcode_data'),

   # 202405150317 김용록 바코드를 위한 웹캠 연결
   path('video_feed/', views_hospital.video_feed, name='video_feed')
] 