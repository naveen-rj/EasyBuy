from django.db import models

# Model for Site Themes
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='site/')
    caption = models.TextField()
