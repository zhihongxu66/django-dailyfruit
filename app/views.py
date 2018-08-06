from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import TypeInfo,GoodsInfo


def index(request,id):
    if request.method == 'GET':
        types = TypeInfo.objects.all()
        if id == 0:
            goods = GoodsInfo.objects.all()
        else:
            goods = GoodsInfo.objects.filter(gtype=id)
        data = {
            'types':types,
            'goods':goods,
            'id':id,
        }

        return render(request,'app/index.html',data)


def cart(request):
    if request.method == 'GET':
        return render(request, 'app/cart.html')

    else:
        id = request.POST.get('id')
        good = GoodsInfo.objects.get(id=id)



def detail(request):
    if request.method == 'GET':
        return render(request, 'app/detail.html')


def place_order(request):
    if request.method == 'GET':
        return render(request, 'app/place_order.html')


def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'app/user_center_info.html')


def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'app/user_center_order.html')


def user_center_site(request):
    if request.method == 'GET':
        return render(request, 'app/user_center_site.html')


def list(request,id):
    if request.method == 'GET':
        goods = GoodsInfo.objects.filter(gtype=id)
        types = TypeInfo.objects.all()
        data = {
            'goods':goods,
            'types':types,
        }
        return  render(request, 'app/list.html', data)