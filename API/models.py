from django.db import models

# Create your models here.
class Videos(models.Model):
  title = models.CharField(max_length=300)
  video = models.FileField(
    upload_to='videos/'
  )
  
  def __str__(self) -> str:
    return self.title
  
  