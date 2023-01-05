from django.shortcuts import render
from store.models import Product, ReviewRating
from django.utils import translation
from django.utils.translation import gettext as _

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    html_language = translation.get_language()

    context = {
        'products': products,
        'reviews': reviews,
        'html_language': html_language,
    }
    return render(request, 'home.html', context)


def foo(request):
    
    html_language = translation.get_language()

    context = {
        'html_language': html_language,
    }
    return context