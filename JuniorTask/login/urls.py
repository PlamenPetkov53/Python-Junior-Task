import login.views as login_views
from knox import views as knox_views
from django.urls import path


app_name = 'drf_login'

urlpatterns = [
    path('register/', login_views.RegisterAPI.as_view(), name='register'),
    path('', login_views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    
]