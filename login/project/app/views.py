from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        # email=request.POST['email']
        email=request.POST.get('email')
        # password=request.POST['password']
        password=request.POST.get('password')
        data1=request.session.get('data')
        print(data1)
        print(data1["name"],data1["email"],data1["contact"],data1["password"])
        if data1['email']==email:
            if data1['password']==password:
                my_data={
                    'nm':data1['name'],
                    'em':data1['email'],
                    'con':data1['contact'],
                    'pas':data1['password']
                }
                return render(request,'dashboard.html',my_data)
            else:
                msg="Password is incorrect"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email is incorrect"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')


    # Try
    # if request.method=='POST':
    #     email=request.POST['email']
    #     password=request.POST['password']
    #     data1=request.session['data']
    #     print(data1["name"],data1["email"],data1["contact"],data1["password"])
    #     # name1=request.session['name']
    #     email1=request.session['email']
    #     password1=request.session['password']
    #     # contact1=request.session['contact']
    #     if email==email1:
    #         if password==password1:
    #             return render(request,'dashboard.html')
    #         else:
    #             msg="Email and Password not matching"
    #             return render(request,'login.html',{'msg':msg})
    #     else:
    #         msg="Email not Registered"    
    #         return render(request,'login.html',{'msg':msg})    
    
        
    # else:
    #     return render(request,'login.html') 
    # I tried
    # 
    #    
    # if request.method=='POST':
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')
    #     name1=request.COOKIES['name']
    #     contact1=request.COOKIES['contact']
    #     email1=request.COOKIES['email']
    #     password1=request.COOKIES['password']
    #     print(name1,contact1,email,password1)
    #     if email==email1:
    #         if password==password1:
    #             data={
    #             'name':name1,
    #             'email':email1,
    #             'contact':contact1,
    #             'pass':password1
    #             }
    #             return render(request,'dashboard.html',data)
    #         else:
    #             msg='Email and Password not matched'
    #             return render(request,'login.html',{'msg':msg})
    #     else:
    #         msg="Email not Registered"    
    #         return render(request,'login.html',{'msg':msg})
    # else:
    #     msg="Welcome to Login page"
    #     return render(request,'login.html',{'msg':msg})


def rdata(request):
    if request.method=='POST':
        name=request.POST.get('nm')
        contact=request.POST.get('con')
        email=request.POST.get('em')
        password=request.POST.get('pass')
        data={'name':name,
              'email':email,
              'contact':contact,
              'password':password}
        request.session['data']=data
        return render(request,'login.html')
    else:
        return render(request,'register.html')


    # print(request.method)
    # print(request.POST)
    # cstoken = request.POST.get('csrfmiddlewaretoken')
    # name = request.POST.get('nm')
    # contact = request.POST.get('con')
    # email = request.POST.get('em')
    # password = request.POST.get('pass')
    # print(cstoken)
    # print(name)
    # print(contact)
    # print(email)
    # print(password)
    # response = render(request,'login.html')
    # response.set_cookie('name',name)
    # response.set_cookie('contact',contact)
    # response.set_cookie('email',email)
    # response.set_cookie('password',password)
    # return response
# def userlogin(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)
