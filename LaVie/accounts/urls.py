from django.urls import path
#from .views import signup, user_login, user_logout
from .views import signup, user_logout, user_login, verify_email, resend_verification

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('verify-email/<uidb64>/<token>/<user_id>', verify_email, name='verify-email'),
    path('resend-verification-email', resend_verification, name='resend-verification-email'),
]
