from .views import HomePageView, SignUpView, LoginView, LogOutView
from django.urls import path


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/register/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogOutView.as_view(), name='logout'),
]
