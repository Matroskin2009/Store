from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


class ExitAccount:
    @staticmethod
    @csrf_exempt
    def exit_account(request):
        if request.method == 'POST':
            logout(request)
            return JsonResponse({'message': 'Вы успешно вышли из аккаунта', 'success': True}, status=200)
        else:
            return redirect('account')