import uuid
from datetime import date
from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.contrib import messages
from apps.don_hang.models import DonHang
from apps.nguoi_dung.models import NguoiDung
from apps.khach_hang.models import KhachHang
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here
    
def order(request):
    cart = None
    total = 0
    a = 1
    if 'cart' in request.session:
        cart = request.session['cart']
    for value in cart:
        total += Decimal(value['price']) * int(value['quantity'])
    if 'total' in request.session:
        total = request.session['total']
        current_user = request.user
        username = current_user.username
        donhang = DonHang()
        donhanglist = DonHang.objects.filter().count()
        nguoi_dung_hien_tai = NguoiDung.objects.get(tai_khoan = username)
        donhang.ma_don_hang = "DH_" + str(donhanglist+1)
        request.session['fdonhang'] = donhang.ma_don_hang
        donhang.ten_don_hang = "Đơn hàng" + str(donhanglist+1)
        request.session['fcart'] = donhang.ma_don_hang
        donhang.ngay_dat = date.today()
        donhang.tong_tien_hang = total
        donhang.ma_khach_hang = KhachHang.objects.get(ma_nguoi_dung = nguoi_dung_hien_tai.ma_nguoi_dung)
        donhang.save()
    return render(request, "pages/checkout.html", {"cart": cart, "total": total})

def formPay(request): 
    donhang_id = request.session['fdonhang']
    donhang = get_object_or_404(DonHang, ma_don_hang = donhang_id)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': donhang.tong_tien_hang,
        'item_name': donhang.ten_don_hang,
        'invoice': donhang.ma_don_hang,
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,reverse('payment_return')),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancel')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'pages/payment.html', {"form": form})

@csrf_exempt
def payment_return(request):
    messages.success(request, "You're successfully made a payment.")
    return redirect('home')

@csrf_exempt
def payment_cancel(request):
    messages.error(request, "Your order has been canceled.")
    return redirect('formPay')