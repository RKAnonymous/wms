from django.shortcuts import render
from django.utils import timezone
from .forms import ProductCreateForm, InventoryCreateForm, InventoryUpdateForm
from .models import Product, Inventory


NOW = timezone.now()


def create_inventory(request):
    form = InventoryCreateForm()
    if request.method == "POST":
        form = InventoryCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.created_at = NOW
            inventory.save()
            return render(request, "inventories.html", context={"msg": 'Created'})

    context = {
        "form": form,
    }

    return render(request, "create_inv.html", context)


def update_inventory(request, id):
    obj = Inventory.objects.get(id=id)
    form = InventoryUpdateForm(instance=obj)

    if request.method == "POST":
        form = InventoryUpdateForm(instance=obj, data=request.POST, files=request.FILES)

        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.updated_at = NOW
            inventory.save()
            return render(request, 'inventories.html', context={'msg': "Updated"})

    context = {
        "form": form,
        "id": id
    }

    return render(request, "update_inv.html", context)


def create_product(request):
    form = ProductCreateForm()
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_at = NOW
            product.save()
            msg = 'Success'
            return render(request, "products.html", context={"msg": msg})
    context = {
        "product_form": form,

    }

    return render(request, "create_product.html", context)

