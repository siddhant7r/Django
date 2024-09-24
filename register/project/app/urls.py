from app import views
from django .urls import path
urlpatterns=[
    path('',views.siddhant,name='siddhant'),
    path('register/',views.register,name='register'),
    path('register/',views.register,name='register'),
    # path('userlogin/',views.userlogin,name='userlogin'),
    path('login/',views.login,name='login'),
]