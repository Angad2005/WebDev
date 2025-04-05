from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            return redirect('home')  # Redirect to homepage
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, "Login successful!")  
#             return redirect('page1')  # Redirect to dashboard
#         else:
#             messages.error(request, "Invalid username or password")  # Show error message

    # else:
    #     form = AuthenticationForm()

    # return render(request, 'registration/login.html', {'form': form})  # Ensure messages persist

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') # Replace 'page1' with your success URL
            else:
                # Handle login failure here (e.g., add an error message to the form)
                form.add_error(None, "Invalid username or password") # Or, form.errors['__all__'] = "..."
                return render(request, 'registration/login.html', {'form': form}) # Re-render login form with error
        else:
          return render(request, 'registration/login.html', {'form': form}) # Re-render with form errors.
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})