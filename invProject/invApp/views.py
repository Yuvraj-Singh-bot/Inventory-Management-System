from django.shortcuts import render,redirect
from .models import Product 
from .forms import ProductForm 

#CRUD : - CREATE,READ,UPDATE,DELETE

#Home View 

def home_view(request) : 
    return render(request,'invApp/home.html') 


#Create View 

def create_product_view(request) : 
    form = ProductForm() 
    
    if request.method == 'POST' : 
        form = ProductForm(request.POST) 
        
        if form.is_valid() : 
            form.save() 
            return redirect('product_list') 
        
    return render(request,'invApp/product_form.html',{'form' : form})

#Read View 

def product_list_view(request) : 
    products = Product.objects.all() 
    context = {'products' : products}
    return render(request,'invApp/product_list.html' , context) 
 

#Update View 

def product_update_view(request,product_id) : 
    product = Product.objects.get(product_id=product_id) 
    form = ProductForm() 
    
    if request.method == 'POST' : 
        form = ProductForm(request.POST,instance= product) 
        if form.is_valid() : 
            form.save() 
            return redirect("product_list") 
        
    return render(request,'invApp/product_form.html',{'form' : form})


#Delete View 

def product_delete_view(request,product_id) : 
    product = Product.objects.get(product_id=product_id)
    
    if request.method == 'POST' : 
        product.delete() 
        return redirect('product_list')  
    
    return render(request, "invApp/prodcut_delete_confirm.html" ,{"product" : product }) 
 


      
        
    
    
    
        
    


         
    

