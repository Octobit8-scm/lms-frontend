import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User
from lms_api.models import Course, Module, Content

# Get all courses
courses = Course.objects.all()

course_modules = {
    'DevOps Master Course': [
        {
            'title': 'Introduction to DevOps',
            'description': 'Understanding DevOps principles and practices',
            'contents': [
                ('Introduction to DevOps Culture', 'video', 'https://example.com/devops-intro'),
                ('DevOps Principles and Practices', 'document', 'DevOps fundamentals and key concepts'),
                ('DevOps Assessment Quiz', 'quiz', 'Test your DevOps knowledge'),
            ]
        },
        {
            'title': 'Continuous Integration/Continuous Deployment',
            'description': 'Understanding CI/CD pipelines and automation',
            'contents': [
                ('CI/CD Pipeline Overview', 'video', 'https://example.com/cicd-intro'),
                ('Jenkins Pipeline Tutorial', 'document', 'Step by step guide to Jenkins pipelines'),
                ('CI/CD Practical Assignment', 'assignment', 'Create a basic CI/CD pipeline'),
            ]
        },
        {
            'title': 'Containerization with Docker',
            'description': 'Learn Docker containerization',
            'contents': [
                ('Docker Fundamentals', 'video', 'https://example.com/docker-basics'),
                ('Docker Compose Guide', 'document', 'Multi-container applications with Docker Compose'),
                ('Docker Practice Project', 'assignment', 'Containerize a web application'),
            ]
        }
    ],
    'AWS Developer Course': [
        {
            'title': 'AWS Fundamentals',
            'description': 'Core AWS services and concepts',
            'contents': [
                ('AWS Services Overview', 'video', 'https://example.com/aws-intro'),
                ('IAM and Security', 'document', 'AWS Identity and Access Management'),
                ('AWS Basic Quiz', 'quiz', 'Test your AWS knowledge'),
            ]
        },
        {
            'title': 'Serverless with Lambda',
            'description': 'Building serverless applications',
            'contents': [
                ('Lambda Functions', 'video', 'https://example.com/lambda-intro'),
                ('API Gateway Integration', 'document', 'Creating serverless APIs'),
                ('Serverless Project', 'assignment', 'Build a serverless application'),
            ]
        }
    ],
    'Python Scripting': [
        {
            'title': 'Python Basics',
            'description': 'Fundamental Python concepts',
            'contents': [
                ('Python Introduction', 'video', 'https://example.com/python-intro'),
                ('Python Data Types', 'document', 'Understanding Python data structures'),
                ('Basic Python Quiz', 'quiz', 'Test your Python knowledge'),
            ]
        },
        {
            'title': 'Automation with Python',
            'description': 'System automation using Python',
            'contents': [
                ('File Handling in Python', 'video', 'https://example.com/python-files'),
                ('System Administration Scripts', 'document', 'Python for system administration'),
                ('Automation Project', 'assignment', 'Create an automation script'),
            ]
        }
    ]
}

# Function to add modules and content
def add_modules_and_content(course, modules_data):
    for order, module_data in enumerate(modules_data, 1):
        module, _ = Module.objects.get_or_create(
            course=course,
            title=module_data['title'],
            defaults={
                'description': module_data['description'],
                'order': order
            }
        )
        
        for content_order, (title, content_type, content_data) in enumerate(module_data['contents'], 1):
            Content.objects.get_or_create(
                module=module,
                title=title,
                defaults={
                    'content_type': content_type,
                    'content_url': content_data if content_type == 'video' else '',
                    'content_text': content_data if content_type in ['document', 'assignment', 'quiz'] else '',
                    'order': content_order
                }
            )

# Add modules and content for each course
for course in courses:
    if course.title in course_modules:
        print(f"Adding content for: {course.title}")
        add_modules_and_content(course, course_modules[course.title])

print('Course content added successfully!') 