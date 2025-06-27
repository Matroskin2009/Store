from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path

from StoreApp import views
from StoreApp.PythonCode.User.auth import AuthUser
from StoreApp.PythonCode.User.reg import RegestrationUser

from StoreApp.PythonCode.Account.exit_account import ExitAccount
from StoreApp.PythonCode.Account.name_account import NameAccount
from StoreApp.PythonCode.Account.password_account import PasswordAccount
from StoreProject import settings
from StoreApp.PythonCode.Basket.basket_page import ButtonsBasket, BasketPage



urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg_user/', RegestrationUser.add_users, name='reg_user'),
    path('reg_form/', RegestrationUser.reg_form, name='reg_form'),
    path('auth_form/', AuthUser.auth_form, name='auth_form'),
    path('auth/', AuthUser().users_auth, name='auth_users'),
    path('index/', views.index, name='index'),
    path('basket/', BasketPage.to_basket, name='basket'),
    path('account/', views.account, name='account'),
    path('change_password/', PasswordAccount.change_password, name='change_password'),
    path('change_password_form/', PasswordAccount.change_password_form, name='change_password_form'),
    path('change_name_form/', NameAccount.change_name_form, name='change_name_form'),
    path('change_name/', NameAccount.change_name, name='change_name'),
    path('product/<int:product_id>/add_to_cart/', views.add_cart, name='add_cart'),
    path('exit_account/', ExitAccount.exit_account, name='exit_account'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_page, name='product_page'),
    path('product3d/<int:product_id>/', views.product_page3d, name='product_page3d'),
    path('basket_minus/<int:product_id>/', ButtonsBasket.button_minus, name='button_minus'),
    path('basket_plus/<int:product_id>/', ButtonsBasket.button_plus, name='button_plus'),
    path('basket_delete/<int:product_id>/', ButtonsBasket.button_delete, name='button_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
