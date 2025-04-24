from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.shortcuts import redirect, render
import logging

from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import User
logger = logging.getLogger(__name__)

def Index(request):
    user_id = request.session.get('user_id')
    if user_id:
        return render(request, 'index.html', context={'userRegistered': True})
    else:
        return render(request, 'index.html', context={'userRegistered': False})

def basket(request):
    return render(request, 'basket.html')

def account(request):
    orderCount = 0
    username = request.session.get('username')
    return render(request, 'account.html', context={'name': username, 'orderCount': orderCount})

def liked(request):
    return render(request, 'liked.html')

