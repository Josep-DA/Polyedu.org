from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ItemCategory(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural='Items Categories'

    def __str__(self):
        return self.title

class Item(models.Model):
    category=models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    profile=models.ForeignKey('polyedu.Profile',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    description=models.TextField()
    body = RichTextField(blank=True, null=True)
    add_time=models.DateTimeField(auto_now_add=True)
    cost = models.IntegerField()

    class Meta:
        verbose_name_plural='Items'

    def __str__(self):
        return self.title

