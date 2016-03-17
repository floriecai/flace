from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
	username = models.CharField(max_length = 100)
	display_name = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s' % self.username

class Post(models.Model):
	title = models.CharField(max_length = 255)
	slug = models.SlugField(max_length = 255, unique = True)
	description = models.CharField(max_length = 255)
	content = models.TextField()
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey('blog.User')
	last_edited = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return '%s' % self.title

	# @models.permalink
	# def get_absolute_url(self):
	# 	return reverse('flace.views.post', args=[self.slug])

	class Meta:
		ordering = ('created',)
