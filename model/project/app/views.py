from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request,'home.html')


def home(request):
    return render(request,"home.html")

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







# def first(request):
#     data=Student.objects.first()
#     data = Student.objects.order_by('stu_name').first()
#     print(data)
#     print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)
    
#     return HttpResponse (data)



# def last(request):
#     data=Student.objects.last()
#     print(data)
#     print(data.id,data.stu_name,data.stu_email,data.stu_contact,data.stu_password)

#     return HttpResponse(data)

# def earliest(request):
#     data0=Student.objects.earliest("stu_name")
#     print(data0.id,data0.stu_name,data0.stu_email)
#     return HttpResponse (data0)    



def all_details(request):
    data=Student.objects.all()
    print(data)
    print(data.values)
    return HttpResponse(data)

def filter(request):
    data=Student.objects.filter(stu_email='virat@mcg.com')
    print(data)
    return HttpResponse(data)









        # user=Student.objects.filter(stu_email=email)
        # user=Student.objects.get(stu_email=email)
        # print(user)
        # print(name,email,contact,password)

        # Model_name.objects.create(
        #     col_name=value,
        #     col_name=value,
        #     col_name=value,
        
        # Student.objects.create(
        #     stu_name=name,
        #     stu_email=email,
        #     stu_contact=contact,
        #     stu_password=password,
        #     )
        # msg="Registration successfull"
        # return render(request,"home.html",{'msg':msg})

        


     
          

# def register(request):
    

#     if request.method=='POST':
#         name=request.POST.get('name')
#         contact=request.POST.get('contact')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#     #     print(name,email,contact,password)
       
#     # else:
#     #     return render(request,'register.html')

#         Student.objects.create(stu_name=name,
#                            stu_email=email,
#                            stu_password=password,
#                            stu_contact=contact)
#         msg=""
#         return render(request,'home.html')




