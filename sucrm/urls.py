from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from leads.views import HomeView, SigupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('leads/', include('leads.urls', namespace="leads")),
    path('agents/', include('agents.urls', namespace="agents")),
    path('signup/', SigupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('password-reset/', PasswordResetView.as_view(), name="password-reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path('logout/', LogoutView.as_view(), name="logout")
]
