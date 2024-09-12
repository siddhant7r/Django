from django.shortcuts import render

# Create your views here.
def myfilter(request):
    # return render(request,'filter.html',{'value':5})
    return render(request,'filter.html',{'value':'siddhant'})