from django.contrib import admin
from .models import Coupon,Order,OrderProduct

# Register your models here.
admin.site.register(Coupon)

class OrderedProductsInline(admin.TabularInline):
    model=OrderProduct
    readonly_fields=['title','count','price','size']
    extra=0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderedProductsInline]