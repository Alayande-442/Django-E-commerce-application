from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name="sign-up-page"),
    path('login/', views.login, name="login-page"),
    path('logout/', views.logout, name="logout-page"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate-page'),
    
]