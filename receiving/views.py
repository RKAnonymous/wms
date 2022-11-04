from django.shortcuts import render
from django.utils import timezone
from . import forms as custom_forms
from .models import Product, Inventory


NOW = timezone.now()


def inventories_list(request):
    inventories = Inventory.objects.all().order_by('-created_at')
    context = {}

    if inventories:
        context["inventories"] = inventories
    else:
        context["error"] = "No Inventories found."

    return render(request, "inventories.html", context)


def inventory_detail(request, id):
    inventory = Inventory.objects.get(id=id)
    context = {}

    if inventory:
        context["inventory"] = inventory
        return render(request, "detail_inv.html", context)

    context["error"] = "Inventory Not found."
    return render(request, "inventories.html", context)


def create_inventory(request):
    form = custom_forms.InventoryCreateForm()
    if request.method == "POST":
        form = custom_forms.InventoryCreateForm(data=request.POST, files=request.FILES)

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
    form = custom_forms.InventoryUpdateForm(instance=obj)

    if request.method == "POST":
        form = custom_forms.InventoryUpdateForm(instance=obj, data=request.POST, files=request.FILES)

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


def delete_inventory(request, id):
    obj = Inventory.objects.get(id=id)

    if obj and request.method == "delete":
        obj.delete()
        return render(request, "inventories.html", {"msg": "Deleted"})

    context = {
        "error": "Object is not found"
    }
    # return render(request, "delete_inv.html", context)


def products_list(request):
    products = Product.objects.all().order_by('-created_at')
    context = {}

    if products:
        context["products"] = products
    else:
        context["error"] = "No products found."

    return render(request, "products.html", context)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {}

    if product:
        context["product"] = product
        return render(request, 'detail_product.html', context)


    context["error"] = "Product Not found."

    return render(request, "products.html", context)


def create_product(request):
    form = custom_forms.ProductCreateForm()
    if request.method == "POST":
        form = custom_forms.ProductCreateForm(data=request.POST)

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


def update_product(request, id):
    obj = Product.objects.get(id=id)
    form = custom_forms.ProductUpdateForm(instance=obj)

    if request.method == "POST":
        form = custom_forms.ProductUpdateForm(instance=obj, data=request.POST, files=request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.updated_at = NOW
            product.save()
            return render(request, 'products.html', context={'msg': "Updated"})

    context = {
        "form": form,
        "id": id
    }

    return render(request, "update_product.html", context)


def delete_product(request, id):
    obj = Product.objects.get(id=id)

    if obj and request.method == "delete":
        obj.delete()
        return render(request, "products.html", {"msg": "Deleted"})

    context = {
        "error": "Object is not found"
    }
    # return render(request, "delete_inv.html", context)