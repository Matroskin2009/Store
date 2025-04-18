from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
import logging
from StoreApp.models import User

logger = logging.getLogger(__name__)

class AuthUser:
    @staticmethod
    def auth_form(request):
        if 'user_id' in request.session:
            return redirect('index')
        return render(request, 'auth.html')

    def users_auth(self, request):
        if 'user_id' in request.session:
            return JsonResponse({'reg': True, 'message': 'Вы уже авторизованы'}, status=200)

        if request.method == 'GET':
            return render(request, 'auth.html', context={'message': "пожалуйста, введите данные"})
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not username or not password:
                return JsonResponse({'message': 'Не успешно: Пожалуйста, введите имя пользователя и пароль'}, status=400)
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    request.session['username'] = username
                    request.session.save()
                    logger.debug(f'все пучком {user.id}')
                    return JsonResponse({'message': 'Успешно', 'reg': True, 'user_id': user.id})

                else:
                    return JsonResponse({'message': 'Не успешно: Некоректный Пароль'})
            except User.DoesNotExist as e:
                return JsonResponse({'message': f'Не успешно: {username} не найден'})