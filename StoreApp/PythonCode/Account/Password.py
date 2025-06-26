from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render

from StoreApp.models import User


class PasswordAccount:
    @staticmethod
    def changePasswordForm(request):
        if 'user_id' in request.session:
            return render(request, 'changePassword.html')
        else:
            return render(request, 'index.html')

    @staticmethod
    def changePassword(request):
        user_id = request.session['user_id']
        if request.method == 'POST':
            user = User.objects.get(id=request.session['user_id'])
            passwordNow = request.POST.get('current_password')
            passwordNew = request.POST.get('new_password')
            passwordConfirm = request.POST.get('confirm_password')
            if check_password(passwordNow, user.password):
                if passwordNew == passwordConfirm and passwordNew != None:
                    if passwordNew == passwordConfirm and passwordNew != None:
                        try:
                            user.set_password(passwordNew)
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
            return render(request, 'changePassword.html')