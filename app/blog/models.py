from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    CATEGORY_CHOICES = (
        ('whats_new', "What's New"),
        ('funny', 'Funny'),
        ('learning', 'Learning'),
        ('fake_news', 'Fake News'),
        ('general', 'General'),
    )
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True, help_text='Optional image for the blog post')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.created.year,
            self.created.month,
            self.created.day,
            self.slug
        ])
