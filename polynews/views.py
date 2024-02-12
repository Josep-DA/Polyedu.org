from django.shortcuts import render, get_object_or_404
from .models import News, NewsCategory
from django.http import Http404


# Create your views here.
def polynews(request):
	news = News.objects.all().order_by('-add_time')
	categories = NewsCategory.objects.all().order_by('title')
	return render(request, 'polynews/index.html', {"news":news, "categories":categories})

def newsarticle(request, pk):
	new = get_object_or_404(News, id=pk)
	news = News.objects.all().order_by('-add_time')

	categories = NewsCategory.objects.all().order_by('title')
	if new:
		return render(request, "polynews/article.html", {'new':new, "news":news, "categories":categories})
	else:
		messages.success(request, ("Cet article n'existe pas..."))
		return redirect('polynews')		

def categories(request, pk):
	category = get_object_or_404(NewsCategory, title=pk)
	news = News.objects.filter(category=category).order_by('-add_time')
	categories = NewsCategory.objects.all().order_by('title')
	if category:
		return render(request, "polynews/category.html", {'category':category, "news":news, "categories":categories})
	else:
		messages.success(request, ("Cet article n'existe pas..."))
		return redirect('polynews')	


def love_generator(request):
	news = News.objects.all().order_by('-add_time')
	categories = NewsCategory.objects.all().order_by('title')
	return render(request, 'polynews/index.html', {"news":news, "categories":categories})

def love(request, dt):
	try:
		data = dt.split(';')
		to_name = data[0]
		from_name = data[1]
		gender = data[2]
		email = data[3]
	except:
		raise Http404("Page does not exist")
	
	return render(request, 'polynews/love.html', {
		'to_name':to_name.capitalize(), 
		'from_name':from_name.capitalize(),
		'gender':gender,
		'email': email
		})