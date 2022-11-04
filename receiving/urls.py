from django.urls import path, include
from .views import (
    products_list, product_detail, create_product, update_product, delete_product,
    inventories_list, inventory_detail, create_inventory, update_inventory, delete_inventory
)


urlpatterns = [
    path('inventories/', include([
        path('', inventories_list, name="inventories"),
        path('detail/<int:id>/', inventory_detail, name="detail-inventory"),
        path('create/', create_inventory, name="create-inventory"),
        path('update/<int:id>/', update_inventory, name="update-inventory"),
        path('delete/<int:id>/', delete_inventory, name="delete-inventory"),
    ])),
    path('products/', include([
        path('', products_list, name="products"),
        path('detail/<int:id>/', product_detail, name="detail-product"),
        path('create/', create_product, name="create-product"),
        path('update/<int:id>/', update_product, name="update-product"),
        path('delete/<int:id>/', delete_product, name="delete-product"),
    ])),
]