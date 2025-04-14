from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Users  # Your custom user model
from lmsfeatures.models import EnrollCourse

class LoginTemplateView(TemplateView):
    template_name = 'login.html'


class RegisterTemplateView(TemplateView):
    template_name = 'register.html'


class UserLoginView(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

class UserRegisterView(View):
    def post(self, request):
        # Collect the data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
       
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')  # Stay on the same page with the error message

        # Check if the email or username already exists
        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

      

        # Create the user
        try:
            user = Users.objects.create_user(email=email, password=password)
            user.name = name
            user.phone_number = phone_number
            user.save()

            # Success message
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('register')
        
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    login_url = 'login'



class EnrollCourseView(LoginRequiredMixin, TemplateView):
    template_name = 'enrollCourse.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all enrolled courses for the current user
        context['enrolled_courses'] = EnrollCourse.objects.filter(user_id=self.request.user)
        return context
    
class EnrollSingleCourseView(LoginRequiredMixin, TemplateView):
    template_name = 'singleCourse.html'
    login_url = 'login'
    
   