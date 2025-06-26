from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from StoreApp.models import User
import logging
logger = logging.getLogger(__name__)

class NameAccount:
    @staticmethod
    def changeNameForm(request):
        if 'user_id' in request.session:
            username = request.session.get('username')
            return render(request, 'changeName.html', context={'name': username})
        else:
            return render(request, 'index.html', context={'registered': False})

    @staticmethod
    @csrf_exempt
    def changeName(request):
        if request.method == 'POST':
            newUsername = request.POST.get('new_name')
            if 'user_id' in request.session:
                try:
                    if User.objects.filter(username=newUsername).exists():
                        logger.error('Пользователь уже создан, ошибка.')
                        return JsonResponse({'reg': False, 'message': 'пользователь был зарегистрирован ранее', 'name': newUsername}, status=409)

                    if newUsername:
                        if newUsername != request.session['username']:
                            user = User.objects.get(id=request.session['user_id'])
                            user.username = newUsername
                            user.save()
                            request.session['username'] = newUsername
                            return JsonResponse({'reg': True, 'message': 'Вы успешно поменяли имя!', 'name': newUsername}, status=200)
                        else:
                            return JsonResponse({'reg': False, 'message': 'Прошлое имя должно отличаться от старого!', 'name': newUsername}, status=400)
                    else:
                        return JsonResponse({'reg': False, 'message': 'Имя не может быть пустым!', 'name': newUsername}, status=400)
                except Exception as e:
                    return JsonResponse({'reg': False, 'message': f'Ошибка сервера, попробуйте позже: {e}', 'name': newUsername}, status=500)
            else:
                return JsonResponse({'reg': False, 'registered': False})
        else:
            username = request.session.get('username')
            return render(request, 'changeName.html', context={'name': username})