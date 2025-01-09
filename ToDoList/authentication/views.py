from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def login_view(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            if (request.user.is_superuser):
                return redirect('auth:approval')
            else:
                return redirect('ToDoList:home')
        try:
            # Check if the username exists and the account is inactive
            if not User.objects.get(username=username).is_active:
                messages.error(request, "Your account is inactive. Please wait for admin approval.")
            else:
                messages.error(request, "Invalid username or password.")
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('auth:login')

def user_signup(request):
    return render(request, 'register.html')

def user_register(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if (User.objects.filter(email = email).exists() or User.objects.filter(username = username).exists()):
            messages.error(request,'Oops looks like Email or Username already exist..')
            return redirect('auth:register')
        
        if (password!=confirm_password):
            messages.error(request,"Oops please make sure both passwords are same")
            return redirect('auth:register')
        
        user = User.objects.create_user(username = username, email = email, password = password, is_active = False)
        user.save()

    return redirect('auth:login')

def user_approval(request):
    users = User.objects.all().exclude(is_superuser=True).values('id', 'username', 'email', 'is_active').order_by('is_active')
    data = list(users)
    return render(request,'approval.html',{'data' : data})

# def user_approval_update(request):
#     if (request.method == "POST"):
#         id = request.POST.get('id')
#         activity = request.POST.get('activity')

#         # print(id,activity)
#         users = User.objects.get(id=id)
#         print(list(users)) #something wrong
#     return redirect('auth:approval')
def user_approval_update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        activity = request.POST.get('activity1')
        print(request.POST.get)
        if activity == 'Active':
            activity = True
        else:
            activity = False
        # print(activity)

        # Ensure the id is valid
        try:
            user = User.objects.get(id=id)
            user.is_active = activity
            user.save()
            # print(user.username)  # Prints the username of the user
            # print(user.email)  # Prints the email of the user
            # Any other attributes you need
        except User.DoesNotExist:
            print("User with the given ID does not exist.")

    return redirect('auth:approval')