from django.db import models
from django.contrib.auth.models import User # Tämä importtaus on siksi, että saadaan User toimimaan

class Rss(models.Model):
	website = models.CharField(max_length=300)
	category = models.CharField(max_length=300)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def get_absolute_url(self):
		return f"/rss/{self.pk}"

	def go_back(self):
		return f"/rss/"

	def __str__(self):
		return self.website
