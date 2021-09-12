from django.db import models


from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )
    image = models.ImageField(upload_to='products/')
    zip=models.FileField(upload_to="products/")

    class Meta:
        ordering = ('-name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'listings:product_list_by_category',
            args=[self.slug]
        )

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name = 'products',
        on_delete = models.CASCADE
    )

    name = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(
        max_length=100,
        unique=False,null=True,blank=True)
    image = models.ImageField(upload_to='products/')
    
 
    
    #class Meta:
        #ordering = ('shu',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'listings:product_detail',
            args=[self.category.slug, self.slug]
        )

    def get_average_review_score(self):
        average_score = 0.0
        if self.reviews.count() > 0:
            total_score = sum([review.rating for review in self.reviews.all()])
            average_score = total_score / self.reviews.count()
        return round(average_score, 1)

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=50)
        
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
