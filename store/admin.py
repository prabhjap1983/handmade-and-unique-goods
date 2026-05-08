from django.contrib import admin
from .models import Category, Customer, Product, Order,ContactUs, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ContactUs)
admin.site.register(Profile)


# Mix profile info and user info
class ProfileInline(admin.StackedInline):
    model = Profile

# extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username","first_name","lastname","email"]
    inlines = [ProfileInline]

# Unregister the old way 
admin.site.unregister(User)

# Re-Register the new way 
admin.site.register(User, UserAdmin)
