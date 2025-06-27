from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render

from StoreApp.models import User


class PasswordAccount:
    @staticmethod
    def change_password_form(request):
        if 'user_id' in request.session:
            return render(request, 'change_password.html')
        else:
            return render(request, 'index.html')

    @staticmethod
    def change_password(request):
        user_id = request.session['user_id']
        if request.method == 'POST':
            user = User.objects.get(id=request.session['user_id'])
            password_now = request.POST.get('current_password')
            password_new = request.POST.get('new_password')
            password_confirm = request.POST.get('confirm_password')
            if check_password(password_now, user.password):
                if password_new == password_confirm and password_new is not None:
                    if password_new == password_confirm and password_new is not None:
                        try:
                            user.set_password(password_new)
                            user.save()
                            return JsonResponse({
                                'message': 'Вы успешно поменяли пароль',
                                'reg': True,
                                'registered': True
                            })
                        except Exception as e:
                            return JsonResponse({
                                'message': f'Ошибка на стороне сервера, пожалуйста, попробуйте позже {user_id} {e}',
                                'reg': False,
                                'registered': True
                            })
                else:
                    return JsonResponse({
                        'reg': False,
                        'message': 'Нужно ввести новый пароль два раза! Они должны быть одинаковыми',
                        'registered': True
                    })
            else:
                return JsonResponse({
                    'reg': False,
                    'message': 'В базе данных такого пароля нет',
                    'registered': True
                })
        else:
            return render(request, 'change_password.html')