from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse
from django.shortcuts import redirect, render
import logging

from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import User
logger = logging.getLogger(__name__)

def Index(request):
    for key, value in request.session.items():
        print(f"{key}: {value}")
    return render(request, 'index.html')

def basket(request):
    return render(request, 'basket.html')

def account(request):
    orderCount = 0
    username = request.session.get('username')
    return render(request, 'account.html', context={'name': username, 'orderCount': orderCount})

def liked(request):
    return render(request, 'liked.html')

def changePasswordForm(request):
    if 'user_id' in request.session:
        return render(request, 'changePassword.html')
    else:
        return render(request, 'index.html')


def changePassword(request):
    user_id = request.session['user_id']
    if user_id:
        print('Та все ок')
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(user_id)
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user_id'])
        password_now = request.POST.get('current_password')
        password_new = request.POST.get('new_password')
        password_confirm = request.POST.get('confirm_password')
        if check_password(password_now, user.password):
            if password_new == password_confirm and password_new != None:
                if password_new == password_confirm and password_new != None:
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
        if 'user_id' in request.session:
            return render(request, 'changePassword.html', context={'registered': True})
        else:
            return redirect('index')
def changeNameForm(request):
    if 'user_id' in request.session:
        username = request.session.get('username')
        return render(request, 'changeName.html', context={'name': username})
    else:
        return render(request, 'index.html', context={'registered': False})

@csrf_exempt
def changeName(request):
    print('воооооооооооооооооо')
    if request.method == 'POST':
        print("11111111111111111111111111111111111111111")
        new_username = request.POST.get('new_name')  # Получаем 'new_name' из формы!
        if 'user_id' in request.session:
            try:
                if User.objects.filter(username=new_username).exists():
                    logger.error('Пользователь уже создан, ошибка.')
                    return JsonResponse({'reg': False, 'message': 'пользователь был зарегистрирован ранее', 'name': new_username}, status=409)

                if new_username:
                    if new_username != request.session['username']:
                        user = User.objects.get(id=request.session['user_id'])
                        user.username = new_username
                        user.save()
                        request.session['username'] = new_username
                        return JsonResponse({'reg': True, 'message': 'Вы успешно поменяли имя!', 'name': new_username}, status=200)
                    else:
                        return JsonResponse({'reg': False, 'message': 'Прошлое имя должно отличаться от старого!', 'name': new_username}, status=400)
                else:
                    return JsonResponse({'reg': False, 'message': 'Имя не может быть пустым!', 'name': new_username}, status=400)
            except Exception as e:
                return JsonResponse({'reg': False, 'message': f'Ошибка сервера, попробуйте позже: {e}', 'name': new_username}, status=500)
        else:
            return JsonResponse({'reg': False, 'registered': False})
    else:
        username = request.session.get('username')
        return render(request, 'changeName.html', context={'name': username})


@csrf_exempt
def exitAccount(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Вы успешно вышли из аккаунта', 'success': True}, status=200)
    else:
        return redirect('account')

