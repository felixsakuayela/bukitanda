import re
from django.shortcuts import render
from store.models import  Product, VariationManager,  Variation, ReviewRating, ProductGallery
from category.models import Category
from manager.forms import CategoryForm, ProductForm, ProductGalleryForm, VariationForm, ReviewRatingForm


def category(request):  
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            slug = form.cleaned_data['slug']
            description = form.cleaned_data['description']
            cat_image = form.cleaned_data['cat_image']
            category = Category.objects.create(category_name=category_name, slug=slug, description=description, cat_image=cat_image,)
            category.save()
    else:
        form = CategoryForm()
    context = {'form': form,}
    return render(request, 'manager/category.html', context)

def product(request):  
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            slug = form.cleaned_data['slug']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            images = form.cleaned_data['images']
            stock = form.cleaned_data['stock']
            is_available = form.cleaned_data['is_available']
            category = form.cleaned_data['category']
            product = Product.objects.create(product_name=product_name, slug=slug, description=description, price=price, images=images, stock=stock, is_available=is_available, category=category)
            product.save()
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'manager/product.html', context)