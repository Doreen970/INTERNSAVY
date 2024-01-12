from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
#from .senders import SendEmail
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from my_blog.settings import EMAIL_HOST_USER


# Create your views here.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form}) 
    """

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            #email verification
            
            login(request, user)
            return redirect('index')  # Redirect to the home page after login
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index') 
     
def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            #send email
            mail = EmailMessage(
                'Welcome', #subject
                f'Hi {user.username}\n, Welcome to LaVie\n', #message
                settings.EMAIL_HOST_USER, #sender
                [user.email] #receiver
            )
            mail.send()
            login(request, user)
            #form.save()
            return redirect('login')
        
    return render(request, "accounts/signup.html", {
        "form": form
    })  

'''
def verify_email(request, uidb64, token, user_id):
    uidb64 = request.GET.get("uidb64")
    token = request.GET.get("token")
    user_id = request.GET.get("user_id")

    try:
            user_obj = User.objects.get(id=user_id)
    except User.DoesNotExist:
            messages.error(request, "You entered an invalid link")
            return redirect(reverse("login"))

    try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=uid)
    except Exception as e:
            user = None

        #Storing the email of the user to avoid error if link is accessed from a different client
    request.session["verification_email"] = (user_obj.email)  

    if user:
            if user.id != user_obj.id:
                messages.error(request, "You entered an invalid link")
                return redirect(reverse("login"))

            if email_verification_generate_token.check_token(user, token):
                user.is_email_verified = True
                user.save()
                messages.success(request, "Verification successful!")
                request.session["verification_email"] = None
                SendEmail.welcome(request, user)
                return redirect(reverse("login"))

    return render(
            request,
            "accounts/email-verification-failed.html",
            {"email": user_obj.email},
        ) 

def resend_verification(request):
    email = request.session.get("verification_email")
        
    try:
            user = User.objects.get(email=email)
            print(user)
    except User.DoesNotExist:
            messages.error(request, "Not allowed")
            return redirect(reverse("login"))

    if user.is_email_verified:
            messages.info(request, "Email address already verified!")
            request.session["verification_email"] = None
            return redirect(reverse("login"))

    SendEMail.verification_email(request, user)
    messages.success(request, "Email Sent")
    return render(
            request,
            "accounts/email-verification-request.html",
        )                 

'''        
