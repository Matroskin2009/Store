from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path

from StoreApp import views
from StoreApp.PythonCode.User.auth import AuthUser
from StoreApp.PythonCode.User.reg import RegestrationUser

from StoreApp.PythonCode.Account.Exit import ExitAccount
from StoreApp.PythonCode.Account.Name import NameAccount
from StoreApp.PythonCode.Account.Password import PasswordAccount
from StoreProject import settings
from StoreApp.PythonCode.Basket.Basket import ButtonsBasket, BasketPage



urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg_user/', RegestrationUser.addUsers, name='reg_user'),
    path('reg_form/', RegestrationUser.regForm, name='reg_form'),
    path('auth_form/', AuthUser.auth_form, name='auth_form'),
    path('auth/', AuthUser().users_auth, name='auth_users'),
    path('index/', views.Index, name='index'),
    path('basket/', BasketPage.toBasket, name='basket'),
    path('account/', views.account, name='account'),
    path('changePassword/', PasswordAccount.changePassword, name='changePassword'),
    path('changePasswordForm/', PasswordAccount.changePasswordForm, name='changePasswordForm'),
    path('changeNameForm/', NameAccount.changeNameForm, name='changeNameForm'),
    path('changeName/', NameAccount.changeName, name='changeName'),
    path('product/<int:product_id>/add_to_cart/', views.addCart, name='addCart'),
    path('exitAccount/', ExitAccount.exitAccount, name='exitAccount'),
    path('products/', views.productList, name='productList'),
    path('product/<int:product_id>/', views.productPage, name='productPage'),
    path('product3d/<int:product_id>/', views.productPage3d, name='productPage3d'),
    path('basketMinus/<int:productId>/', ButtonsBasket.buttonMinus, name='buttonMinus'),
    path('basketPlus/<int:productId>/', ButtonsBasket.buttonPlus, name='buttonPlus'),
    path('basketDelete/<int:productId>/', ButtonsBasket.buttonDelete, name='buttonDelete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
