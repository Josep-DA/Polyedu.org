from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Article, Category, Verb, Exercice, Source, RessourceExterne, ForumPost

# Unregister Groups

# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	# Just display username fields on admin page
	inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)
admin.site.register(ForumPost)

# Register Articles
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Exercice)

# Ressources
admin.site.register(Source)
admin.site.register(RessourceExterne)

# Register Verbs
admin.site.register(Verb)