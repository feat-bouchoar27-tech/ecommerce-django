from django.shortcuts import render

def product_list(request):
    return render(request, 'products_list.html')

def product_detail(request, id):
    return render(request, 'product_detail.html', {"id": id})