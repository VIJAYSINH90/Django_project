from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import User
from .forms import UserRegisterForm,VendorRegisterForm,AdminRegisterForm,UserProfileForm,ContactForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView,TemplateView,FormView
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import user_required,vendor_required,admin_required
from django.core.mail import send_mail
from django.conf import settings

class IndexView(TemplateView):
    template_name = 'user/index.html'
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class VendorRegisterView(CreateView):
    model = User
    form_class = VendorRegisterForm
    template_name = 'user/vendor_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'user/login.html'
    success_url = '/user/login/'
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
           if self.request.user.is_user:
            return '/user/user/dashboard'
           elif self.request.user.is_vendor:
            return '/user/vendor/dashboard'
           else:
            return '/user/admin/dashboard'
        
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #     messages.success(request, "You have been logged out.")
    #     return response


@method_decorator([login_required(login_url='/user/login/'),vendor_required],name='dispatch')       
class VendorDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        product = Product.objects.filter()
        sort_by = self.request.GET.get('sort_by','product_name')
        direction = self.request.GET.get('direction','asc')
        print(".....",sort_by)
        print(".....",direction)
        if direction == 'asc':
            product = product.order_by(sort_by)
        elif direction == 'desc':
            product = product.order_by(f'-{sort_by}')
        
        return render(request, 'user/vendor_dashboard.html',{
            'products':product,
        })

    template_name = 'user/vendor_dashboard.html'

@method_decorator([login_required(login_url='/user/login/'),admin_required],name='dispatch')
class AdminDashboardView(TemplateView):

    template_name = 'user/admin_dashboard.html'
    
@method_decorator([login_required(login_url='/user/login/'),user_required],name='dispatch')
class UserDashboardView(TemplateView):
    template_name = 'user/user_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #user = self.request.user
        products = Product.objects.filter()
        context['products'] = products
        return context
    
class UserProfileView(CreateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/user_profile.html'
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_user:
                return 'user/user/dashboard'
            elif self.request.user.is_vendor:
                return 'user/vendor/dashboard'
            else:
                return 'user/admin/dashboard'
class ContactView(FormView):
    template_name = 'user/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contactsuccess')

    def form_valid(self, form):
        name = form.cleaned_data.get('name', '')
        email = form.cleaned_data.get('email', '')
        message = form.cleaned_data.get('message', '')

        # Send email to site owner
        send_mail(
            'New message from Contact Us form',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email, # From email address
            [settings.EMAIL_HOST_USER], # To email address
            fail_silently=False,
        )

        return super().form_valid(form)