from django.shortcuts import render
from django.urls.conf import path
from .  import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.CreateUserView.as_view(), name="create"),
    path("profile/<pk>[0-9]/", views.ProfileDetailView.as_view(), name="user_profile"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path("profile/edit/", views.EditUserProfileView.as_view(), name="edit"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name='account/logout.html'), name="logout"),
    path("confirm/", views.confirm_information, name="confirm_information"),
    
    path("recover/", views.RecoverView.as_view(), name="recover_password"),
    path("recover/reset/done/", views.RecoverResetDoneView.as_view(), name="recover_password_done"),
    path("recover/reset/<token>/", views.RecoverResetView.as_view(), name="recover_password_reset"),
    path("recover/<signature>/", views.RecoverDoneView.as_view(), name="recover_password_sent"),
]