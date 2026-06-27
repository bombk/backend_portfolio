import os
import sys
import django

# Add backend to path and set up Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_backend.settings")
django.setup()

from api.models import HeroData, AboutData, SkillCategory, Skill, Project, BlogPost, ResearchTopic

def seed():
    print("Seeding database...")

    # 1. Hero
    HeroData.objects.all().delete()
    hero = HeroData.objects.create(
        name="Er. Bom Bahadur BK",
        phrases=["IT Engineer", "Full Stack Developer", "DevOps Enthusiast", "Problem Solver"],
        tagline="Passionate about building scalable web applications and optimizing developer workflows. Turning complex problems into elegant, efficient solutions.",
        cv_url="#"
    )
    print("Seeded HeroData.")

    # 2. About
    AboutData.objects.all().delete()
    about = AboutData.objects.create(
        title="Professional IT Engineer",
        description_1="I am a dedicated IT Engineer with a strong foundation in computer science and a passion for modern web technologies. My journey in tech is driven by a constant desire to learn and implement cutting-edge solutions.",
        description_2="With expertise in full-stack development and a keen interest in DevOps, I bridge the gap between robust backend systems and intuitive frontend experiences. I believe in writing clean, maintainable code and building products that make a difference.",
        location="Kathmandu, Nepal",
        email="er.bombdrbk@gmail.com",
        company="ADBL",
        interests="AI, Blockchain, Cloud, DevSecOps"
    )
    print("Seeded AboutData.")

    # 3. Skills
    SkillCategory.objects.all().delete()
    skills_map = {
        "AI/ML": ["Machine Learning", "Deep Learning", "Reinforcement Learning", "Data Science", "Keras", "TensorFlow", "PyTorch", "Scikit-learn"],
        "DevOps": ["Linux", "Kubernetes", "Docker", "Jenkins", "AWS", "CI/CD", "Windows Server", "Nginx", "Apache"],
        "Backend": ["Python", "Laravel", "Django", "PostgreSQL", "Oracle DB", "MongoDB", "MySQL", "Redis"],
        "Frontend": ["React", "Bootstrap", "TypeScript", "Tailwind CSS", "Next.js"]
    }

    for cat_title, skills in skills_map.items():
        cat = SkillCategory.objects.create(title=cat_title)
        for s_name in skills:
            Skill.objects.create(category=cat, name=s_name)
    print("Seeded Skills.")

    # 4. Projects
    Project.objects.all().delete()
    projects = [
        {
            "title": "CloudScale Platform",
            "description": "A high-performance cloud monitoring dashboard with real-time metrics and alerts.",
            "tags": ["React", "Go", "Kubernetes"],
            "link": "#",
            "order": 0
        },
        {
            "title": "AI Analysis Tool",
            "description": "Leveraging LLMs to perform automated code reviews and security audits.",
            "tags": ["Python", "FastAPI", "OpenAI"],
            "link": "#",
            "order": 1
        },
        {
            "title": "E-Commerce Engine",
            "description": "A headless commerce solution built for scalability and lightning-fast performance.",
            "tags": ["Next.js", "GraphQL", "Stripe"],
            "link": "#",
            "order": 2
        }
    ]

    for p in projects:
        Project.objects.create(**p)
    print("Seeded Projects.")

    # 5. Blog
    BlogPost.objects.all().delete()
    blogs = [
        {
            "title": "Understanding Microservices Architecture",
            "slug": "understanding-microservices-architecture",
            "excerpt": "An introductory guide to building scalable and independently deployable microservice architectures.",
            "content": "Microservices are an architectural style that structures an application as a collection of services that are highly maintainable, testable, loosely coupled, and independently deployable. In this post, we explore their benefits, common design patterns, and deployment strategies using Docker and Kubernetes. We also touch upon patterns like API Gateways, Service Discovery, and database separation.",
            "read_time": "5 min read"
        },
        {
            "title": "Deep Dive into React Server Components",
            "slug": "react-server-components",
            "excerpt": "A detailed look into the rendering paradigms introduced by React Server Components.",
            "content": "React Server Components represent a significant shift in how we build React applications. By allowing components to render on the server, we can reduce the JavaScript bundle size sent to the client, improve initial page load times, and integrate seamlessly with data sources. This post covers the conceptual model, standard implementations, and how React 19 handles static and dynamic server-side execution.",
            "read_time": "8 min read"
        }
    ]

    for b in blogs:
        BlogPost.objects.create(**b)
    print("Seeded Blog posts.")

    # 6. Research
    ResearchTopic.objects.all().delete()
    research_topics = [
        {
            "title": "AI-Driven Automated Vulnerability Assessment",
            "description": "Developing a system that uses fine-tuned LLMs to scan source code repositories for security issues, mapping them to CWE standards and recommending fixes.",
            "status": "Active Research",
            "link": "",
            "date": "Ongoing"
        },
        {
            "title": "Decentralized Identity Verification using Blockchain",
            "description": "A research paper proposing secure protocols for privacy-preserving digital identity credentials on public-private blockchains with zero-knowledge proofs.",
            "status": "Published",
            "link": "https://example.com/blockchain-identity",
            "date": "December 2025"
        }
    ]

    for r in research_topics:
        ResearchTopic.objects.create(**r)
    print("Seeded Research topics.")

    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed()
