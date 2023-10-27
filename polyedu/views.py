from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Article, Verb, Exercice, Source, RessourceExterne, ForumPost, Category
from .forms import ArticleForm, SignUpForm, ProfilePicForm, VerbConjugationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.translation import activate, get_language
from django.conf import settings
from random import sample

def home(request):
	return render(request, 'polyedu/index.html', {})

def campagne(request):
	return render(request, 'polyedu/campagne.html', {})

def test(request):
	return render(request, 'polyedu/test.html', {})

def courses(request):
	return render(request, 'polyedu/courses/courses.html', {})

def correlation_lineaire(request):
	return render(request, 'polyedu/courses/correlation-lineaire/correlation_lineaire.html', {})

def geometrie_analytique(request):
	return render(request, 'polyedu/courses/geometrie-analytique/geometrie-analytique.html', {})

def europe(request):
	return render(request, 'polyedu/courses/grandes-regions-monde/europe.html', {})

def classesdemots(request):
	return render(request, 'polyedu/courses/classes-de-mots/classesdemots.html', {})

def dudh1(request):
	return render(request, 'polyedu/dudh1.html', {})

def gm1(request):
	return render(request, 'polyedu/gm1.html', {})

def exercices(request):
	exercices = Exercice.objects.all().order_by('-created_at')
	return render(request, 'polyedu/courses/exercices/exercices.html', {"exercices":exercices})

def exercice_show(request, pk):
    exercice = get_object_or_404(Exercice, id=pk)
    exercices = Exercice.objects.all().order_by('-created_at')
    if exercice:
        return render(request, "polyedu/courses/exercices/show_exercice.html", {'exercice':exercice, "exercices":exercices})
    else:
        messages.success(request, ("That Exercice Does Not Exist..."))
        return redirect('home')	

def bibliography(request):
	sources = Source.objects.all().order_by('title')
	return render(request, 'polyedu/bibliography.html', {'sources':sources})

def bjournal(request):
	return render(request, 'polyedu/bjournal.html', {})

def ressources_externe(request):
	ressources = RessourceExterne.objects.all().order_by('title')
	return render(request, 'polyedu/ressources/externes/ressources_externe.html', {"ressources":ressources})

def ressources_interne(request):
	return render(request, 'polyedu/ressources/internes/ressources_interne.html', {})

def code_editor(request):
	return render(request, 'polyedu/ressources/internes/code_editor.html', {})

def periodic_table(request):
	return render(request, 'polyedu/ressources/internes/periodic_table.html', {})

def word_counter(request):
	return render(request, 'polyedu/ressources/internes/word_counter.html', {})

def code_resistor(request):
	return render(request, 'polyedu/ressources/internes/code_resistor.html', {})

def circuit_simulator(request):
	return render(request, 'polyedu/ressources/internes/circuit_simulator.html', {})

def career_exploration(request):
	return render(request, 'polyedu/ressources/internes/career_exploration.html', {})

def art_studio(request):
	return render(request, 'polyedu/ressources/internes/art_studio.html', {})

def ondes(request):
	return render(request, 'polyedu/ressources/internes/ondes.html', {})

def ellipse_lab(request):
	return render(request, 'polyedu/ressources/internes/ellipse_lab.html', {})

def articles(request):
	if request.user.is_authenticated:
		form = ArticleForm(request.POST or None)
		articles = Article.objects.all().order_by("-created_at")
		if request.method == "POST":
			search = request.POST['search']
			searched = Article.objects.filter(body__contains = search)
			return render(request, 'polyedu/courses/articles/articles.html', {'search':search, 'searched':searched, "articles":articles, "form":form})
		else:
			return render(request, 'polyedu/courses/articles/articles.html', {"articles":articles, "form":form})
	else:
		articles = Article.objects.all().order_by("-created_at")
		if request.method == "POST":
			search = request.POST['search']
			searched = Article.objects.filter(body__contains = search)
			return render(request, 'polyedu/courses/articles/articles.html', {'search':search, 'searched':searched, "articles":articles})
		else:
			return render(request, 'polyedu/courses/articles/articles.html', {"articles":articles})

def article_create(request):
    if request.user.is_authenticated:
        form = ArticleForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()

           
                messages.success(request,
                            'Your Article Has Been Posted!')
                return redirect('articles')
        articles = Article.objects.all().order_by('-created_at')
        return render(request, 'polyedu/courses/articles/create_article.html',
                      {'articles': articles, 'form': form})
    else:
        messages.success(request,
                         'You have to be logged in to do this action!')
        return redirect('home')

@login_required
def chat_room(request):
    return render(request, 'polyedu/chat/chat_room.html')

def profile_list(request):
	if request.user.is_authenticated:
		profiles = Profile.objects.exclude(user=request.user)
		return render(request, 'polyedu/profile/profile_list.html', {"profiles":profiles})
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')

def unfollow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.remove(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Unfollowed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')

def follow(request, pk):
	if request.user.is_authenticated:
		# Get the profile to unfollow
		profile = Profile.objects.get(user_id=pk)
		# Unfollow the user
		request.user.profile.follows.add(profile)
		# Save our profile
		request.user.profile.save()

		# Return message
		messages.success(request, (f"You Have Successfully Followed {profile.user.username}"))
		return redirect(request.META.get("HTTP_REFERER"))

	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')




def profile(request, pk):
	if request.user.is_authenticated:
		profile = Profile.objects.get(user_id=pk)
		articles = Article.objects.filter(user_id=pk).order_by("-created_at")

		# Post Form logic
		if request.method == "POST":
			# Get current user
			current_user_profile = request.user.profile
			# Get form data
			action = request.POST['follow']
			# Decide to follow or unfollow
			if action == "unfollow":
				current_user_profile.follows.remove(profile)
			elif action == "follow":
				current_user_profile.follows.add(profile)
			# Save the profile
			current_user_profile.save()



		return render(request, "polyedu/profile/profile.html", {"profile":profile, "articles":articles})
	else:
		messages.success(request, ("Vous devez être connecté afin de visionner cette page."))
		return redirect('home')		

def followers(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'polyedu/profile/followers.html', {"profiles":profiles})
		else:
			messages.success(request, ("That's Not Your Profile Page..."))
			return redirect('home')	
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')


def follows(request, pk):
	if request.user.is_authenticated:
		if request.user.id == pk:
			profiles = Profile.objects.get(user_id=pk)
			return render(request, 'polyedu/profile/follows.html', {"profiles":profiles})
		else:
			messages.success(request, ("That's Not Your Profile Page..."))
			return redirect('home')	
	else:
		messages.success(request, ("You Must Be Logged In To View This Page..."))
		return redirect('home')



def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ("You Have Been Logged In!"))
			return redirect('home')
		else:
			messages.success(request, ("There was an error logging in. Please Try Again..."))
			return redirect('login')

	else:
		return render(request, "polyedu/registration/login.html", {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You Have Been Logged Out. Sorry to Let You Go..."))
	return redirect('home')

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# first_name = form.cleaned_data['first_name']
			# second_name = form.cleaned_data['second_name']
			# email = form.cleaned_data['email']
			# Log in user
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ("You have successfully registered! Welcome!"))
			return redirect('home')
	
	return render(request, "polyedu/registration/register.html", {'form':form})


def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		profile_user = Profile.objects.get(user__id=request.user.id)
		# Get Forms
		user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
		profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

			login(request, current_user)
			messages.success(request, ("Your Profile Has Been Updated!"))
			return redirect('home')

		return render(request, "polyedu/profile/update_user.html", {'user_form':user_form, 'profile_form':profile_form})
	else:
		messages.success(request, ("You Must Be Logged In To View That Page..."))
		return redirect('home')
	
def article_like(request, pk):
	if request.user.is_authenticated:
		article = get_object_or_404(Article, id=pk)
		if article.likes.filter(id=request.user.id):
			article.likes.remove(request.user)
		else:
			article.likes.add(request.user)
		
		return redirect(request.META.get("HTTP_REFERER"))




	else:
		messages.success(request, ("You Must Be Logged In To View That Page..."))
		return redirect('home')


def article_show(request, pk):
	article = get_object_or_404(Article, id=pk)
	articles = Article.objects.filter(category = article.category).order_by('?')[:2]
	if article:
		return render(request, "polyedu/courses/articles/show_article.html", {'article':article, "articles":articles})
	else:
		messages.success(request, ("That Article Does Not Exist..."))
		return redirect('home')		


def delete_article(request, pk):
	if request.user.is_authenticated:
		article = get_object_or_404(Article, id=pk)
		# Check to see if you own the article
		if request.user.username == article.user.username:
			# Delete The article
			article.delete()
			
			messages.success(request, ("The Article Has Been Deleted!"))
			return redirect(request.META.get("HTTP_REFERER"))	
		else:
			messages.success(request, ("You Don't Own That Article!!"))
			return redirect('home')

	else:
		messages.success(request, ("Please Log In To Continue..."))
		return redirect(request.META.get("HTTP_REFERER"))

def edit_article(request, pk):
	if request.user.is_authenticated:
     
		article = get_object_or_404(Article, id=pk)
		if request.user.username == article.user.username:
			form = ArticleForm(request.POST or None, instance=article)
			if request.method == "POST":
				if form.is_valid():
					article = form.save(commit=False)
					article.user = request.user
					article.save()
					messages.success(request, ("Your Article Has Been Updated!"))
					return redirect('home')
		# Check to see if you own the article
			else:
				return render(request, "polyedu/courses/articles/edit_article.html", {'form':form, 'article':article})	
		else:
			messages.success(request, ("You Don't Own That Article!!"))
			return redirect('home')

	else:
		messages.success(request, ("Please Log In To Continue..."))
		return redirect('home')

# Articles

def switch_language(request):
    language_code = request.GET.get('language_code')

    # Get the current language
    current_language = get_language()

    # If language_code is not provided or invalid, toggle between French and English
    if language_code not in ['fr-ca', 'en']:
        if current_language == 'fr-ca':
            language_code = 'en'
        else:
            language_code = 'fr-ca'

    # Activate the chosen language
    activate(language_code)

    # Store the language preference in session or cookie
    if hasattr(request, 'session'):
        request.session[settings.LANGUAGE_SESSION_KEY] = language_code
    else:
        response = redirect(request.GET.get('next', '/'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)

    return response

def search_user(request):
	if request.method == "POST":
		search = request.POST['search']

		searched = User.objects.filter(username__contains = search)

		return render(request, 'polyedu/profile/search_user.html', {'search':search, 'searched':searched})
	else:
		return render(request, 'polyedu/profile/search_user.html', {})

def conjugation_view(request):
    verb = Verb.objects.get(pk=1)  # Assuming you have a verb object stored in the database
    if request.method == 'POST':
        form = VerbConjugationForm(request.POST)
        if form.is_valid():
            # Process the form data here
            # You can access the conjugation values using form.cleaned_data['pronoun']
            # and perform any necessary validation or calculations
            # Return the result to the user
            return render(request, 'polyedu/courses/exercices/conjugator/result.html')
    else:
        form = VerbConjugationForm(initial={'infinitive': verb.infinitive, 'tense': verb.tense})
    
    return render(request, 'polyedu/courses/exercices/conjugator/conjugation.html', {'form': form})

def leaderboard(request):
    profiles = Profile.objects.order_by('-points')  # Sort profiles by points in descending order
    return render(request, 'polyedu/profile/leaderboard.html', {'profiles': profiles})

def forum(request):
	categories = Category.objects.all().order_by('name')
	return render(request, "polyedu/forum/forum.html", {"categories":categories})

def forumcategory(request, ck):
	category = get_object_or_404(Category, name=ck)
	posts = ForumPost.objects.filter(category=category).order_by('-created_at')
	categories = Category.objects.all().order_by('name')
	return render(request, "polyedu/forum/category.html", {"posts":posts,"category":category, "categories":categories})

def forumpost(request, ck, pk):
	post = get_object_or_404(ForumPost, id=pk)
	category = get_object_or_404(Category, name=ck)
	posts = ForumPost.objects.filter(category = post.category).order_by('-created_at')[:2]
	if article:
		return render(request, "polyedu/forum/post.html", {'post':post, "posts":posts,"category":category})
	else:
		messages.success(request, ("That Post Does Not Exist..."))
		return redirect('forum')

