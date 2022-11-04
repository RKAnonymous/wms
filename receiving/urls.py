from django.urls import path, include
from .views import (
    create_product, update_product,
    inventories_list, inventory_detail, create_inventory, update_inventory, delete_inventory
)


urlpatterns = [
    path('inventories/', include([
        path('', inventories_list, name="inventories"),
        path('detail/<int:id>/', inventory_detail, name="detail-inventory"),
        path('create/', create_inventory, name="create-inventory"),
        path('update/<int:id>/', update_inventory, name="update-inventory"),
        # path('delete/<int:id>/', delete_inventory, name="delete-inventory"),
    ])),
    path('products/', include([
        path('create/', create_product, name="create-product"),
        path('update/<int:id>/', update_product, name="update-product"),
    ])),
]