from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category( models.Model ):
    name = models.CharField(max_length=200) 

class Subcategory( models.Model ):  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Product( models.Model ):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()


class Order( models.Model ):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    
''' 
500Table => 50,000 Rows category (1) 50,000 -> bulk update  Transaction ()
subactegories
name | name => X
ACID Property Hamper (ACID)

categories
(PK) -> Key table 1 time, repeat X , 3 X -> 3 (PK)
id | name          | seller
1  | ABC => (GEH)  | s1
2  | XYZ           | s2
3  | CDF           | s3


Subcategories
FK ( 2nd table PK, 2 tables )
category_id | subcategory_name
3          |     A                   
1           |     B
2           |     A1
3           |     A2

Products
category_id | subcategory_name  | Product_name
1           |     A             |      P1
1           |     B             |      P2
2           |     A1            |      P3
3           |     A2            |      P4
'''