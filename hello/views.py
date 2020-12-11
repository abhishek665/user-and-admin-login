from django.shortcuts import render, redirect
from .forms import*
from .models import*
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'hello/index.html')


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        reg_form = RegForm(data=request.POST)
        if user_form.is_valid() and reg_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            reg = reg_form.save(commit=False)
            reg.save()
            registered = True
        else:
            print("tryAgain", user_form.errors, reg_form.errors)
    else:
        user_form = UserForm()
        reg_form = RegForm()
    return render(request, 'hello/registration.html',
                  {'user_form': user_form,
                   'reg_form': reg_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:

            if user.is_active:
                login(request, user)
                user.save()
                return redirect("hello:index")
            else:
                return HttpResponse('account not active')
        else:
            print("Login Failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login")
    else:
        return render(request, 'hello/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return redirect("hello:index")


def delete_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        num = request.POST.get('num')
        account = authenticate(username=username, password=password)
        if account:
            if account.is_active:
                login(request, account)
                account.delete()
                print("Account Deleted!")
                return redirect("hello:index")  #edirect(reverse('index'))
            else:
                return HttpResponse('account not active')
        else:
            print("Deletion Failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid Details!")
    else:
        return render(request, 'hello/delete.html', {})


def show_db(request):
    obj = Registration.objects.all()
    return render(request, "hello/index.html", {'obj': obj})


def delete_db(request):
    model = Registration.objects.filter()
    model.delete()
    return render(request, 'hello/base.html', {'model': model})


def edit_account(request, id):
    uni = Registration.objects.get(id=id)
    form = EditForm(request.POST, instance=uni)

    if form.is_valid():
        form.save()
        return show_db(request)
    else:
        print("error")
    return render(request, 'hello/index.html', {'form': form, 'uni': uni})

