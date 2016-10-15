from django.db import models

class Posts(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)