from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.
def polyshop(request):
	return render(request, 'polyshop/index.html', {})

def catalogue(request):
	items = Item.objects.all().order_by('?')
	return render(request, 'polyshop/catalogue.html', {"items":items})

def item(request, pk):
	item = get_object_or_404(Item, id=pk)
	similar_items = Item.objects.filter(category = item.category).order_by('?')[:4]
	return render(request, 'polyshop/item.html', {"item":item, "similar_items":similar_items})

def locations(request):
	return render(request, 'polyshop/locations.html', {})