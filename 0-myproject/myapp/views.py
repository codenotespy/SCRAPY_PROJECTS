from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello, world. You're at the myapp index.")



def search(request):
    if request.method == 'GET':
        part_name =  request.GET.get('search').replace('-', '').replace(',', '').replace(' ', '').replace('.', '').replace('/', '').replace('\\', '').replace('|', '').replace('*', '').replace('+', '').replace(':', '').replace(';', '').replace('?', '')
        results = main_table.objects.filter(part_no_form__icontains=part_name) | main_table.objects.filter(cross_part_form__icontains=part_name)
        resultnumber = results.count()
        return render(request, "home.html", {'results': results, 'resultnumber': resultnumber})
    else:
        return render(request,"home.html")
    

