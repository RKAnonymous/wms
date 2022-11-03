from django.urls import path, include
from .views import create_product, create_inventory, update_inventory

urlpatterns = [
    path('inventories/', include([
        path('create/', create_inventory, name="create-inventory"),
        path('update/<int:id>/', update_inventory, name="update-inventory"),
    ])),
    path('products/', include([
        path('create/', create_product, name="create-product"),
    ])),
]