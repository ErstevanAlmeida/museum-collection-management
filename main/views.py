import json
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from main.forms import NewCollectionForm
from main.models import Product
import datetime

@login_required(login_url='/login/')
def show_main(request):
    collection = Product.objects.filter(user=request.user)
    collection_count = len(collection)

    context = {
        'apps_name': 'DS Museum Collections',
        'name': 'Erstevan Laurel Lucky Almeida',
        'npm': '2206082493',
        'class': 'PBP - E',
        'products': collection,
        'collection_count': collection_count,
        'last_login': request.COOKIES.get('last_login'),
        'account' : request.user.username,
    }

    return render(request, "main.html", context)

def create_collection(request):
    form = NewCollectionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        collection = form.save(commit=False)
        collection.user = request.user
        collection.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been succesfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_collection(request, id):
    collection = Product.objects.get(pk = id)
    form = NewCollectionForm(request.POST or None, instance=collection)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form':form}
    return render(request, "edit_collection.html", context)

def delete_collection(request, id):
    collection = Product.objects.get(pk=id)
    collection.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_collection_json(request):
    collection = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', collection))

@csrf_exempt
def add_collection_ajax(request):
    if request.method == 'POST':
        collection = request.POST.get("collection")
        type = request.POST.get("type")
        amount = request.POST.get("amount")
        year = request.POST.get("year")
        description = request.POST.get("description")
        user = request.user

        new_collection = Product(collection=collection, type=type, amount=amount, year=year, description=description, user=user)
        new_collection.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            collection = data["collection"],
            type = data["year"],
            year = int(data["year"]),
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)