from datetime import datetime
from decimal import Decimal
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from apps.loai_san_pham.models import LoaiSanPham as LoaiSanPham_model
from apps.san_pham.models import SanPham as SanPham_Model
from apps.nguoi_dung.models import NguoiDung
from apps.don_hang.models import DonHang
from apps.khach_hang.models import KhachHang
from apps.san_pham.models import SanPham
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import string
# Create your views here.


def get_home(request): 
    loaisanpham_list = LoaiSanPham_model.objects.filter().order_by('ma_loai')
    sanpham_list = SanPham_Model.objects.filter().order_by('ma_san_pham')
    cart = None
    if 'cart' in request.session: 
        cart = request.session['cart']
    return render(request, 'body/index.html', { "loaisanpham_list" :loaisanpham_list, "sanpham_list" :sanpham_list})

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user is not None: 
            login(request, user)
            fname = user.first_name
            return redirect('/')
        else: 
            messages.error(request, "Tài khoản hoặc mật khẩu không đúng! Vui lòng nhập lại!!!")
            return redirect('/signin')
    return render(request, 'pages/login.html')

@csrf_exempt
def signup(request):
    user = NguoiDung()
    khachhang = KhachHang()
    soluong_nguoidung = NguoiDung.objects.filter().count()
    soluong_khachhang = KhachHang.objects.filter().count()
    if request.method == "POST":
        soluongnguoidung = soluong_nguoidung + 1
        taikhoan = request.POST["username"]
        email = request.POST["email"]
        matkhau = request.POST["password"]
        loaitaikhoan = "Khách hàng"

        if User.objects.filter(username = taikhoan).exists() and NguoiDung.objects.filter(tai_khoan = taikhoan):
            messages.warning(request, "Username đã tồn tại! Vui lòng nhập username khác")
            return redirect(signup)
        if User.objects.filter(email = email).exists() and NguoiDung.objects.filter(email = email):
            messages.warning(request, "Email đã tồn tại! Vui Lòng nhập Email khác")
            return redirect(signup)
        else: 
            user.ma_nguoi_dung = soluongnguoidung
            user.tai_khoan = taikhoan
            user.mat_khau = matkhau
            user.email = email
            user.loai_tai_khoan = loaitaikhoan

            khachhang.ma_khach_hang = soluong_khachhang + 1
            khachhang.ten_khach_hang = request.POST['lname'] + request.POST['fname']
            khachhang.ma_nguoi_dung = user
            khachhang.sdt = " "
            khachhang.so_nha = ""
            khachhang.duong = " "
            khachhang.phuong = " "
            khachhang.quan = " "
            khachhang.thanh_pho = " "
            khachhang.khach_hang_thuong_xuyen = 0

            myuser = User.objects.create_user(taikhoan, email, matkhau)
            myuser.first_name = request.POST['fname']
            myuser.last_name = request.POST['lname']
            user.save()
            khachhang.save()
            myuser.save()
        
        messages.success(request, "Bạn đã đăng ký thành công")  
        return redirect(signin)
        
    return render(request, 'pages/signup.html')

def signout(request): 
    logout(request)
    return redirect('home')

def shop(request):
    sanpham_list = SanPham_Model.objects.filter().order_by('ma_loai')
    loaisanpham_list = LoaiSanPham_model.objects.filter().order_by('ma_loai')
    soluong_sanpham = SanPham_Model.objects.all().count()
    page = Paginator(sanpham_list, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    return render(request, 'pages/shop.html', { "loaisanpham_list" :loaisanpham_list, "soluong_sanpham":soluong_sanpham, 'page': page} )

def maloai(request, id):
    productcat = SanPham_Model.objects.filter(ma_loai = id)
    loaisanpham_list = LoaiSanPham_model.objects.filter().order_by('ma_loai')
    soluong_sanpham = SanPham_Model.objects.filter(ma_loai = id).count()
    page = page = Paginator(productcat, 3)
    page_list = request.GET.get('page_maloai')
    page = page.get_page(page_list)
    return render(request, 'pages/categories.html', {'productcat': productcat, 'page': page, 'loaisanpham_list': loaisanpham_list, 'soluong_sanpham': soluong_sanpham})

def detail(request, id):
    ChiTietSanPham_list = SanPham.objects.get(ma_san_pham = id)
    loaisanpham_list = LoaiSanPham_model.objects.get(ma_loai = ChiTietSanPham_list.ma_loai)
    return render(request, "pages/detail.html", {'ChiTietSanPham_list': ChiTietSanPham_list, 'loaisanpham_list': loaisanpham_list})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print("Action:", action)
    print("ProductId:", productId)


    return JsonResponse("Item was added", safe=False)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' 

def addcart(request): 
    if is_ajax(request=request):
        id = request.POST.get('id')
        num = request.POST.get('num')
        chitietSanPham = SanPham.objects.get(ma_san_pham = id)
        cart = []
        if 'cart' in request.session:
            cart = request.session['cart']
        updateCart = []
        inCart = False
        for cartProduct in cart: 
            currentId = cartProduct.get('id')
            if currentId == chitietSanPham.ma_san_pham:
                inCart = True
                if num != 1:
                    cartProduct['quantity'] = cartProduct['quantity'] + int(num)
                else:
                    cartProduct['quantity'] = cartProduct['quantity'] + 1
            updateCart.append(cartProduct)
        if inCart == False:
            updateCart.append({
                "id": chitietSanPham.ma_san_pham,
                "name": chitietSanPham.ten_san_pham,
                "image": str(chitietSanPham.hinh_anh),
                "price": str(chitietSanPham.don_gia),
                'quantity': int(num)
            })
        request.session['cart'] = updateCart
    return HttpResponseRedirect('/shop/cart')

def clearCart(request):
    del request.session['cart']
    return HttpResponse("Xóa thành công ")

def xoaCartItem(request, id):
    cart = []
    if 'cart' in request.session:
        cart = request.session['cart']
    updateCart = []
    for cartProduct in cart: 
        currentId = cartProduct.get('id')
        if currentId != id:
            updateCart.append(cartProduct)
    request.session['cart'] = updateCart

    return HttpResponseRedirect('/shop/cart')
    #return HttpResponse("Xóa sản phẩm thành công")
@login_required
def cart(request):
    global total
    cart = None
    if 'cart' in request.session:
        cart = request.session['cart']
    total = 0
    if cart is not None: 
        for value in cart:
            total += Decimal(value['price']) * int(value['quantity'])
            request.session['total'] = int(total)
    return render(request, 'pages/cart.html', {'cart': cart, 'total':total}) 

def updateCart(request):
    return 
