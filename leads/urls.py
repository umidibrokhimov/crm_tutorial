from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name = "leads"

urlpatterns = [
    path('leads/', ListView.as_view(), name='leads-details'),
    path('', HomeView.as_view()),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('leads/create/', LeadCreateView.as_view(), name='lead-create'),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup')
]