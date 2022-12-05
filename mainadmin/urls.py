from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.admin,name="admin"),
    path("dashboard",views.admin_dashbord,name="admin_home"),
    path("login",views.login,name="admin_login"),
    path('blck!<p>',views.block,name='block'),
    path('unblck!<po>',views.unblock,name='unblock'),
    path('users',views.admin_users,name='admin_users'),
    path('logout',views.logout,name='admin_logout'),
    path('product',views.admin_products,name='admin_products'),
    path('add_product',views.admin_addproducts,name='admin_addproducts'),
    path('edit!<id>',views.admin_editproducts,name='admin_editproducts'),
    path('dele!<id>',views.admin_deleteproducts,name='admin_deleteproducts'),
    path('ad_brand',views.admin_brand,name='admin_brand_add'),
    path('oders',views.admin_oders,name="oders"),
    path('change-status',views.change_status,name="change_status"),
    path('order_det!<id>',views.admin_orders_details,name="admin_orders_details"),
    path('coupon!<id>',views.coupon,name="coupon")
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
