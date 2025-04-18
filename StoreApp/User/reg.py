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
            return JsonResponse({'reg': True, 'message': 'Вы уже авторизованы'}, status=200)

        if request.method == 'POST':
            username = request.POST.get('user')
            password = request.POST.get('password')

            if not username or not username.strip() or not password:
                logger.error('username or password is empty. Regestration')
                return JsonResponse({'message': 'ошибка, не поле не может быть пустым', 'redirect': 'false'}, status=400)
            if User.objects.filter(username=username).exists():
                logger.error('user is created, error. Regestration ')
                return JsonResponse({'message': 'Такой пользователь уже есть в базе данных', 'reg': False}, status=409)
            try:
                better_password = make_password(password)
                user = User.objects.create(username=username, password=better_password)

                request.session['user_id'] = user.id  # Сохраняем ID пользователя в сессии
                request.session['username'] = user.username  # Сохраняем имя пользователя в сессии
                request.session.save()

                logger.info('user is could register! Loger')
                return JsonResponse({'reg': True}, status=200)
            except Exception as e:
                logger.error('user could not registered. Loger')
                return JsonResponse({'message': 'Ошибка сервера, пожалуйста попробуйте позднее', 'reg': False}, status=500)
        else:  # GET запрос
            user_id = request.session.get('user_id')
            username = request.session.get('username')

            if user_id and username:
                # Пользователь авторизован
                return JsonResponse({'message': f'Привет, {username}!', 'redirect': 'true'})
            else:
                # Пользователь не авторизован
                return JsonResponse({
                    'message': 'Пожалуйста, войдите в систему',
                    'redirect': 'false',
                    'authenticated': False
                }, status=200)





