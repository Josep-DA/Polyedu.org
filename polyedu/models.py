from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image 

class Category(models.Model):
	color = ColorField()
	name = models.CharField(max_length=225)
	desc = models.CharField(max_length=225, blank=True, null=True)
	
	def __str__(self):
		return(
			f"{self.name} "
			)
    

# create article model
class Article(models.Model):
	user = models.ForeignKey(
		User, related_name="articles", 
		on_delete=models.DO_NOTHING
		)
	title = models.CharField(max_length=75)
	desc = models.CharField(max_length=250)
	body = RichTextUploadingField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name="article_like", blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Aucune catégorie de matière')

	# Keep track or count of likes
	def number_of_likes(self):
		return self.likes.count()



	def __str__(self):
		return(
			f"{self.user} "
			f"({self.created_at:%Y-%m-%d %H:%M}): "
   			f"{self.title}:"
      		f"{self.category}."
			)

class Exercice(models.Model):
	user = models.ForeignKey(
		User, related_name="exercices", 
		on_delete=models.DO_NOTHING
		)
	title = models.CharField(max_length=75)
	desc = models.CharField(max_length=250)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Aucune catégorie de matière')
	
	def __str__(self):
		return self.title

class Source(models.Model):
	author_name = models.CharField(max_length=75)
	author_first_name = models.CharField(max_length=75, blank=True, null=True)
	title = models.CharField(max_length=75)
	url_link = models.CharField(max_length=200, blank=True, null=True)
	date_creation = models.DateTimeField(blank=True, null=True)
	date_consultation = models.DateTimeField(blank=True, null=True)
	published_from = models.CharField(max_length=100, blank=True, null=True)
	number_of_pages = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.title

class RessourceExterne(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Aucune catégorie de matière')
	title = models.CharField(max_length=75)
	desc = models.CharField(max_length=275)
	url_link = models.CharField(max_length=200, blank=True, null=True)
	date_creation = models.DateTimeField(blank=True, null=True)
	date_consultation = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

# Create A User Profile Model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follows = models.ManyToManyField("self", 
		related_name="followed_by",
		symmetrical=False,
		blank=True,
  		)	
	
	date_modified = models.DateTimeField(User, auto_now=True)	
	profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	profile_bio = models.CharField(default="L'écrivain(e) n'a pas de section «À propos».", null=True, blank=True, max_length=500)
	homepage_link = models.CharField(null=True, blank=True, max_length=100)
	facebook_link = models.CharField(null=True, blank=True, max_length=100)
	instagram_link = models.CharField(null=True, blank=True, max_length=100) 
	linkedin_link = models.CharField(null=True, blank=True, max_length=100)

	points = models.IntegerField(default=0)
	
	def __str__(self):
		return self.user.username

# Create Profile When New User Signs Up
#@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
		# Have the user follow themselves
		user_profile.follows.set([instance.profile.id])
		user_profile.save()

post_save.connect(create_profile, sender=User)




class Verb(models.Model):
    infinitive = models.CharField(max_length=100)
    tense = models.CharField(max_length=100)

    def __str__(self):
        return self.infinitive

class ForumPost(models.Model):
	title = models.CharField(max_length=400)
	slug = models.SlugField(max_length=400, unique=True, blank=True)
	user = models.ForeignKey(
		User, related_name="forumpost", 
		on_delete=models.DO_NOTHING
		)
	body = RichTextUploadingField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name="forum_like", blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='Aucune catégorie de matière')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(ForumPost, self).save(*args, **kwargs)