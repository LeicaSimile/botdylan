from django.shortcuts import render

def songwriter(request):
    return render(request, 'songwriter/songwriter.html', {})
