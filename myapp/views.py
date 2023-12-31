from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from .forms import TODOForm

from .models import TODO

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user)
        context = {'form':form, 'todos':todos}
        return render(request, 'myapp/home.html', context= context)

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'myapp/login.html', context=context)
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context = {'form':form}
            return render(request, 'myapp/login.html', context=context)



def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {"form" : form}
        return render(request, 'myapp/signup.html', context=context)
    else:
        form = UserCreationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            user =form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context=context)


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             loginUser(request, user)
#             return redirect('home')
#     else:
#         form = CustomUserCreationForm()

#     context = {'form': form}
#     return render(request, 'myapp/signup.html', context=context)


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, 'home.html', context={'form':form})
        

@login_required(login_url='login')
def delete_todo(request, id):
    todo = TODO.objects.get(pk=id)

    todo.delete()

    return redirect('home')


@login_required(login_url='login')
def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()

    return redirect('home')
        

def signout(request):
    logout(request)
    
    return redirect("login")
    