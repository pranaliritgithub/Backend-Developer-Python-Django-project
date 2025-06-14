from django import forms

# Furniture Form
class FurnitureForm(forms.Form):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    description = forms.CharField(widget=forms.Textarea, required=False)

# Order Form
class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    furniture_name = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')])
    date_created = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# Customer Form
class CreateCustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()
