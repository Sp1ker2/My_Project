from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Items(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["title"])]


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    logo = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    class Meta:
        indexes = [models.Index(fields=["email"])]


class Orders(models.Model):
    choices_for_order = {
        "Pending": "Pending",
        "Awaiting": "Awaiting",
        "Shipped": "Shipped",
        "Completed": "Completed",
        "Canceled": "Canceled",
    }
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey("pets.Users", on_delete=models.DO_NOTHING)


class FavouriteItems(models.Model):
    user_id = models.ForeignKey("pets.Users", on_delete=models.DO_NOTHING)
    item_id = models.ForeignKey("pets.Items", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("user_id", "item_id")


class ItemsOrders(models.Model):
    item_id = models.ForeignKey("pets.Items", on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey("pets.Orders", on_delete=models.CASCADE)
    quantity = models.IntegerField()


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
