from django.shortcuts import render

# Create your views here.
def siddhant(request):
    return render(request,'home.html')

def register(request):
    print(request.method)
    print(request.POST)
    # return render(request,'register.html')

    cstoken=request.POST.get('csrfmiddlewaretoken')
    name=request.POST.get('nm')
    email=request.POST.get('em')
    contact=request.POST.get('con')
    password=request.POST.get('pass')

    # print(name,email,contact,password)
    response=render(request,'login.html')
    response.set_cookie('name',name)
    response.set_cookie('email',email)
    response.set_cookie('contact',contact)
    response.set_cookie('password',password)
    return response

def userlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
