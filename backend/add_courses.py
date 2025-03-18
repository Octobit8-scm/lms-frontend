import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User
from lms_api.models import Course

# Get the admin user
admin_user = User.objects.get(username='admin')

# Course data
courses_data = [
    {
        'title': 'DevOps Master Course',
        'description': 'Master DevOps practices, tools, and methodologies. Learn CI/CD, containerization, automation, and infrastructure as code.',
    },
    {
        'title': 'AWS Developer Course',
        'description': 'Learn to develop applications for AWS. Master services like Lambda, S3, DynamoDB, and API Gateway.',
    },
    {
        'title': 'AWS DevOps Course',
        'description': 'Implement DevOps practices on AWS. Learn CodePipeline, CodeBuild, CodeDeploy, and CloudFormation.',
    },
    {
        'title': 'AWS Cloud Practitioner',
        'description': 'Get started with AWS cloud services. Learn core services, security, architecture, and pricing.',
    },
    {
        'title': 'GCP Developer Course',
        'description': 'Develop applications for Google Cloud Platform. Master App Engine, Cloud Functions, and Cloud Run.',
    },
    {
        'title': 'GCP DevOps Course',
        'description': 'Implement DevOps on Google Cloud Platform. Learn Cloud Build, Container Registry, and Kubernetes Engine.',
    },
    {
        'title': 'GCP Cloud Practitioner',
        'description': 'Introduction to Google Cloud Platform. Learn core services, networking, storage, and compute options.',
    },
    {
        'title': 'Azure DevOps Course',
        'description': 'Master DevOps practices on Azure. Learn Azure Pipelines, Azure Repos, and Azure Artifacts.',
    },
    {
        'title': 'Azure Developer Course',
        'description': 'Develop applications for Microsoft Azure. Learn App Service, Functions, and Cosmos DB.',
    },
    {
        'title': 'Azure Cloud Practitioner',
        'description': 'Get started with Microsoft Azure. Learn core services, security, and cloud concepts.',
    },
    {
        'title': 'Groovy Scripting',
        'description': 'Master Groovy programming language. Learn syntax, closures, metaprogramming, and Jenkins pipeline scripting.',
    },
    {
        'title': 'Linux Scripting',
        'description': 'Learn shell scripting in Linux. Master Bash, automation, system administration, and text processing.',
    },
    {
        'title': 'Python Scripting',
        'description': 'Learn Python scripting for automation. Master file handling, system automation, and task automation.',
    },
]

# Create courses
for course_data in courses_data:
    Course.objects.get_or_create(
        title=course_data['title'],
        defaults={
            'description': course_data['description'],
            'instructor': admin_user,
        }
    )

print('Courses added successfully!') 