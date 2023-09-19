from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Product
from main.forms import NewCollectionForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    collection = Product.objects.all()
    collection_count = len(collection)

    context = {
        'apps_name': 'DS Museum Collections',
        'name': 'Erstevan Laurel Lucky Almeida',
        'npm': '2206082493',
        'class': 'PBP - E',
        'products': collection,
        'collection_count': collection_count,
    }

    return render(request, "main.html", context)

def create_collection(request):
    form = NewCollectionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form' : form}
    return render(request, "create_collection.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")