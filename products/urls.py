from django.urls import path

from products.views import ProductsListViews, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', ProductsListViews.as_view(), name='index'),
    path('category/<int:category_id>', ProductsListViews.as_view(), name='category_id'),
    path('page/<int:page>', ProductsListViews.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
