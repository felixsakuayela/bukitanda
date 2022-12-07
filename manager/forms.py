from django import forms
from store.models import  Product, VariationManager,  Variation, ReviewRating, ProductGallery
from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'slug', 'description', 'cat_image']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'slug', 'description', 'price', 'images', 'stock', 'is_available', 'category',]

class VariationForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = ['product', 'variation_category', 'variation_value', 'is_active']

class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['product', 'user', 'subject', 'review', 'rating', 'ip', 'status']

class ProductGalleryForm(forms.ModelForm):
    class Meta:
        model = ProductGallery
        fields = ['product', 'image',]

