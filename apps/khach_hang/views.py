from django.shortcuts import render, redirect
from django.contrib import messages
from apps.nguoi_dung.models import NguoiDung
from apps.khach_hang.models import KhachHang
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def profile(request):
    nguoidung_list = NguoiDung.objects.get(tai_khoan = request.user.username)
    khachhang_list = KhachHang.objects.get(ma_nguoi_dung = nguoidung_list.ma_nguoi_dung)
    return render(request, 'pages/profile.html', {'nguoidung_list': nguoidung_list, 'khachhang_list': khachhang_list})

@csrf_exempt
def updateProfile(request): 
    nguoidung_list = NguoiDung.objects.get(tai_khoan = request.user.username)
    khachhang_list = KhachHang.objects.get(ma_nguoi_dung = nguoidung_list.ma_nguoi_dung)
    if request.method == 'POST':
        tenkhachhang = request.POST.get("tenkhachhang", False)
        taikhoan = request.POST["taikhoan"]
        email = request.POST["email"]
        sdt = request.POST["sdt"]
        sonha = request.POST["sonha"]
        duong = request.POST["duong"]
        phuong = request.POST["phuong"]
        quan = request.POST["quan"]
        thanhpho = request.POST["thanhpho"]

        nguoidung_list.tai_khoan = taikhoan
        nguoidung_list.email = email
        nguoidung_list.save()
         
        khachhang_list.ten_khach_hang = tenkhachhang
        khachhang_list.sdt = sdt 
        khachhang_list.so_nha = sonha 
        khachhang_list.duong = duong 
        khachhang_list.phuong = phuong 
        khachhang_list.quan = quan 
        khachhang_list.thanh_pho = thanhpho
        khachhang_list.save()
        messages.success(request, "Cập nhập thông tin thành công")
    return redirect('/profile')

@csrf_exempt
def changePass(request):
    myuser = User
    if request.method == "POST":
        password = request.POST["password"]
        newpass = request.POST["newpassword"]
        confirm = request.POST["confirmpassword"]
        if password == newpass:
            messages.warning(request, "Mật khẩu trùng với mật khẩu cũ! Vui lòng nhập lại!!!")
            return redirect(changePass)
        if newpass != confirm: 
            messages.warning(request, "Mật khẩu mới không trùng! Vui lòng nhập lại!!!")
            return redirect(changePass)
        else:
            myuser.password = newpass
            myuser.save()
            messages.success(request, "Đổi mật khẩu thành công")
    return redirect("/profile")