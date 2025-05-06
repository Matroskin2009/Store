from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path

from StoreApp import views
from StoreApp.User.auth import AuthUser
from StoreApp.User.reg import RegestrationUser

from StoreApp.Account.Exit import ExitAccount
from StoreApp.Account.Name import NameAccount
from StoreApp.Account.Password import PasswordAccount
from StoreProject import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg_user/', RegestrationUser.add_users, name='reg_user'),
    path('reg_form/', RegestrationUser.reg_form, name='reg_form'),
    path('auth_form/', AuthUser.auth_form, name='auth_form'),
    path('auth/', AuthUser().users_auth, name='auth_users'),
    path('index/', views.Index, name='index'),
    path('basket/', views.basket, name='basket'),
    path('account/', views.account, name='account'),
    path('liked/', views.liked, name='liked'),
    path('changePassword/', PasswordAccount.changePassword, name='changePassword'),
    path('changePasswordForm/', PasswordAccount.changePasswordForm, name='changePasswordForm'),
    path('changeNameForm/', NameAccount.changeNameForm, name='changeNameForm'),
    path('changeName/', NameAccount.changeName, name='changeName'),
    path('exitAccount/', ExitAccount.exitAccount, name='exitAccount'),
    path('products/', views.productList, name='productList'),
    path('product/<int:product_id>/', views.product_detail, name='catalog')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
