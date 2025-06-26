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
                if user.check_password(password):
                    login(request, user)
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    return JsonResponse({'message': 'Успешно', 'reg': True, 'user_id': user.id})
                else:
                    return JsonResponse({'message': 'Некорректный пароль'}, status=401)
            except User.DoesNotExist:
                return JsonResponse({'message': f'Пользователь {username} не найден'}, status=404)


