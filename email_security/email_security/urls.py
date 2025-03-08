from django.contrib import admin
from django.urls import path
from security import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('', views.home, name='home'),  # Home Page
    path('login/', views.user_login, name='login'),  # Login Page
    path('logout/', views.user_logout, name='logout'),  # Logout
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard
    # path('check-spam/', views.check_spam, name='check_spam'),
    # path('check-phishing/', views.check_phishing, name='check_phishing'),
    # path('check-threats/', views.check_threats, name='check_threats'),
    # path('check-email-auth/', views.check_email_auth, name='check_email_auth'),
    # path('encrypt-email/', views.encrypt_email, name='encrypt_email'),

    path('check-ip/', views.check_ip, name='check_ip'),
    path('check-hash/', views.check_hash, name='check_hash'),
    path('check-domain/', views.check_domain, name='check_domain'),

    # ✅ Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="security/password_reset.html"), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="security/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="security/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="security/password_reset_complete.html"), name="password_reset_complete"),
]
