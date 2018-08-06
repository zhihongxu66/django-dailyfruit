from django.conf.urls import url
from app import views


urlpatterns = [
    # 主页
    url(r'^index/(?P<id>\d+)/', views.index, name='index'),
    # 购物车
    url(r'^cart/', views.cart, name='cart'),
    # detail某一件商品的详情信息
    url(r'^detail/', views.detail, name='detail'),
    # place_order提交订单页
    url(r'^place_order/', views.place_order, name='place_order'),
    # user_center_info用户中心-用户信息页，用户中心功能一，查看用户的基本信息
    url(r'^user_center_info', views.user_center_info, name='user_center_info'),
    # user_center_order用户中心-用户订单页，用户中心功能二，查看用户的全部订单
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # user_center_site,用户中心，用户收货地址页，用户中心功能三，查看和设置用户的收货地址
    url(r'^user_center_site/', views.user_center_site, name='user_center_site' ),
    # 查看更多商品
    url(r'^list/(?P<id>\d+)/', views.list, name='list'),



]