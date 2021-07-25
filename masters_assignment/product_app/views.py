from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import ProductForm
from django.views import View

from .models import *
# Create your views here.


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            "products" : products,
            "form": ProductForm()
        }
        return render(request, 'product_app/index.html', context)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("home"))


def index(request):
    products = Product.objects.all()
    context = {
        "products" : products,
        "form": ProductForm()
    }
    return render(request, 'product_app/index.html', context)

def get_all_categories(request):
    categories = Category.objects.values_list("name")
    response = []
    for cat in categories:
        response.append(cat[0])
    return JsonResponse(response, safe=False)

def get_all_subcategories(request, slug):
    response = []
    try:
        category = Category.objects.get(slug=slug)
        sub_categories = SubCategory.objects.filter(category=category).values_list("name")
        for cat in sub_categories:
            response.append(cat[0])
    except:
        pass
    return JsonResponse(response, safe=False)

def get_product_from_category(request, slug):
    # import pdb; pdb.set_trace()
    response = []
    try:
        category = Category.objects.get(slug=slug)
        sub_categories = SubCategory.objects.filter(category=category)
        for sc in sub_categories:
            products = Product.objects.filter(sub_category=sc).values_list("name")
            for prod in products:
                response.append(prod[0])
    except:
        raise Http404("Category does not exist")
    return JsonResponse(response, safe=False)

def get_product_from_subcategory(request, slug):
    response = []
    try:
        sub_category = get_object_or_404(SubCategory, slug=slug) 
        products = Product.objects.filter(sub_category=sub_category).values_list("name")
        for prod in products:
            response.append(prod[0])
    except:
        raise Http404("Sub Category does not exist")
    return JsonResponse(response, safe=False)