from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class NewsCategory(models.Model):
    title=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='News Categories'

    def __str__(self):
        return self.title

class News(models.Model):
    category=models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    profile=models.ForeignKey('polyedu.Profile',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()
    body = RichTextField(blank=True, null=True)
    add_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='News'

    def __str__(self):
        return self.title

class Comment(models.Model):
    news=models.ForeignKey(News, on_delete=models.CASCADE)
    profile=models.ForeignKey('polyedu.Profile',on_delete=models.CASCADE)
    comment=models.TextField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.comment