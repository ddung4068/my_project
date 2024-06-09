from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Type(models.Model):
    Type_ID = models.IntegerField(null=True, blank=True)
    Type_Name = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Types'
        
    def __str__(self):
        return str(self.Type_Name)
    
# Create your models here.
class Manufacture(models.Model):
    Manufacture_ID = models.IntegerField(null=True, blank=True)
    Manufacture_Name = models.CharField(max_length = 150, default= "")

    class Meta:
        db_table = 'Manufactures'
        
    def __str__(self):
        return str(self.Manufacture_Name)
    

    
# Create your models here.   
class Product(models.Model):
    Type_ID = models.ForeignKey(Type, on_delete = models.CASCADE)  # khóa ngoài với Type
    Manufacture_ID = models.ForeignKey(Manufacture, on_delete = models.CASCADE)   #khóa ngoài với Manufacture
    Product_ID = models.IntegerField(null=True, blank=True)
    Product_Img = models.ImageField(null=True, blank=True, upload_to="image_product/")
    Product_Name = models.CharField(max_length = 150, default= "")
    Configuration = models.CharField(max_length = 150, default= "")
    Description= models.TextField(default= "")
    Battery = models.CharField(max_length = 150, default= "")
    Unit_Price = models.IntegerField(null=True, blank=True)
    Warranty = models.CharField(max_length = 150, default= "")
    Other = models.CharField(max_length = 150, default= "")
     
    class Meta:
        db_table = 'Products'
        
    def __str__(self):
        return str(self.Product_Name)
    
# Create your models here.
class Shopping_Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # khóa ngoài với User của authtication
    Product_ID= models.ForeignKey(Product, on_delete = models.CASCADE) #khóa ngoài với Product
    Quantity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'Shopping_Cart'
        
    def __str__(self):
        return str(self.Quantity)

# Create your models here.
class Customer(models.Model):
    Cust_Name = models.CharField(max_length = 150, default= "")
    Cust_Adress = models.CharField(max_length = 150, default= "")
    Cust_Phone = models.CharField(max_length = 150, default= "")
    Cust_Email = models.EmailField(max_length = 150, default= "")
    
    class Meta:
        db_table = 'Customer'
        
    def __str__(self):
        return str(self.Cust_Name)
       
# Create your models here.
class Order_Detail(models.Model):
    Order_ID = models.ForeignKey(Customer, on_delete = models.CASCADE)         #khóa ngoài với Customer
    Product_ID = models.ForeignKey(Product, on_delete = models.CASCADE)          #khóa ngoài với Product
    Quantity = models.ForeignKey(Shopping_Cart, on_delete = models.CASCADE)      #khóa ngoài với Shopping_Cart
    Total_Price = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'Order_Details'
        
    def __str__(self):
        return str(self.Total_Price)


