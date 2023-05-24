from django.shortcuts import render

def frontpage(request):
    return render(request, 'basket_app/frontpage.html')
