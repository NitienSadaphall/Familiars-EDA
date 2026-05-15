# EDA Project

# Step 1 - Import Libraries
import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import date

# Initialize Faker from generating fake data
fake=Faker()

# Step 2 : Define Base Lists

categories = {

    'Mens':['Jeans','Trousers','T-shirts','Shirts','Jackets','innerwears'],
    'Womens':['Jeans','Jeggings','Top"s','Shirts','Jackets','InnerWears'],
    'Kids_Boys':['Jeans','Tshirts','Shorts','Shirts','Jackets','Innerwears'],
    'Kids_Girls':['Jeans','Jeggings','Skirts','Tops','Shirts','Innerwears']

}

regions = ['Urban','Rural']
payment_modes = ['Cash','Credit_Card','UPI','Net_Banking']
delivery_status = ['Delivered','Pending','Returned','Cancelled']
customer_segments = ['locals','Tourists','Discount_Customers']

# step 3 : Generate Dataset

records = []  # Empty List To Store all rows

for i in range(1000): # 1000 orders
    order_id = f'ORD{1000+i}'
    order_date = fake.date_between(start_date='-3y',end_date=date(2024, 12, 31))
    ship_date = order_date + pd.Timedelta(days=random.randint(1,7))

    names = ["Amit Sharma","Rajesh Patil","Suresh Kumar","Vijay Singh","Rohit Deshmukh","Nitin Jadhav","Prakash More",
    "Sunil Pawar","Manoj Shinde","Deepak Joshi","Ajay Kulkarni","Santosh Chavan","Mahesh Gaikwad","Rakesh Yadav",
    "Vinod Mishra","Anil Verma","Kiran Salunkhe","Sachin Wagh","Ganesh Kale","Pankaj Thakur","Priya Sharma",
    "Sneha Patil","Pooja Deshmukh","Neha Jadhav","Aarti Kulkarni","Kavita Joshi","Swati More","Anjali Pawar",
    "Deepali Shinde","Sonali Chavan","Meena Gaikwad","Ritu Yadav","Komal Verma","Jyoti Mishra","Vaishali Salunkhe",
    "Shweta Wagh","Nikita Kale","Rani Thakur","Bhavna Singh","Sakshi Patil"]

    customer_name = random.choice(names)
    customer_id = f'CUST{random.randint(100,999)}'
    customer_segment = random.choice(customer_segments)
    supplier_names = ["Patil Garments Pvt Ltd","Shree Fashion Hub","Deshmukh Textiles","Maharashtra Clothing Suppliers","Sai Apparels","Om Sai Garments",
                    "Pune Textile House","Shivshakti Fashions","Royal Ethnic Wear","Ganesh Garment Suppliers","Jadhav Fashion World","Krishna Apparels",
                    "Modern Textile Traders","Vardhaman Clothing House","Sunrise Garments","Elite Fashion Suppliers","Shree Balaji Textiles","Vinayak Apparels","Classic Wear India","Pawan Garment House"]

    category = random.choice(list(categories.keys()))
    product_name = random.choice(categories[category])
    product_id = f'PROD{random.randint(1000,9999)}'

    region = random.choice(regions)
    villages = ["Nere","Marunji","Dattawadi","Maan","Hinjewadi","kasarsai"]
    city = ['Pune','Pimpri','Chinchwad']
    city = random.choice(city)
    village = random.choice(villages)

    quantity = random.randint(1,10)
    unit_price = random.randint(100,5000)
    discount = random.choice ([0,5,10,15,20])

    sales_amount = quantity * unit_price *(1 - discount / 100)
    cost_price = sales_amount * random.uniform(0.6,0.9)
    profit = sales_amount - cost_price

    stock_left = random.randint(0,50)

    if stock_left < 10 :
        auto_reorder = 'Yes'
        reorder_quantity = random.randint(20,50)
    else :
        auto_reorder = "No"
        reorder_quantity = 0

    supplier_name = random.choice(supplier_names)
    supplier_email = (supplier_name.lower().replace(" ", "").replace("pvtltd", "").replace(".", "")+ "@gmail.com")
    payment_mode =random.choice(payment_modes)
    delivery = random.choice(delivery_status)

    # append row as dictionary

    records.append({
        'Order ID': order_id,
        'Order Date':order_date,
        'Ship Date':ship_date,
        'Customer ID':customer_id,
        'Customer Name':customer_name,
        'Customer Segment':customer_segment,
        'Product ID':product_id,
        'Product Name':product_name,
        'Category':category,
        'Region':region,
        'City':city,
        'Village':village,
        'Quanity':quantity,
        'Unit Price':unit_price,
        'Discount (%)':discount,
        'Sales Amount':round(sales_amount,2),
        'Cost Price':round(cost_price,2),
        'Profit':round(profit,2),
        'Payment Mode':payment_mode,
        'Delivery Status':delivery,
        'Supplier Name':supplier_name,
        'Supplier Email':supplier_email,
        'Stock_Left':stock_left,
        'Auto Reorder':auto_reorder,
        'Reorder Quantity':reorder_quantity

        })
    
# Step 4 : Create Database & Save to CSV

df = pd.DataFrame(records)
try:
    df.to_csv('Familiars_Clothing_Database.csv', index=False)
    print(' ✔ Database Generated successfully ! File Saved as "Familiars_Clothing_Database.csv" ')
except PermissionError:
    print('⚠ please close the file "Familiars_Clothing_Database.csv" if it is open in Excel or Power BI')
     