# import operator
# from functools import reduce

from django.db.models import Q
from django.shortcuts import render
from shopapp.models import Product


# Create your views here.

def search_result(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        # q_list = [Q(name__contains=query), Q(description__contains=)]
        # Product.objects.filter(reduce(operator.or_, q_list))
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
