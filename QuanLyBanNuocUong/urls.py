import imp
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from apps.home import views as home
from apps.khach_hang import views as kh
from apps.san_pham import views as sanpham
from apps.don_hang import views as donhang
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile', kh.profile),
    path('updateProfile', kh.updateProfile),
    path('changePass', kh.changePass),
    path('', home.get_home, name='home'),

    #signin/signup
    path("signin", home.signin),
    path("signup", home.signup, name="signup"),
    path("signout", home.signout),
    path("clearcart", home.clearCart),
    path("update_item/", home.updateItem, name="update_item"),
    
    #shop
    path("shop/addCart", home.addcart, name='Mua hàng'),
    path("shop/cart", home.cart, name='Gio hang'),
    path("shop", home.shop, name='shop'),
    path("shop/cart/xoaCartItem/<str:id>", home.xoaCartItem),
    path("shop/maloai/<str:id>", home.maloai, name='San Pham Thuoc Danh Muc'),
    path("shop/detail/<str:id>", home.detail, name='Chi tiet san pham'),

    #checkout
    path("checkout/", donhang.order, name='formPay'),

    #paypal
    path('payment/', donhang.formPay, name='formPay'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment_return/', donhang.payment_return, name='payment_return'),
    path('payment_cancel/', donhang.payment_cancel, name='payment_cancel'),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
admin.site.site_header = "SodaPopStop"
