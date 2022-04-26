# -*- encoding: utf-8 -*-


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from apps.authentication.models import *
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
userr = get_user_model()
from apps.authentication.models import user
import razorpay
from .models import *



def index(request):
    return render(request, 'accounts/index.html')

def confirmation(request):
    return render(request, 'accounts/confirmation.html')

def course1(request):
    return render(request,'accounts/course-1.html')

def course2(request):
    return render(request,'accounts/course-2.html')

def course3(request):
    return render(request,'accounts/course-3.html')

def coursed(request):
    return render(request,'accounts/single-course.html')


def about(request):
    return render(request,'accounts/about-1.html')

def about2(request):
    return render(request,'accounts/about-2.html')

def instructor(request):
    return render(request,'accounts/instructor.html')

def instructorprofile(request):
    return render(request,'accounts/profile.html')

def blog(request):
    return render(request,'accounts/blog.html')

def blog2(request):
    return render(request,'accounts/single-post.html')

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser == False and user.is_staff == False:
                    login(request, user)
                    return redirect("/")

                elif user.is_superuser == False and user.is_staff == True:
                    login(request, user)
                    return redirect("/ins")

                elif user.is_superuser == True and user.is_staff == True:
                    login(request, user)
                    return redirect("/adm")

                else:
                    msg = "invalid"
                    return redirect('login/')


            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/contact.html", {"form": form, "msg": msg, "success": success})


def stuinquiry(request):
    if request.method == "POST":
        name = request.POST.get('inqname')
        email = request.POST.get('inqemail')
        if StudentInquiry.objects.filter(email=email).exists():
            messages.info(request,'Email is already exists')
            return redirect('/inquiry/')
        number = request.POST.get('inqnumber')
        mod = request.POST.get('inqmod')
        msg = request.POST.get('message')
        si = StudentInquiry(name=name,email=email,number=number,selectmodel=mod,message=msg)
        si.save()
        sub = 'Welcome to Student Course Portal'
        msg = '''Hi there!
                You have successfully submitted your enquiry please
                 complete your registration through given link ,
                 '''+ "\nRegistrationlink:"+ "http://127.0.0.1:8000//reg1/"
        EmailMessage(sub, msg, to=[email]).send()
        u = user.objects.filter(is_superuser=True)
        for i in u:
            sub = 'Welcome to Student Course Portal'
            msg = '''Hi there!
                                    New user Requested to you ,
                                    '''+ "\nName:" + " " + name + "\nEmail:" + " " + email + "\nNumber:" + " " + number + " " + "Select-Mod:" +  " " + mod
            EmailMessage(sub, msg, to=[i.email]).send()
        return redirect('/confirmation/')

    return redirect('/login/')





def reg11(request):
    return render(request,'accounts/reg1.html')

def Registerfill(request):
    if request.method == 'POST':
        fn = request.POST.get('rfname')
        ln = request.POST.get('lfname')
        birthday = request.POST.get('rbname')
        gendery = request.POST.get('rradio')
        email = request.POST.get('remail')
        phone = request.POST.get('rphone')
        aphone = request.POST.get('arphone')
        address = request.POST.get('praddress')
        state = request.POST.get('rstate')
        village = request.POST.get('rvillage')
        dist = request.POST.get('rdistrict')
        pin = request.POST.get('rpincode')
        city = request.POST.get('rcity')
        aadhar = request.POST.get('raadhar')
        active = request.POST.get('acradio')
        qualification = request.POST.get('rqalification')
        sscs = request.POST.get('sscs')
        sscpy = request.POST.get('sscpy')
        sscom = request.POST.get('sscom')
        sscg = request.POST.get('sscg')
        # rupdated = request.POST.get('rupdated')
        # rlstupon = request.POST.get('rlstupon')
        # rfee = request.POST.get('rfee')
        # rfeepaiddate = request.POST.get('rfeepaiddate')
        # rfeepaidamount = request.POST.get('rfeepaidamount')
        pp = user(fname=fn, laname=ln, birthday=birthday, gender=gendery, email=email, mobile=phone,
                  alternate_mobile=aphone, address1=address, state=state, village=village, district=dist,
                  pin=pin,
                  city=city, Aadhar=aadhar, qualification=qualification, school=sscs, passingyear=sscom,
                  marks=sscpy, grade=sscg,Active=active)
        pp.save()
    return redirect('/')



def rrhomee(request):

    amount = 500*100

    order_currency = 'INR'
    client = razorpay.Client(auth=('rzp_test_PgHNzZxAI49468','IU8ChpBVTn3Yf4k9dnHa6Elm'))
    payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'0'})
    return render(request,'accounts/payment.html',{'payment':payment})


def successs(request):
    return redirect('/regg11/')



