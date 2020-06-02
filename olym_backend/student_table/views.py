from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.core.mail import send_mail
from passlib.hash import pbkdf2_sha256

def login(request):
    pass


def st_table(request):
    if(request.method=='POST'):
        ref_code = request.POST['ref_code']
        name=request.POST['name']
        parent_name = request.POST['parent_name']
        dob = request.POST['dob']
        country =request.POST['country']
        address = request.POST['address']
        school=request.POST['school']
        school_state = request.POST['school_state']
        school_address=request.POST['school_address']
        school_city=request.POST['school_city']
        pincode = request.POST['pincode']
        number=request.POST['number']
        email = request.POST['email']
        password =request.POST['password']

        standard = request.POST['standard']
        enc_password = pbkdf2_sha256.encrypt(password, rounds=8000, salt_size=10)
        if(Student.objects.filter(email=email).exists()):
            messages.warning(request,"Email already exist")
        else:
            context=Student(ref_code = ref_code ,name=name,parent_name = parent_name,dob = dob,country= country,address= address,school=school,school_state= school_state,school_address= school_address,school_city= school_city,pincode=pincode,number=number,email=email,standard= standard,password= enc_password)
            context.save()
            messages.success(request,"Student Registered successfully")
            # user.is_active=False
            # user.save()




    return render(request,'home.html')


# Create your views here.
