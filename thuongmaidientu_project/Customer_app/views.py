from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
# Thêm model User trong authentication
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import os
from django.conf import settings


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Kiểm tra xem username đã tồn tại trong hệ thống chưa
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Tên tài khoản đã có. Hãy đặt tên khác')
            return redirect('register')

        # Tạo người dùng mới
        user = User.objects.create_user(username=username, password=password)

        # Nếu tạo người dùng thành công, đăng nhập và chuyển hướng đến trang chính
        if user:
            messages.info(request, 'Đăng ký thành công!')
            return redirect('login')
        else:
            messages.error(request, 'Đã có lỗi xảy ra. Vui lòng thử lại sau.')

    return render(request, 'Customer_app/register.html')

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    # Nếu người dùng là admin, chuyển hướng đến trang admin
                    return redirect('admin:index')
                else:
                    # Ngược lại, chuyển hướng đến trang chính của ứng dụng
                    return redirect('home')
            else:
                messages.info(request, 'tên đăng nhập hoặc mật khẩu không đúng')
                
    else:
        form = LoginForm()
        
    return render(request,'Customer_app/login.html',{'form': form})
        
    
def sign_out(request):
    logout(request)
    return redirect('home')

def analyst(request):
    # thông tin tài khoản
    current_user = request.user
    
    # Đường dẫn tới thư mục chứa hình ảnh
    image_folder = settings.IMG_ANALYST_ROOT
    image_urls = []

    # Lấy danh sách các tệp hình ảnh trong thư mục
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_urls.append(settings.IMG_ANALYST_URL + filename)

    context = {'current_user':current_user,'image_urls': image_urls}
    # Trả về template HTML và truyền danh sách các URL hình ảnh vào template
    return render(request, 'Customer_app/analyst.html', context)