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

# def userlogin(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')

def login(request):
    if request.method=='POST':
        print("hello")
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        #print(name,contact)
        name1=request.COOKIES['name']
        email1=request.COOKIES['email']
        contact1=request.COOKIES['contact']
        password1=request.COOKIES['password']
        print(name1,email1,contact1,password1)
        if name1==name:
            if contact1==contact:
                data={
                    'n1':name1,
                    'n2':email1,
                    'n3':contact1,
                    'n4':password1,
                }
                return render(request,'dashboard.html',data)        
            else:
                msg='Contact and Name not matched'
                return render('request','login.html',{msg:msg})        
        else:
            pass
    else:
        return render(request,'login.html')            
