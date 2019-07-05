from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from UserRbs.forms import RoleDetailsForm
from UserRbs.models import RoleDetails, UserRole
from MiscFiles.genric_functions import generic_string, link_send


def signIn(request):
    return render(request, "signin.html")


def register(request):
    data = UserRole.objects.all()
    if request.method == "POST":
        string = generic_string()
        password = string
        link = make_password(password)
        link = link.replace("+", "")
        form = RoleDetailsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.role_id = request.POST['role']
            f.name = request.POST['name']
            f.email = request.POST['email']
            f.gender = request.POST['gender']
            f.active = 0
            f.password = make_password(link)
            f.verify_link = link
            f.save()
            f_link = "127.0.0.1:8000/verify_link/?link=" + link
            request.session['email'] = f.email
            link_send(f.email, f_link, password)
            return render(request, "registration.html", {'confirm':True})
    return render(request, "registration.html", {'data': data})


def verify_link(request):
    get_link = request.GET['link']
    session_mail = request.session['email']
    data = RoleDetails.objects.get(email=session_mail)
    db_verify = data.verify_link
    if get_link == db_verify:
        update = RoleDetails(email=session_mail, active=1, verify_link="")
        update.save(update_fields=['active','verify_link'])
        return render(request,"updatePassword.html")


def login(request):
    if request.method == "POST":
        get_email = request.POST["email"]
        get_password = request.POST["password"]
        try:
            data = RoleDetails.objects.get(email=get_email)
            db_password = data.password
            db_active = data.active
            db_verify = data.verify_link
            if db_active == 0 and db_verify == "0":
                string = generic_string()
                f_link = make_password(string)
                link = "http://127.0.0.1:8000/verify_link/?link="+f_link
                update = RoleDetails(email=get_email, verify_link=f_link)
                update.save(update_fields=["verify_link"])
                request.session['email']=get_email
                # link_send(get_email, link)
            elif db_active == "0" and db_verify != "":
                pass
        except:
            return HttpResponse("<h1>Email not valid</h1>")
    return render(request, "signin.html")


