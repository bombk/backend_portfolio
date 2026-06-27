from django.db import models

class HeroData(models.Model):
    name = models.CharField(max_length=100, default="Er. Bom Bahadur BK")
    phrases = models.JSONField(default=list, help_text="JSON array of typing text phrases")
    tagline = models.TextField(default="Passionate about building scalable web applications and optimizing developer workflows.")
    cv_url = models.CharField(max_length=255, default="#")

    class Meta:
        verbose_name = "Hero Data"
        verbose_name_plural = "Hero Data"

    def __str__(self):
        return self.name

class AboutData(models.Model):
    title = models.CharField(max_length=150, default="Professional IT Engineer")
    description_1 = models.TextField()
    description_2 = models.TextField()
    location = models.CharField(max_length=100, default="Kathmandu, Nepal")
    email = models.EmailField(default="er.bombdrbk@gmail.com")
    company = models.CharField(max_length=100, default="ADBL")
    interests = models.CharField(max_length=255, default="AI, Blockchain, Cloud, DevSecOps")
    profile_image = models.CharField(max_length=255, default="/profile.jpg")

    class Meta:
        verbose_name = "About Data"
        verbose_name_plural = "About Data"

    def __str__(self):
        return self.title

class SkillCategory(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.title

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.category.title})"

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tags = models.JSONField(default=list, help_text="JSON array of tech tags")
    image_url = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default="#")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField()
    content = models.TextField()
    image_url = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now_add=True)
    read_time = models.CharField(max_length=50, default="5 min read")

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class ResearchTopic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=100, default="Ongoing", help_text="e.g. Active, Completed, Published")
    link = models.CharField(max_length=255, blank=True, default="")
    date = models.CharField(max_length=100, default="June 2026")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
