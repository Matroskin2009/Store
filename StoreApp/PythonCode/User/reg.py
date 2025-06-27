from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse, HttpRequest
from django.shortcuts import render, redirect
import logging
from StoreApp.models import User

logger = logging.getLogger(__name__)


class RegestrationUser:
    @staticmethod
    def reg_form(request):
        if 'user_id' in request.session:
            return redirect('index')
        return render(request, 'registration.html')

    @staticmethod
    def add_users(request):  # type: (HttpRequest) -> JsonResponse
        if 'user_id' in request.session:
            return JsonResponse({'reg': True}, status=200)

        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            if not username or not username.strip() or not password:
                logger.error('username or password is empty')
                return JsonResponse({'message': 'ошибка, не поле не может быть пустым'}, status=400)
            if User.objects.filter(username=username).exists():
                logger.error('user is created, error')
                return JsonResponse({'message': 'Такой пользователь уже есть в базе данных', 'reg': False}, status=409)
            try:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                logger.info('user is could register!')
                print(f'Пользователь успешно зарегистрирован: {user.username} (ID: {user.id})')
                print(type(user.id))
                return JsonResponse({'reg': True}, status=200)
            except Exception as e:
                logger.error('user could not registered')
                return JsonResponse({'message': f'Ошибка сервера, пожалуйста попробуйте позднее', 'reg': False}, status=500)
        else:  # GET запрос
            return render(request, 'registration.html')




