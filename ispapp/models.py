from django.db import models

# Create your models here.
class Packages(models.Model):
    CATEGORY_CHOICES = [
        ('home', 'Home'),
        ('business', 'Business'),
    ]
    name = models.CharField(max_length=100)
    speed = models.IntegerField()
    unit = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='home')
    content = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
class Bloglist(models.Model):
    heading = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='previews/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.heading

class Blog(models.Model):
    # Link to the list entry
    blog_list_ref = models.OneToOneField(Bloglist, on_delete=models.CASCADE, related_name='full_content')
    date = models.DateField(auto_now=True)
    main_title = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=40)
    blog_image = models.ImageField(upload_to='blogs/')
    lead_text = models.TextField(null=True)
    sub_heading = models.CharField(max_length=100)
    block_quote = models.TextField(null=True)
    full_blog = models.TextField(null=True)

    def __str__(self):
        return self.main_title
    
class Lead(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    interested_package = models.ForeignKey(Packages, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.interested_package}"

class AdminDashboardProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    is_notified_on_new_lead = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username