from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def account_view(request):
    context = {}
    if request.method == 'POST' and 'register' in request.POST:
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        password = request.POST['password']

        try:
            # Creates a user account
            user = User.objects.create_user(username=username, email=email, password=password)

            # Creates a customer account
            Customer.objects.create(
                name=username,
                email=email,
                mobile=mobile,
                address=address,
                user=user
            )

            # Account created successfully
            messages.success(request, 'Account created successfully!')
            context['login'] = True
        
        except Exception as e:
            error_message = str(e).split('DETAIL:')[1].strip()
            messages.error(request, error_message)
    
    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'account.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')
