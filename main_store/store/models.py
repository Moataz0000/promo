from django.db import models
from django.urls import reverse
from django.conf import settings





class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True , max_length=250)
    image = models.ImageField(upload_to='category/%Y/%m/%d' , blank=True)


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

        verbose_name = 'category'
        verbose_name_plural = 'Categories'



    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("store:product_by_category", args=[self.slug])
    
    




class Product(models.Model):

    class Status(models.TextChoices):
        ProductOffers = 'PO','ProductOffers'
        Regularproduct = 'RP ,Regularproduct'
        
    category = models.ForeignKey(Category , related_name="products" , on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='seller',on_delete=models.CASCADE , null=True)
    slug = models.SlugField(unique=True , max_length=250)
    image = models.ImageField(upload_to='products/%Y/%m/%d' , blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20 , choices=Status.choices , default=Status.Regularproduct)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    old_price = models.DecimalField(max_digits=10 , decimal_places=2)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id' , 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])
    




class Comments(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField(blank=True , null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comments"


    def __str__(self):
        return f'{self.name} By {self.product}'

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]   

    def __str__(self):
        return f'Comment by {self.name} on {self.product}'    

























class VariationManager(models.Manager):
    # Just get color    
    def get_color(self):
        return super(VariationManager , self).filter(Variation_category='color' , is_active=True)
    # just get size
    def get_size(self):
        return super(VariationManager , self).filter(Variation_category='size' , is_active=True)


Variation_category_choices =(
    ('color' , 'color'),
    ('size' , 'size'),
)




class Variation(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    Variation_category = models.CharField(max_length=100 , choices=Variation_category_choices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now=True)
    
    objects = VariationManager()

















# class Comment(models.Model):
#     product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='comments')
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['created']
#         indexes = [
#             models.Index(fields=['created'])
#         ]

#     def __str__(self):
#         return f'Comment by {self.name} on {self.product}'     
