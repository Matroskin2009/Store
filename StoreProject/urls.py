
from django.contrib import admin
from django.urls import path

from StoreApp import views
from StoreApp.User.auth import AuthUser
from StoreApp.User.reg import RegestrationUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg_user/', RegestrationUser.add_users, name='reg_user'),  # Make sure this path exists
    path('reg_form/', RegestrationUser.reg_form, name='reg_form'),  # Make sure this path exists
    path('auth_form/', AuthUser.auth_form, name='auth_form'),
    path('auth/', AuthUser().users_auth, name='auth_users'),
    path('index/', views.Index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('account/', views.account, name='account'),
    path('liked/', views.liked, name='liked'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('changePasswordForm/', views.changePasswordForm, name='changePasswordForm'),
    path('changeNameForm/', views.changeNameForm, name='changeNameForm'),
    path('changeName/', views.changeName, name='changeName'),
    path('exitAccount/', views.exitAccount, name='exitAccount')
]
