from django.shortcuts import render
from .models import Student

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
