from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)

    # ✅ Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)   # set when created
    updated_at = models.DateTimeField(auto_now=True)       # set when updated

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} - {self.product.name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    items = models.TextField()  # simple JSON string of items for demo
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.name}"

    class Meta:
        ordering = ['-created_at']  # latest first


class SupportQuery(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Support - {self.email}"

    class Meta:
        verbose_name_plural = "Support Queries"
