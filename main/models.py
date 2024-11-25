from django.db import models

# Create your models here.
class Navigate(models.Model):

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="main_images", blank=True, null=True, verbose_name="Изображение"
    )
    
    class Meta:
        db_table = "navigate"
        verbose_name = "Навигация"
        verbose_name_plural = "Навигации"

    
    def __str__(self):
        return self.name
    