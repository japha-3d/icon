from django.contrib import admin
from .models import Category,Product,Review,Contact

class OrderReviewInline(admin.TabularInline):
    model = Review
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepopulated_fields={'slug':('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('category','name')

admin.site.register(Contact)



