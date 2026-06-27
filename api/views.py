from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import HeroData, AboutData, SkillCategory, Skill, Project, BlogPost, ResearchTopic, ContactMessage

def get_portfolio_data(request):
    # Get or create HeroData
    hero, _ = HeroData.objects.get_or_create(
        id=1,
        defaults={
            "name": "Er. Bom Bahadur BK",
            "phrases": ["IT Engineer", "Full Stack Developer", "DevOps Enthusiast", "Problem Solver"],
            "tagline": "Passionate about building scalable web applications and optimizing developer workflows. Turning complex problems into elegant, efficient solutions.",
            "cv_url": "#"
        }
    )

    # Get or create AboutData
    about, _ = AboutData.objects.get_or_create(
        id=1,
        defaults={
            "title": "Professional IT Engineer",
            "description_1": "I am a dedicated IT Engineer with a strong foundation in computer science and a passion for modern web technologies. My journey in tech is driven by a constant desire to learn and implement cutting-edge solutions.",
            "description_2": "With expertise in full-stack development and a keen interest in DevOps, I bridge the gap between robust backend systems and intuitive frontend experiences. I believe in writing clean, maintainable code and building products that make a difference.",
            "location": "Kathmandu, Nepal",
            "email": "er.bombdrbk@gmail.com",
            "company": "ADBL",
            "interests": "AI, Blockchain, Cloud, DevSecOps",
            "profile_image": "/profile.jpg"
        }
    )

    # Format Skills
    categories = SkillCategory.objects.prefetch_related('skills').all()
    skills_data = []
    for cat in categories:
        skills_data.append({
            "title": cat.title,
            "skills": [s.name for s in cat.skills.all()]
        })

    # Format Projects
    projects = Project.objects.all()
    projects_data = []
    for p in projects:
        projects_data.append({
            "title": p.title,
            "desc": p.description,
            "tags": p.tags,
            "image": p.image_url,
            "link": p.link
        })

    # Format Blog Posts
    blogs = BlogPost.objects.all()
    blogs_data = []
    for b in blogs:
        blogs_data.append({
            "id": b.id,
            "title": b.title,
            "slug": b.slug,
            "excerpt": b.excerpt,
            "content": b.content,
            "image": b.image_url,
            "published_date": b.published_date.strftime("%Y-%m-%d"),
            "read_time": b.read_time
        })

    # Format Research Topics
    research = ResearchTopic.objects.all()
    research_data = []
    for r in research:
        research_data.append({
            "id": r.id,
            "title": r.title,
            "description": r.description,
            "status": r.status,
            "link": r.link,
            "date": r.date
        })

    response_data = {
        "hero": {
            "name": hero.name,
            "phrases": hero.phrases,
            "tagline": hero.tagline,
            "cv_url": hero.cv_url
        },
        "about": {
            "title": about.title,
            "description_1": about.description_1,
            "description_2": about.description_2,
            "location": about.location,
            "email": about.email,
            "company": about.company,
            "interests": about.interests,
            "profile_image": about.profile_image
        },
        "skills": skills_data,
        "projects": projects_data,
        "blogs": blogs_data,
        "research": research_data
    }

    return JsonResponse(response_data, safe=False)

@csrf_exempt
def contact_submit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            if not name or not email or not message:
                return JsonResponse({"error": "All fields are required"}, status=400)

            msg = ContactMessage.objects.create(name=name, email=email, message=message)
            return JsonResponse({"message": "Message received successfully", "id": msg.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
