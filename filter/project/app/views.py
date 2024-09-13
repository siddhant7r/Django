from django.shortcuts import render

# Create your views here.
def myfilter(request):
    # return render(request,'filter.html',{'value':5})
    # return render(request,'filter.html',{'value':'siddhant'})
    data=[
    {'name':'Siddhant','age':28,'phone':'Realme'},
    {'name':'iddhant','age':28,'phone':'ealme'},
    {'name':'Shubham','age':25,'phone':'Samsung'}]
    return render(request,'filter.html',{'data':data})