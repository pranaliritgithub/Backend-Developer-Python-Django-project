# from django.shortcuts import render, redirect
# from .manage import OrderForm, FurnitureForm, CreateCustomerForm
# from django.forms import inlineformset_factory
# from .models import *

# # Create your views here.
# def home(request):
#     furniture = Furniture.objects.all()
#     customers = Customer.objects.all()
#     orders = Order.objects.all()
#     delivered = orders.filter(status='Delivered').count()

#     context = {
#         'furniture': furniture, 'customers': customers, 'orders': orders, 'delivered': delivered
#     }

#     return render(request, 'store/home.html', context)

# def manage(request):
#     furniture = Furniture.objects.all()
#     customers = Customer.objects.all()
#     orders = Order.objects.all()
#     delivered = orders.filter(status='Delivered').count()
#     pending = orders.filter(status='Pending').count()

#     context = {
#         'furniture':furniture, 'customers':customers, 'orders': orders,
#         'delivered':delivered, 'pending':pending
#     }

#     return render(request, 'store/manage.html', context)

# def furniture(request):
#     furniture = Furniture.objects.all()
#     customers = Customer.objects.all()
#     orders = Order.objects.all()
#     delivered = orders.filter(status='Delivered').count()
#     pending = orders.filter(status='Pending').count()

#     context = {
#         'furniture':furniture, 'customers':customers, 'orders': orders, 'delivered':delivered, 'pending':pending
#     }

#     return render(request, 'store/furniture.html', context)

# def contact(request):
#     return render(request, 'store/contact.html')


# def update_furniture(request, name):
#     furniture = Furniture.objects.get(name=name)
#     form = FurnitureForm(instance=furniture)
#     if request.method == 'POST':
#         form = FurnitureForm(request.POST, instance=furniture)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request,'store/order_form.html', context)

# def delete_furniture(request, name):
#     furniture = Furniture.objects.get(name=name)
#     if request.method == 'POST':
#         furniture.delete()
#         return redirect('/')
#     context = {'item': furniture}
#     return render(request, 'store/delete.html',context)


# def update_order(request, pk):
#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)
#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request,'store/order_form.html', context)


# def delete_order(request, pk):
#     order = Order.objects.get(id=pk)
#     if request.method == 'POST':
#         order.delete()
#         return redirect('/')
#     context = {'item': order}
#     return render(request, 'store/delete.html',context)

# def create_customer(request):
#     form = CreateCustomerForm()
#     if request.method == 'POST':
#         form = CreateCustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form': form}
#     return render(request, 'store/create_customer.html', context)


# def create_furniture(request):
#     form = FurnitureForm()
#     if request.method == 'POST':
#         form = FurnitureForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request, 'store/create_customer.html',context)

# #do it same as add furniture
# def create_order(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request, 'store/create_order.html',context)


# from django.shortcuts import render, redirect
# # from .forms_mongo import OrderForm, FurnitureForm, CreateCustomerForm
# from .forms_mongo import FurnitureForm, OrderForm, CreateCustomerForm

# from bson.objectid import ObjectId
# from .models import furniture_collection, customer_collection, order_collection

# # Home page
# def home(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#     }
#     return render(request, 'store/home.html', context)

# # Dashboard
# def manage(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')
#     pending = sum(1 for o in orders if o['status'] == 'Pending')

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#         'pending': pending,
#     }
#     return render(request, 'store/manage.html', context)

# # Furniture list
# def furniture(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')
#     pending = sum(1 for o in orders if o['status'] == 'Pending')

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#         'pending': pending,
#     }
#     return render(request, 'store/furniture.html', context)

# def contact(request):
#     return render(request, 'store/contact.html')

# # Create Furniture
# #create_furniture are changed to FurnitureForm
# def create_furniture(request):
#     form = FurnitureForm()
#     if request.method == 'POST':
#         form = FurnitureForm(request.POST)
#         if form.is_valid():
#             furniture_collection.insert_one(form.cleaned_data)
#             return redirect('/')
#     return render(request, 'store/create_customer.html', {'form': form})

# # Update Furniture
# def update_furniture(request, id):
#     furniture_item = furniture_collection.find_one({'_id': ObjectId(id)})
#     form = FurnitureForm(initial=furniture_item)
#     if request.method == 'POST':
#         form = FurnitureForm(request.POST)
#         if form.is_valid():
#             furniture_collection.update_one(
#                 {'_id': ObjectId(id)},
#                 {'$set': form.cleaned_data}
#             )
#             return redirect('/')
#     return render(request, 'store/order_form.html', {'form': form})

# # Delete Furniture
# def delete_furniture(request, id):
#     furniture_item = furniture_collection.find_one({'_id': ObjectId(id)})
#     if request.method == 'POST':
#         furniture_collection.delete_one({'_id': ObjectId(id)})
#         return redirect('/')
#     return render(request, 'store/delete.html', {'item': furniture_item})

# # Create Customer
# def create_customer(request):
#     form = CreateCustomerForm()
#     if request.method == 'POST':
#         form = CreateCustomerForm(request.POST)
#         if form.is_valid():
#             customer_collection.insert_one(form.cleaned_data)
#             return redirect('/')
#     return render(request, 'store/create_customer.html', {'form': form})

# # Create Order
# def create_order(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order_collection.insert_one(form.cleaned_data)
#             return redirect('/')
#     return render(request, 'store/create_order.html', {'form': form})

# # Update Order
# def update_order(request, id):
#     order = order_collection.find_one({'_id': ObjectId(id)})
#     form = OrderForm(initial=order)
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order_collection.update_one(
#                 {'_id': ObjectId(id)},
#                 {'$set': form.cleaned_data}
#             )
#             return redirect('/')
#     return render(request, 'store/order_form.html', {'form': form})

# # Delete Order
# def delete_order(request, id):
#     order = order_collection.find_one({'_id': ObjectId(id)})
#     if request.method == 'POST':
#         order_collection.delete_one({'_id': ObjectId(id)})
#         return redirect('/')
#     return render(request, 'store/delete.html', {'item': order})

from django.shortcuts import render, redirect
from .forms_mongo import FurnitureForm, OrderForm, CreateCustomerForm
from bson.objectid import ObjectId
from bson.objectid import ObjectId, InvalidId
from decimal import Decimal
from .models import furniture_collection, customer_collection, order_collection
from bson.errors import InvalidId
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
import datetime
# from .mongo import furniture_collection  # make sure this import is correct


# Home page
# def home(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#     }
#     return render(request, 'store/home.html', context)

def home(request):
    furniture = list(furniture_collection.find())
    customers = list(customer_collection.find())
    orders = list(order_collection.find())
    delivered = sum(1 for o in orders if o['status'] == 'Delivered')

    # Convert ObjectId to string and assign to 'id' key
    for item in furniture:
        item['id'] = str(item['_id'])
    for item in customers:
        item['id'] = str(item['_id'])
    for item in orders:
        item['id'] = str(item['_id'])

    context = {
        'furniture': furniture,
        'customers': customers,
        'orders': orders,
        'delivered': delivered,
    }
    return render(request, 'store/home.html', context)


# Dashboard
# def manage(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')
#     pending = sum(1 for o in orders if o['status'] == 'Pending')

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#         'pending': pending,
#     }
#     return render(request, 'store/manage.html', context)

def manage(request):
    furniture = list(furniture_collection.find())
    customers = list(customer_collection.find())
    orders = list(order_collection.find())
    delivered = sum(1 for o in orders if o['status'] == 'Delivered')
    pending = sum(1 for o in orders if o['status'] == 'Pending')

    # Convert ObjectId to string using a new 'id' key
    for item in furniture:
        item['id'] = str(item['_id'])
    for item in customers:
        item['id'] = str(item['_id'])
    for item in orders:
        item['id'] = str(item['_id'])

    context = {
        'furniture': furniture,
        'customers': customers,
        'orders': orders,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request, 'store/manage.html', context)



# Furniture list
# def furniture(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')
#     pending = sum(1 for o in orders if o['status'] == 'Pending')

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#         'pending': pending,
#     }
#     return render(request, 'store/furniture.html', context)

# def contact(request):
#     return render(request, 'store/contact.html')

# def furniture(request):
#     furniture = list(furniture_collection.find())
#     customers = list(customer_collection.find())
#     orders = list(order_collection.find())
#     delivered = sum(1 for o in orders if o['status'] == 'Delivered')
#     pending = sum(1 for o in orders if o['status'] == 'Pending')

#     # Replace '_id' with 'id' for template use
#     for item in furniture:
#         item['id'] = str(item['_id'])
#     for item in customers:
#         item['id'] = str(item['_id'])
#     for item in orders:
#         item['id'] = str(item['_id'])

#     context = {
#         'furniture': furniture,
#         'customers': customers,
#         'orders': orders,
#         'delivered': delivered,
#         'pending': pending,
#     }
#     return render(request, 'store/furniture.html', context)

def furniture(request):
    # Fetch data from MongoDB
    furniture = list(furniture_collection.find())
    customers = list(customer_collection.find())
    orders = list(order_collection.find())

    # Convert MongoDB ObjectIds to string for template use
    for item in furniture:
        item['id'] = str(item['_id'])

    for item in customers:
        item['id'] = str(item['_id'])

    for item in orders:
        item['id'] = str(item['_id'])

    # Calculate order stats
    delivered = sum(1 for o in orders if o.get('status') == 'Delivered')
    pending = sum(1 for o in orders if o.get('status') == 'Pending')

    # Send context to template
    context = {
        'furniture': furniture,
        'customers': customers,
        'orders': orders,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request, 'store/furniture.html', context)


# Create Furniture
def create_furniture(request):
    form = FurnitureForm()
    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for k, v in data.items():
                if isinstance(v, Decimal):
                    data[k] = float(v)
            furniture_collection.insert_one(data)
            return redirect('/')
    return render(request, 'store/create_customer.html', {'form': form})

# Update Furniture
# def update_furniture(request, id):
#     furniture_item = furniture_collection.find_one({'_id': ObjectId(id)})
#     form = FurnitureForm(initial=furniture_item)
#     if request.method == 'POST':
#         form = FurnitureForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             for k, v in data.items():
#                 if isinstance(v, Decimal):
#                     data[k] = float(v)
#             furniture_collection.update_one(
#                 {'_id': ObjectId(id)},
#                 {'$set': data}
#             )
#             return redirect('/')
#     return render(request, 'store/order_form.html', {'form': form})

# def update_furniture(request, id):
#     try:
#         object_id = ObjectId(id)
#     except InvalidId:
#         return HttpResponseBadRequest("Invalid ID format")

#     furniture = furniture_collection.find_one({'_id': object_id})
#     if not furniture:
#         return HttpResponseBadRequest("Furniture not found")

#     if request.method == 'POST':
#         form = FurnitureForm(request.POST)
#         if form.is_valid():
#             furniture_collection.update_one(
#                 {'_id': object_id},
#                 {'$set': form.cleaned_data}
#             )
#             return redirect('/')
#     else:
#         form = FurnitureForm(initial=furniture)

#     return render(request, 'store/update_furniture.html', {'form': form})

def update_furniture(request, id):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return HttpResponseBadRequest("Invalid ID format")

    furniture = furniture_collection.find_one({'_id': object_id})
    if not furniture:
        return HttpResponseBadRequest("Furniture not found")

    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # 👇 Convert Decimal price to float (MongoDB safe)
            if isinstance(data.get('price'), Decimal):
                data['price'] = float(data['price'])

            furniture_collection.update_one(
                {'_id': object_id},
                {'$set': data}
            )
            return redirect('/')
    else:
        form = FurnitureForm(initial=furniture)

    return render(request, 'store/update_furniture.html', {'form': form})


# Delete Furniture
# def delete_furniture(request, id):
#     furniture_item = furniture_collection.find_one({'_id': ObjectId(id)})
#     if request.method == 'POST':
#         furniture_collection.delete_one({'_id': ObjectId(id)})
#         return redirect('/')
#     return render(request, 'store/delete.html', {'item': furniture_item})

# def delete_furniture(request, id):
#     try:
#         object_id = ObjectId(id)
#     except InvalidId:
#         return render(request, 'store/error.html', {'error': 'Invalid furniture ID.'})

#     furniture_item = furniture_collection.find_one({'_id': object_id})
#     if request.method == 'POST':
#         furniture_collection.delete_one({'_id': object_id})
#         return redirect('/')
#     return render(request, 'store/delete.html', {'item': furniture_item})

def delete_furniture(request, id):
    try:
        object_id = ObjectId(id)
    except InvalidId:
        return render(request, 'store/error.html', {'error': 'Invalid furniture ID.'})

    item = furniture_collection.find_one({'_id': object_id})
    if item:
        item['id'] = str(item['_id'])  # this makes it usable in template
    else:
        return render(request, 'store/error.html', {'error': 'Furniture item not found.'})

    if request.method == 'POST':
        furniture_collection.delete_one({'_id': object_id})
        return redirect('/')

    return render(request, 'store/delete.html', {'item': item})


# Create Customer
def create_customer(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for k, v in data.items():
                if isinstance(v, Decimal):
                    data[k] = float(v)
            customer_collection.insert_one(data)
            return redirect('/')
    return render(request, 'store/create_customer.html', {'form': form})

# Create Order
# def create_order(request):
#     form = OrderForm()
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             for k, v in data.items():
#                 if isinstance(v, Decimal):
#                     data[k] = float(v)
#             order_collection.insert_one(data)
#             return redirect('/')
#     return render(request, 'store/create_order.html', {'form': form})

def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Convert Decimal to float and date to datetime
            for k, v in data.items():
                if isinstance(v, Decimal):
                    data[k] = float(v)
                elif isinstance(v, datetime.date):
                    data[k] = datetime.datetime.combine(v, datetime.datetime.min.time())

            order_collection.insert_one(data)
            return redirect('/')
    return render(request, 'store/create_order.html', {'form': form})

# Update Order
def update_order(request, id):
    order = order_collection.find_one({'_id': ObjectId(id)})
    form = OrderForm(initial=order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            for k, v in data.items():
                if isinstance(v, Decimal):
                    data[k] = float(v)
            order_collection.update_one(
                {'_id': ObjectId(id)},
                {'$set': data}
            )
            return redirect('/')
    return render(request, 'store/order_form.html', {'form': form})

# Delete Order
# def delete_order(request, id):
#     order = order_collection.find_one({'_id': ObjectId(id)})
#     if request.method == 'POST':
#         order_collection.delete_one({'_id': ObjectId(id)})
#         return redirect('/')
#     return render(request, 'store/delete.html', {'item': order})

def delete_order(request, id):
    # 1. Find order by ObjectId
    order = order_collection.find_one({'_id': ObjectId(id)})

    # 2. If not found, redirect to home (or show error)
    if not order:
        return redirect('/')

    # 3. ✅ Add this line: convert _id to string
    order['id'] = str(order['_id'])

    # 4. If user confirms deletion
    if request.method == 'POST':
        order_collection.delete_one({'_id': ObjectId(id)})
        return redirect('/')

    # 5. Render confirmation template
    return render(request, 'store/delete.html', {'item': order})

# def contact(request):
#     return render(request, 'store/contact.html') 

def contact(request):
    if request.method == 'POST':
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'subject': request.POST.get('subject'),
            'message': request.POST.get('message'),
        }
        print("Received Contact Form Data:", data)  # Optional: for debugging
        return HttpResponse("Thanks for contacting us!")
    return render(request, 'store/contact.html')