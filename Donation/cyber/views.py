from django.shortcuts import render
from django.contrib import messages
from user.models import Usermodel
from donor.models import donormodel, OurAchivements

def index(request):
    return render(request, "index.html")

def Home(request):
    return index(request)

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginaction(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['upasswd']
        if uname == 'admin' and passwd == 'admin':
            data = Usermodel.objects.all()
            return render(request, "admin/adminhome.html", {'data': data})
        else:
            messages.success(request, 'Incorrect Details')
            return render(request, "admin/adminlogin.html")
    return render(request, "admin/adminlogin.html")

def showusers(request):
    data = Usermodel.objects.all()
    return render(request, "admin/adminhome.html", {'data': data})

def showdonors(request):
    data = donormodel.objects.all()
    return render(request, "admin/showdonors.html", {'data': data})

def AdminActiveUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        Usermodel.objects.filter(id=id).update(status=status)
        data = Usermodel.objects.all()
        return render(request, "admin/adminhome.html", {'data': data})
    
def AdminActivedonors(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        donormodel.objects.filter(id=id).update(status=status)
        data = Usermodel.objects.all()
        return render(request, "admin/showdonors.html", {'data': data})

def logout(request):
    return render(request, "admin/adminlogin.html")

def OurAchivement(request):
    our_achivements = OurAchivements.objects.all()
    return render(request, "OurAchivements.html", {'our_achivements': our_achivements})

def uploadachivepage(request):
    return render(request, "admin/uploadachivepage.html")

def updateachivement(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        file = request.FILES['file']
        achivement = OurAchivements(description=description, file=file)
        achivement.save()
        messages.success(request, 'Updated Successfully')
        return render(request, "admin/uploadachivepage.html")
    else:
        messages.success(request, 'Updated Successfully')
        return render(request, "admin/uploadachivepage.html")
