from django.db import models
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField

STATUS = (
    ('Received', 'Received'),
    ('Processed', 'Processed'),
    ('Sent', 'Sent'),
    ('Delivered', 'Delivered'),
    ('Rejected', 'Rejected'),
)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    cc_number = CardNumberField()
    cc_expiry = CardExpiryField()
    cc_code = SecurityCodeField()
    
    class Meta:
        verbose_name_plural = 'Payment Methods'
    
    def __str__(self):
        return f'{self.id}'

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'

class Contract(models.Model):

    notes = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='Contracts', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return f'Contract-{self.date}'

class Shipment(models.Model):

    notes = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to='Contracts', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Shipments'

    def __str__(self):
        return f'Shipment-{self.date}'


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return f'{self.name}'

class Series(models.Model):
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    barcode = models.ImageField(upload_to='Barcodes', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return f'{self.id}-{self.date}'

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='Products', null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}-{self.series.vendor.name}-{self.quantity}'


class OrderClient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Clients'
    def __str__(self):
        return f'{self.firstname} {self.lastname}-{self.id}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, null=True, blank=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=True, blank=True)
    order_quantity = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(OrderClient, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.product} - order by {self.employee.username}'