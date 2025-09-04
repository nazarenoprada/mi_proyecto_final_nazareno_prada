from django.shortcuts import render, redirect

def buy_view(request):
    """
    Vista para la página de compra. Si el formulario se envía,
    redirige a la página de compra finalizada.
    """
    if request.method == 'POST':
        return redirect('buy:finish_buy')
    
    return render(request, 'buy/buy.html')

def finish_buy_view(request):
    return render(request, 'buy/finish_buy.html')
