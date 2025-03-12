from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from user.models import Usermodel,requestdonorModels
from donor.models import donorModels, Acceptmodel

# Create your views here.
def Userlogin(request):
    return render(request, "user/Userlogin.html")

def userregister(request):
    return render(request, "user/userregister.html")

def userregisterAction(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upasswd')
        phoneno = request.POST.get('uphonenumber')
        form1 = Usermodel(name=name, email=email, password=password, phoneno=phoneno, status='waiting')
        form1.save()
        messages.success(request, 'Registration Successful')
        return render(request, "user/Userlogin.html")
    else:
        messages.error(request, 'Registration Unsuccessful')
        return render(request, "user/userregister.html")

def userloginaction(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        spasswd = request.POST.get('upasswd')
        try:
            check = Usermodel.objects.get(email=sname, password=spasswd)
            status = check.status
            if status == 'activated':
                request.session['email'] = check.email
                messages.success(request, 'Login Successful')
                return render(request, "user/userhome.html")
            else:
                messages.error(request, 'Login Unsuccessful')
                return render(request, "user/Userlogin.html")
        except:
            messages.error(request, 'Login Unsuccessful')
            return render(request, "user/Userlogin.html")
    else:
        messages.error(request, 'Login Unsuccessful')
        return render(request, "user/userhome.html")

def searchdonors(request):
    return render(request, "user/userhome.html")

def searchdonorslocation(request):
    if request.method=='POST':
        crpname = request.POST.get('cropname')
        search_data = donorModels.objects.filter(price__icontains=crpname)
        return render(request, "user/searchdonorslocation.html",{'data':search_data})

def usrlogout(request):
    return render(request, "user/userlogin.html")


def request1(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        session_email = request.session.get('email')

        associated_email_query = Acceptmodel.objects.filter(uid=uid).values('email').first()
        print(f"UID: {uid}, Associated Email Query: {associated_email_query}")

        associated_email = associated_email_query['email'] if associated_email_query else ''

        accept = Acceptmodel(uid=uid, email=session_email, associated_email=associated_email)
        accept.save()

        messages.success(request, f'Requested successful. Session Email: {session_email}, Associated Email: {associated_email}')
        return render(request, 'user/userhome.html')
    else:
        messages.error(request, 'Requested Un-successful')
        return render(request, 'user/userhome.html')


def Requestdonors(request):
    return render(request, "user/Requestdonors.html")

def requestdonation1(request):
    if request.method=='POST':
        cropname = request.POST.get('cropname')
        price = request.POST.get('price')
        date= request.POST.get('date')
        description = request.POST.get('description')
        email = request.session['email']
        requestdonorModels.objects.create(selleremail=email,date=date,cropname=cropname,price=price, description=description)
        messages.success(request, 'Request Addedd Success')
        return render(request, "user/Requestdonors.html")
    else:
        return render(request, "user/Requestdonors.html")    

