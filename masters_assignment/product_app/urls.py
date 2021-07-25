from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',views.IndexView.as_view(),name="home"),
    path('categories/', views.get_all_categories, name="get_all_categories"),
    path("categories/<slug:slug>", views.get_all_subcategories, name="get_subcategories"),
    path("products/category/<slug:slug>", views.get_product_from_category, name="get_product_from_category"),
    path("products/sub_category/<slug:slug>", views.get_product_from_subcategory, name="get_product_from_subcategory")
]