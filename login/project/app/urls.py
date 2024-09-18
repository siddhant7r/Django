from app import views
from django .urls import path

urlpatterns= [
    path('',views.home, name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('rdata',views.rdata,name="rdata"),
    # path('userlogin/',views.userlogin,name='userlogin')
    

]