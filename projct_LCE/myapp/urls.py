from django.contrib import admin
from django.urls import path, include

# 2306161647 김용록 MVT 패턴을 위해 urls.py 파일 추가.
from .import views
urlpatterns = [
   path('',views.index,name="Home"),
   #path('signup/',views.signup,name="signup"),
   #path('',views.handlesignup,name="creation"),
   path('handlesignup',views.index),
]
