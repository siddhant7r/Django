from app import views
from django .urls import path
urlpatterns=[

    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    # path('first',views.first,name='first'),
    # path('last',views.last,name='last'),
    # path('earliest',views.earliest,name='earliest'),
    path('all_details',views.all_details,name='all_details'),
    path('filter',views.filter,name='filter'),



]