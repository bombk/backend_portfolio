from django.contrib import admin
from .models import HeroData, AboutData, SkillCategory, Skill, Project, BlogPost, ResearchTopic, ContactMessage

@admin.register(HeroData)
class HeroDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')

@admin.register(AboutData)
class AboutDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'email', 'company')

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'link')
    list_editable = ('order',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'read_time')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ResearchTopic)
class ResearchTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date')
    list_filter = ('status',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    def has_add_permission(self, request):
        return False
