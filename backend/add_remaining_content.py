import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User
from lms_api.models import Course, Module, Content

# Get all courses
courses = Course.objects.all()

course_modules = {
    'AWS DevOps Course': [
        {
            'title': 'AWS DevOps Fundamentals',
            'description': 'Introduction to AWS DevOps practices',
            'contents': [
                ('AWS DevOps Overview', 'video', 'https://example.com/aws-devops-intro'),
                ('AWS DevOps Tools', 'document', 'Overview of AWS DevOps tools and services'),
                ('AWS DevOps Quiz', 'quiz', 'Test your AWS DevOps knowledge'),
            ]
        },
        {
            'title': 'AWS CI/CD Services',
            'description': 'AWS CI/CD pipeline implementation',
            'contents': [
                ('CodePipeline Introduction', 'video', 'https://example.com/codepipeline'),
                ('CodeBuild and CodeDeploy', 'document', 'Implementing CI/CD with AWS services'),
                ('CI/CD Project', 'assignment', 'Create a CI/CD pipeline in AWS'),
            ]
        }
    ],
    'AWS Cloud Practitioner': [
        {
            'title': 'Cloud Concepts',
            'description': 'Understanding cloud computing basics',
            'contents': [
                ('Cloud Computing Basics', 'video', 'https://example.com/cloud-basics'),
                ('AWS Global Infrastructure', 'document', 'Understanding AWS regions and availability zones'),
                ('Cloud Concepts Quiz', 'quiz', 'Test your cloud knowledge'),
            ]
        },
        {
            'title': 'AWS Core Services',
            'description': 'Essential AWS services overview',
            'contents': [
                ('EC2 and S3 Basics', 'video', 'https://example.com/aws-core'),
                ('AWS Security Fundamentals', 'document', 'Basic AWS security concepts'),
                ('Core Services Project', 'assignment', 'Work with basic AWS services'),
            ]
        }
    ],
    'GCP Developer Course': [
        {
            'title': 'GCP Development Basics',
            'description': 'Getting started with GCP development',
            'contents': [
                ('GCP Development Overview', 'video', 'https://example.com/gcp-dev'),
                ('App Engine Fundamentals', 'document', 'Building applications with App Engine'),
                ('GCP Development Quiz', 'quiz', 'Test your GCP knowledge'),
            ]
        },
        {
            'title': 'Cloud Functions and Run',
            'description': 'Serverless development in GCP',
            'contents': [
                ('Cloud Functions Basics', 'video', 'https://example.com/cloud-functions'),
                ('Cloud Run Deployment', 'document', 'Deploying containers with Cloud Run'),
                ('Serverless Project', 'assignment', 'Build a serverless application in GCP'),
            ]
        }
    ],
    'Azure DevOps Course': [
        {
            'title': 'Azure DevOps Fundamentals',
            'description': 'Introduction to Azure DevOps services',
            'contents': [
                ('Azure DevOps Overview', 'video', 'https://example.com/azure-devops'),
                ('Azure Pipelines Basics', 'document', 'Understanding Azure Pipelines'),
                ('Azure DevOps Quiz', 'quiz', 'Test your Azure DevOps knowledge'),
            ]
        },
        {
            'title': 'Azure CI/CD Implementation',
            'description': 'Implementing CI/CD in Azure',
            'contents': [
                ('Azure Pipelines Advanced', 'video', 'https://example.com/azure-pipelines'),
                ('Release Management', 'document', 'Managing releases in Azure DevOps'),
                ('CI/CD Project', 'assignment', 'Create a CI/CD pipeline in Azure'),
            ]
        }
    ],
    'Linux Scripting': [
        {
            'title': 'Shell Scripting Basics',
            'description': 'Introduction to shell scripting',
            'contents': [
                ('Bash Basics', 'video', 'https://example.com/bash-intro'),
                ('Shell Commands and Scripts', 'document', 'Essential shell commands and scripting'),
                ('Basic Scripts Quiz', 'quiz', 'Test your shell scripting knowledge'),
            ]
        },
        {
            'title': 'Advanced Shell Scripting',
            'description': 'Advanced shell scripting concepts',
            'contents': [
                ('Advanced Scripting Techniques', 'video', 'https://example.com/advanced-bash'),
                ('Automation with Shell Scripts', 'document', 'Creating automation scripts'),
                ('Automation Project', 'assignment', 'Create an automation script'),
            ]
        }
    ],
    'Groovy Scripting': [
        {
            'title': 'Groovy Fundamentals',
            'description': 'Introduction to Groovy programming',
            'contents': [
                ('Groovy Syntax', 'video', 'https://example.com/groovy-intro'),
                ('Groovy Basics', 'document', 'Groovy programming fundamentals'),
                ('Groovy Quiz', 'quiz', 'Test your Groovy knowledge'),
            ]
        },
        {
            'title': 'Jenkins Pipeline Scripting',
            'description': 'Groovy scripting for Jenkins pipelines',
            'contents': [
                ('Pipeline Basics', 'video', 'https://example.com/jenkins-pipeline'),
                ('Pipeline Script Development', 'document', 'Creating Jenkins pipeline scripts'),
                ('Pipeline Project', 'assignment', 'Create a Jenkins pipeline script'),
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

print('Additional course content added successfully!') 