from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')


def result_view(request):
    if request.method == "GET":
        return render(request, 'result.html')
    elif request.method == "POST":
        print(request.POST)
        get_action = request.POST.get('action')
        first = int(request.POST.get('first'))
        second = int(request.POST.get('second'))
        result = 0
        if get_action == '+':
            result = first + second
        elif get_action == '-':
            result = first - second
        elif get_action == '*':
            result = first * second
        elif get_action == '/':
            result = first / second
        context = {
            'first': first,
            'second': second,
            'action': get_action,
            'result': result,
        }
        return render(request, 'result.html', context)
