from django.shortcuts import render

def home_view(request):
    return render(request, 'inicio/home.html')
def acerca_de_mi_view(request):
    return render(request, 'inicio/acerca_de_mi.html')