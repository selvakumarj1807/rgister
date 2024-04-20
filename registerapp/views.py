from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserProfile


# Create your views here.
def home(request):
    return render(request,"index.html")

def registerpage(request):
    return render(request,"regiter.html")

# user_management/views.py

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'regiter.html', {'form': form})

def registration_success(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, "logi.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = UserProfile.objects.get(username=username, password=password)
            return redirect('user_dashboard', username=username)
        except UserProfile.DoesNotExist:
            error_message = 'Invalid username or password'
            return render(request, 'logi.html', {'error_message': error_message})
    
    return render(request, 'logi.html')

def user_dashboard(request, username):
    return render(request, 'user_dashboard.html', {'username': username})