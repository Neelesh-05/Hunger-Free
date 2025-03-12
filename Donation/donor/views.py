from django.shortcuts import render
from donor.models import donormodel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from donor.models import donorModels, Acceptmodel
from user.models import requestdonorModels, Usermodel

# Create your views here.
def donorlogin(request):
    return render(request, "donor/donorlogin.html")

def donorregister(request):
    return render(request, "donor/donorregister.html")

def donorloginaction(request):
    if request.method == 'POST':
        sname = request.POST.get('email')
        spasswd = request.POST.get('upasswd')
        try:
            check = donormodel.objects.get(email=sname, password=spasswd)
            status = check.status
            if status == 'activated':
                request.session['email'] = check.email
                return render(request, "donor/donorhome.html")
            else:
                messages.error(request, 'Login Unsuccessful')
                return render(request, "donor/donorlogin.html")
        except:
            messages.error(request, 'Login Unsuccessful')
            return render(request, "donor/donorlogin.html")
    else:
        messages.error(request, 'Login Unsuccessful')
        return render(request, "donor/donorlogin.html") 

def donorregisterAction(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upasswd')
        phoneno = request.POST.get('uphonenumber')
        form1 = donormodel(name=name, email=email, password=password, phoneno=phoneno, status='waiting')
        form1.save()
        messages.success(request, 'Registration Successful')
        return render(request, "donor/donorlogin.html")
    else:
        messages.error(request, 'Registration Unsuccessful')
        return render(request, "donor/donorregister.html")
    
def logout(request):
    return render(request, "donor/donorlogin.html")

def uploaddonations(request):
    return render(request, "donor/uploaddonations.html")

def uploaddonation(request):
    if request.method=='POST':
        cropname = request.POST.get('cropname')
        price = request.POST.get('price')
        description = request.POST.get('description')
        location = request.POST.get('location')
        image_file = request.FILES['file']
                # let's check if it is a csv file
        if not image_file.name.endswith('.jpg'):
            messages.error(request, 'THIS IS NOT A JPG  FILE')
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        detect_filename = fs.save(image_file.name, image_file)
        uploaded_file_url = fs.url(filename)
        
        email = request.session['email']
        donorModels.objects.create(selleremail=email, cropname=cropname,price=price, description=description,file=uploaded_file_url,status='waiting', location=location)
        messages.success(request, 'Donation Addedd Success')
        return render(request, 'donor/uploaddonations.html', {})
    else:
        return render(request, "donor/uploaddonations.html")
    
def donordonation(request):
    loginid = request.session['email']
    data = donorModels.objects.filter(selleremail=loginid)
    return render(request, 'donor/donordonation.html',{'data':data})

def donorrequestesfood(request):
    data = requestdonorModels.objects.all()
    return render(request, 'donor/donorrequestesfood.html',{'data':data})

def acceptrequestesfood(request):
    session_email = request.session.get('email')
    data = Acceptmodel.objects.filter(associated_email=session_email)
    user_data = Usermodel.objects.filter(email=session_email)
    return render(request, 'donor/acceptrequestesfood.html', {'data': data, 'user_data': user_data})
