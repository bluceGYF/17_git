from django.shortcuts import render


def order_details(request):
    return render(request, 'order/order_details.html', locals())



