from django.shortcuts import render, redirect
from .models import *
# thêm form
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# THỨ TỰ CÁC TYPE
# 1. ĐIỆN THOẠI 
# 2. LAPTOP 
# 3. SMARTWATCH 
# 4. TAI NGHE 
# 5. TIVI

# THỨ TỰ CÁC MANUFACTURE
# 1. APPLE 
# 2. SAMSUNG 
# 3. XIAOMI 
# 4. LENOVO 
# 5. DELL

# Create your views here.
# trang chủ chứa tất cả các sản phẩm
def home(request):
    # thông tin tài khoản
    current_user = request.user
    # list
    phone = Product.objects.filter(Type_ID_id='1')
    laptop = Product.objects.filter(Type_ID_id='2')
    smartwatch = Product.objects.filter(Type_ID_id='3')
    headphone = Product.objects.filter(Type_ID_id='4')
    tivi = Product.objects.filter(Type_ID_id='5')
    
    if request.method== "POST":
        # lấy gúa trị từ ô search
        search_value = request.POST['search_value']
        # sử dụng filter để nhập liệu
        phone = Product.objects.filter(Q( Product_Name__contains = search_value) |
                                        Q( Unit_Price__contains = search_value), Type_ID_id='1' )
        
        laptop = Product.objects.filter(Q( Product_Name__contains = search_value) |
                                         Q( Unit_Price__contains = search_value),Type_ID_id='2' )
        
        smartwatch = Product.objects.filter(Q( Product_Name__contains = search_value) |
                                         Q( Unit_Price__contains = search_value) ,Type_ID_id='3' )
        
        headphone = Product.objects.filter(Q( Product_Name__contains = search_value) |
                                         Q( Unit_Price__contains = search_value) ,Type_ID_id='4' )
        
        tivi = Product.objects.filter(Q( Product_Name__contains = search_value) |
                                         Q( Unit_Price__contains = search_value) ,Type_ID_id='5' )
        
        # thông tin tài khoản
        current_user = request.user
        
        context = {'phone': phone,'laptop':laptop , 'smartwatch':smartwatch,'headphone':headphone,'tivi':tivi , 'current_user':current_user}
        return render(request, 'Guest_app/home.html', context)
    
    context = {'phone':phone,'laptop':laptop,
               'smartwatch':smartwatch,'headphone':headphone,'tivi':tivi, 'current_user':current_user}
    return render(request, 'Guest_app/home.html',context)
 

# add product bằng admin của Django
# LIST 1.ĐIỆN THOẠI
def list_iphone(request):
    # Lọc các Type_ID là '1' (điện thoại) và lọc theo id APPLE  =1
    iphone = Product.objects.filter(Type_ID='1', Manufacture_ID= '1' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'iphone':iphone, 'current_user':current_user}
    return render(request , 'Guest_app/dien_thoai/iphone/iphone.html',context)

def list_samsung(request):
    # Lọc các Type_ID là '1' (điện thoại) và lọc theo id SAMSUNG = 2
    samsung = Product.objects.filter(Type_ID= '1', Manufacture_ID= '2')
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'samsung':samsung, 'current_user':current_user }
    return render(request , 'Guest_app/dien_thoai/samsung/samsung.html',context)

def list_xiaomi(request):
    # Lọc các Type_ID là '1' (điện thoại) và lọc theo id XIAOMI = 3
    xiaomi = Product.objects.filter(Type_ID= '1', Manufacture_ID= '3')

    # thông tin tài khoản
    current_user = request.user
    
    context = {'xiaomi':xiaomi, 'current_user':current_user}
    return render(request , 'Guest_app/dien_thoai/xiaomi/xiaomi.html',context)

# LIST 2.LAPTOP
def list_macbook(request):
    # Lọc các Type_ID là '2' (laptop) và lọc theo id APPLE =1
    macbook = Product.objects.filter(Type_ID= '2' , Manufacture_ID= '1' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'macbook':macbook, 'current_user':current_user}
    return render(request , 'Guest_app/laptop/macbook/macbook.html',context)

def list_lenovo(request):
    # Lọc các Type_ID là '2' (laptop) và lọc theo id LENOVO =4
    lenovo = Product.objects.filter(Type_ID='2', Manufacture_ID= '4' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'lenovo':lenovo, 'current_user':current_user}
    return render(request , 'Guest_app/laptop/lenovo/lenovo.html',context)

def list_dell(request):
    # Lọc các Type_ID là '2' (laptop) và lọc theo id DELL = 5
    dell = Product.objects.filter(Type_ID='2', Manufacture_ID= '5' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'dell':dell, 'current_user':current_user}
    return render(request , 'Guest_app/laptop/dell/dell.html',context)

# LIST 3.SMARTWATCH
def list_apple_watch(request):
    # Lọc các Type_ID là '3' (smart watch) và lọc theo id APPLE =1
    apple_watch = Product.objects.filter(Type_ID= '3', Manufacture_ID= '1' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'apple_watch':apple_watch, 'current_user':current_user}
    return render(request , 'Guest_app/smart_watch/apple_watch/apple_watch.html',context)

def list_samsung_watch(request):
    # Lọc các Type_ID là '3' (smart watch) và lọc theo id SAMSUNG = 2
    samsung_watch = Product.objects.filter(Type_ID= '3', Manufacture_ID= '2' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'samsung_watch':samsung_watch, 'current_user':current_user}
    return render(request , 'Guest_app/smart_watch/samsung/samsung_watch.html',context)

def list_xiaomi_watch(request):
    # Lọc các Type_ID là '3' (smart watch) lọc theo id XIAOMI = 3
    xiaomi_watch = Product.objects.filter(Type_ID= '3', Manufacture_ID= '3' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'xiaomi_watch':xiaomi_watch, 'current_user':current_user}
    return render(request , 'Guest_app/smart_watch/xiaomi/xiaomi_watch.html',context)

# list 4.TAI NGHE
def list_airpods(request): 
    # Lọc các Type_ID là '4' (TAI NGHE) và lọc theo id APPLE =1
    airpods = Product.objects.filter(Type_ID= '4' , Manufacture_ID= '1')
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'airpods':airpods, 'current_user':current_user}
    return render(request , 'Guest_app/head_phone/apple/aripods.html',context)

def list_samsung_headphone(request):
    # Lọc các Type_ID là '4'(TAI NGHE) và lọc theo id SAMSUNG =2
    ss_headphone = Product.objects.filter(Type_ID= '4', Manufacture_ID= '2')
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'ss_headphone':ss_headphone, 'current_user':current_user}
    return render(request , 'Guest_app/head_phone/samsung/samsung.html',context)

def list_xiaomi_headphone(request):
    # Lọc các Type_ID là '4' (headphone) và theo id XIAOMI = 3
    xiaomi_headphone = Product.objects.filter(Type_ID= '4', Manufacture_ID= '3' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'xiaomi_headphone':xiaomi_headphone,'current_user':current_user}
    return render(request , 'Guest_app/head_phone/xiaomi/xiaomi.html',context)

# List 5.TV
def list_samsungTV(request):
    # Lọc các Type_ID là '5' (Tivi) và lọc theo id SAMSUNG = 2
    samsung_tv = Product.objects.filter(Type_ID= '5', Manufacture_ID= '2' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'samsung_tv':samsung_tv,'current_user':current_user}
    return render(request , 'Guest_app/tivi/samsung/samsung.html',context)

def list_xiaomiTV(request):
    # Lọc các Type_ID là '5' (Tivi) và theo id XIAOMI = 3
    xiaomi_tv = Product.objects.filter(Type_ID= '5', Manufacture_ID= '3' )
    
    # thông tin tài khoản
    current_user = request.user
    
    context= {'xiaomi_tv':xiaomi_tv, 'current_user':current_user}
    return render(request , 'Guest_app/tivi/xiaomi/xiaomi.html',context)


# chi tiết sản phẩm + thêm vào giỏ hàng
# hàm chính để tái sử dụng
def detail_product(request, id, template_name, context_name ):
    # Truy vấn sản phẩm dựa trên ID
    product = Product.objects.filter(Product_ID=id)
    current_user = request.user

    if request.method == 'POST':
        # Lấy thông tin sản phẩm từ request.POST
        product_id = request.POST.get('product_id')
        qty = int(request.POST.get('quantity', 1))
        # Kiểm tra xem người dùng đã đăng nhập hay chưa
        if not current_user.is_authenticated:
            # Nếu chưa đăng nhập, chuyển hướng họ đến trang đăng nhập
            return redirect('login')
        
        # Kiểm tra xem sản phẩm đã tồn tại trong giỏ hàng chưa
        shopping_cart_item = Shopping_Cart.objects.filter(Product_ID_id=product_id, user=request.user).first()
        if shopping_cart_item:
            # Nếu sản phẩm đã tồn tại trong giỏ hàng, cập nhật số lượng bằng cách thêm số lượng mới vào số lượng hiện tại
            shopping_cart_item.Quantity += qty
            shopping_cart_item.save()
            
        else:
            # Tạo database Shopping_Cart từ request.POST
            shopping_cart_item = Shopping_Cart( Product_ID_id=product_id, Quantity=qty, user=request.user)
            shopping_cart_item.save()
            
        return redirect('shopping_cart')
    
    context = {context_name: product, 'current_user':current_user }
    return render(request, template_name, context)

# điện thoại
def detail_phone(request, id):
    return detail_product(request, id, 'Guest_app/dien_thoai/detail_phone.html', 'phone')
# laptop
def detail_laptop(request, id):
    return detail_product(request, id, 'Guest_app/laptop/detail_laptop.html', 'laptop')
# smart watch
def detail_smartwatch(request, id):
    return detail_product(request, id, 'Guest_app/smart_watch/detail_smartwatch.html', 'smart_watch')
# headphone
def detail_headphone(request, id):
    return detail_product(request, id, 'Guest_app/head_phone/detail_headphone.html', 'head_phone')
# tivi
def detail_TV(request, id):
    return detail_product(request, id, 'Guest_app/tivi/detail_TV.html', 'tivi')

# phải login mới vào được trang giỏ hàng
@login_required(login_url='login')
# hiển thị sản phẩm trong giỏ hàng
def shopping_cart(request):
    current_user = request.user  # Lấy thông tin người dùng hiện tại đã đăng nhập
    list_shopping_cart = Shopping_Cart.objects.filter(user=current_user)  # Lấy giỏ hàng của người dùng hiện tại
    
    # đếm số lượng sản phẩm trong giỏ
    count = 0
    for item in list_shopping_cart:
        count += item.Quantity
        
    context = {'list_shopping_cart': list_shopping_cart, 'current_user':current_user , 'count':count }
    return render(request, 'Guest_app/cart/shopping_cart.html', context)

# thay đổi số lượng
def edit_product(request, id):
    # lấy sản phẩm từ database theo ID để chỉnh sửa
    product_edit = Shopping_Cart.objects.get(id= id)
    
    if request.method == 'POST':
        qty = request.POST.get('edit_Quantity')
        # Kiểm tra xem sản phẩm có tồn tại trong giỏ hàng không
        if product_edit:
            # Thay đổi số lượng sản phẩm và lưu lại
            product_edit.Quantity = qty
            product_edit.save()
            return redirect('shopping_cart')
        else:
            # Xử lý trường hợp sản phẩm không tồn tại trong giỏ hàng
            pass
    
    context = {'product_edit': product_edit}
    return render(request, 'Guest_app/cart/shopping_cart.html', context)


# xóa khỏi giỏ hàng
def remove_product(request, id):
    # Truy vấn giỏ hàng bằng id của nó
    shopping_cart_item = Shopping_Cart.objects.get(id= id)
    # Xóa mục khỏi giỏ hàng
    shopping_cart_item.delete()
    return redirect('shopping_cart')

# thanh toán
def check_out(request):
    current_user = request.user  # Lấy thông tin người dùng hiện tại đã đăng nhập
    # Lấy tất cả các mục trong giỏ hàng của người dùng hiện tại
    checkout_items = Shopping_Cart.objects.filter(user=current_user)

    # Tính tổng giá trị cho tất cả các sản phẩm trong giỏ hàng
    total_price=0
    for item in checkout_items:
        total_price += (item.Quantity * item.Product_ID.Unit_Price)
    
    # Khởi tạo biến customer để lấy thông tin của id trong model Customer
    customer = None  
    # Xử lý form thông tin khách hàng
    if request.method == "POST":
        form_1 = CustomerForm(request.POST)
        if form_1.is_valid():  
            try:
                # Lưu thông tin khách hàng vào model Customer
                customer = form_1.save()

                # Tạo database của Order_Detail cho từng mục trong giỏ hàng
                for checkout_item in checkout_items:
                    order_detail = Order_Detail(
                        Order_ID_id = customer.id,
                        Product_ID_id = checkout_item.Product_ID.id,
                        Quantity_id = checkout_item.id,
                        Total_Price = checkout_item.Quantity * checkout_item.Product_ID.Unit_Price
                    )
                    order_detail.save()
                return redirect('checkout_detail', id=customer.id )
            except:  
                pass
    else:  
        form_1 = CustomerForm()
        
    context = { 'checkout_items': checkout_items, 'current_user': current_user, 'customer': customer, 'total_price': total_price,'form_1': form_1}
    return render(request, 'Guest_app/cart/check_out.html', context)

def checkout_detail(request,id) :
    # Lấy thông tin người dùng hiện tại đã đăng nhập
    current_user = request.user
    # thông tin khách hàng
    if_customer = Customer.objects.get(id=id)
    # thông tin Order_Detail
    od_detail = Order_Detail.objects.filter(Order_ID = id)

    context = {'current_user':current_user,'if_customer':if_customer,  'od_detail':od_detail}
    return render(request, 'Guest_app/cart/checkout_detail.html', context)
