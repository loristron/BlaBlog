from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q
from django.utils.text import slugify

from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL
now = timezone.now()

class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now)

	def search(self, query):

		lookups = (
			Q(postTitle__icontains=query) 			|
			Q(postContent__icontains=query) 		|
			Q(slug__icontains=query) 				|
			Q(user__first_name__icontains=query) 	|
			Q(user__last_name__icontains=query)		|
			Q(user__email__icontains=query) 		|
			Q(user__username__icontains=query)
			)

		return self.filter(lookups)


class BlogPostManager(models.Manager):
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db)

	def published(self):
		return self.get_queryset().published()

	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query)
		


class BlogPost(models.Model):
	user 			= models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	image 			= models.ImageField(upload_to='images/', blank=True, null=True)
	postTitle		= models.CharField(max_length=240)
	postContent 	= models.TextField(null=True, blank=True)
	publish_date 	= models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True, default=now)
	time_stamp	 	= models.DateTimeField(auto_now=True, auto_now_add=False)
	update_stamp 	= models.DateTimeField(auto_now=True, auto_now_add=False)
	slug 			= models.SlugField(unique=True, editable=False, ) #url "enconded' value


	objects = BlogPostManager()


	class Meta:
		ordering = [
			'-publish_date', 
			'-update_stamp', 
			'-time_stamp',
		]

	def save(self, *args, **kwargs):
		self.slug = slugify(self.postTitle, allow_unicode=True)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
