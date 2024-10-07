from django.shortcuts import render
from .models import Student
from .models import Query

# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        # print(request.POST)
        name=request.POST.get('nm')
        email=request.POST.get('em')
        contact=request.POST.get('con')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')

        if password==cpassword:
            user=Student.objects.filter(stu_email=email)
            if user:
                msg="Email already exist"
                return render (request,'login.html',{'msg':msg})
            else:
                Student.objects.create(
                stu_name=name,
                stu_email=email,            
                stu_contact=contact,
                stu_password=password,
                )
            msg="Registration successfull"
            return render(request,"home.html",{'msg':msg})
        else:
            msg="Password is not matching"
            return render(request,'register.html',{'msg':msg})    
    else:
        return render(request,"register.html") 

def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=Student.objects.filter(stu_email=email)
        if user:
            user_data=Student.objects.get(stu_email=email)
            print(user_data)
            email1=user_data.stu_email
            name1=user_data.stu_name
            contact1=user_data.stu_contact
            password1=user_data.stu_password
            print(name1,email1,contact1,password1)
            if password==password1:
                data={
                    'name':name1,
                    'email':email1,
                    'contact':contact1,
                    'password':password1
                }
                return render(request,'dashboard.html',{'data':data})   
            else:
                msg="Email & password not matched"
                return render(request,'login.html',{'msg':msg})
        else:
            msg="Email Not Registered"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'login.html')





def exclude(request):
    data=Student.objects.exclude(stu_name='Siddhant')
    print(data)
    return render (request, 'dashboard.html', {'data':data})

def query(request):
    if request.method=='POST':
        # print(request.POST)
        name1=request.POST.get('nm')
        email1=request.POST.get('em')
        query1=request.POST.get('query')

        Query.objects.create(stu_name=name1,stu_query=query1,stu_email=email1)

        data=Student.objects.get(stu_email=email1)

        data1={'name':data.stu_name,
               'email':data.stu_email,
               'contact':data.stu_contact,
               'password':data.stu_password}
        
        query_data=Query.objects.filter(stu_email=email1)
        return render(request,'dashboard.html',{'data':data1, 'query_data':query_data})
    

    






