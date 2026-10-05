from django.shortcuts import render

def calculadora_view(request):
    return render(request, 'app_actions/actions.html')