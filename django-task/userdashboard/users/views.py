from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, DoctorForm

def signup(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'patient':
            form = PatientForm(request.POST)
        elif user_type == 'doctor':
            form = DoctorForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            # Redirect to login or dashboard as per your application flow
            return redirect('login')
    else:
        form = PatientForm()  # Default form

    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    # Display user details on the dashboard
    return render(request, 'dashboard.html', {'user': user})



