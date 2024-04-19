from django.contrib import admin
from .models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    list_display_links = ['name']
    prepopulated_fields = {'slug':('name',)}





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' ,'status', 'category' , 'stock' , 'price' , 'available' , 'created' , 'updated']
    list_filter = ['created'  ,'available' , 'updated']
    list_editable = ['price' , 'available']
    prepopulated_fields = {'slug':('name',)}



@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product' , 'Variation_category' , 'variation_value' , 'is_active' , 'created_date']
    list_filter =  ['product' , 'Variation_category' , 'variation_value' , 'is_active' , 'created_date']
    list_display_links =  ['product' , 'Variation_category' , 'variation_value' , 'is_active' , 'created_date']
 



@admin.register(Comments)
class CommetnAdmin(admin.ModelAdmin):
    list_display = ['name' , 'active' ,'content', 'created']
    list_filter =  ['created' , 'updated']
    search_fields = ['name']
 





