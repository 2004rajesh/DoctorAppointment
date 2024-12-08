from django.shortcuts import render,redirect
from .models import Userdata,Doctor,Patient
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def login(request,method=['GET','POST']):
    if request.method=='POST':
        email=request.POST.get('email')
        password1=request.POST.get('password1')

        users = Userdata.objects.filter(email=email,password=password1)
        if users.exists():
            request.session['email']=email
            return redirect('/main/')
    return render(request,'login.html')

def signup(request,method=['GET','POST']):
    if request.method == 'POST':
        email=request.POST.get('email')
        password1=request.POST.get('password1') 
        password2=request.POST.get('password2')

        user=Userdata.objects.filter(email=email)

        if user.exists():
            messages.info(request,'User is already exits')
        elif password1 != password2 :
            messages.info(request,'Passwords does not match')
        else:
            Userdata.objects.create(email=email,password=password1)
            return render(request,'login.html')
       # print(email,password1,password2)
    return render(request,'signup.html')

def main(request):
    email=request.session['email']
    doctor=Doctor.objects.all()
    return render(request,'main.html',{'doctor':doctor,'email':email})

def register(request,id,method=['GET','POST']):
    email=request.session['email']
    doctor=Doctor.objects.get(id=id)
    return render(request,'register.html',{'doctor':doctor,'email':email})
 
def appoint(request):
    email=request.session['email']
    users=Userdata.objects.get(email=email)
    if request.method == 'POST':
        doctor=request.POST.get('doctor')
        doc=Doctor.objects.get(doctor_name=doctor)
        name=request.POST.get('name') 
        age=request.POST.get('age')
        gender=request.POST.get('gender')       
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        date=request.POST.get('date')
        description=request.POST.get('description')
        
        user = Patient.objects.filter(email=email)
        date_exists = Patient.objects.filter(date=date, email=email)
        if user.exists():
            if date_exists.exists():
                messages.info(request,"You already Appointed on this date...")
            else:
                Patient.objects.create(user=users,doctorinfo=doc,name=name,age=age,gender=gender,email=email,phoneno=phoneno,date=date,description=description)
                return redirect('success')
        else:
            Patient.objects.create(user=users,doctorinfo=doc,name=name,age=age,gender=gender,email=email,phoneno=phoneno,date=date,description=description)
            return redirect('success')
   

def success(request):
    return render(request,'success.html')