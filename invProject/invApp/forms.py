from django import forms 
from .models import Product 

class ProductForm(forms.ModelForm) : 
    class Meta : 
        model = Product
        fields = '__all__' 
        labels = { 
                  'product_id': 'Product ID' , 
                  'name': 'Name' , 
                  'sku': 'Product ID', 
                  'price': 'Price', 
                  'quantity': 'Quantity',
                  'supplier': 'Supplier' ,  
                  
                  
                 }
        widgets = {
            'product_id' : forms.NumberInput(attrs={'placeholder':'shirt','class':'form-control'}) , 
            'name' : forms.TextInput(attrs={'placeholder':'John','class':'form-control'}) , 
            'sku' : forms.TextInput(attrs={'placeholder':'W1233','class':'form-control'}) , 
            'price' : forms.NumberInput(attrs={'placeholder':'9000','class':'form-control'}) , 
            'quantity' : forms.NumberInput(attrs={'placeholder':'4,5 etc.','class':'form-control'}) , 
            'supplier' : forms.TextInput(attrs={'placeholder':'shirt','class':'form-control'}) , 
            
            
             
                   }