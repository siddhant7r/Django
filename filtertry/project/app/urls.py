from django .urls import path
from app import views

urlpatterns=[
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('exclude/',views.exclude,name='exclude'),
    path('query',views.query,name='query'),

]