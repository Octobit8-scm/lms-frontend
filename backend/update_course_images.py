import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from lms_api.models import Course

# Course image URLs mapping
course_images = {
    'DevOps Master Course': 'https://img-c.udemycdn.com/course/750x422/3067678_d82e.jpg',
    'AWS Developer Course': 'https://img-c.udemycdn.com/course/750x422/3413644_dc6c.jpg',
    'AWS DevOps Course': 'https://img-c.udemycdn.com/course/750x422/2555208_5a3e.jpg',
    'AWS Cloud Practitioner': 'https://img-c.udemycdn.com/course/750x422/3937580_7a24_5.jpg',
    'GCP Developer Course': 'https://img-c.udemycdn.com/course/750x422/2534736_2e57_2.jpg',
    'GCP DevOps Course': 'https://img-c.udemycdn.com/course/750x422/3460744_d3c4_2.jpg',
    'GCP Cloud Practitioner': 'https://img-c.udemycdn.com/course/750x422/2554450_6ed0_5.jpg',
    'Azure DevOps Course': 'https://img-c.udemycdn.com/course/750x422/3245278_1c5f_2.jpg',
    'Azure Developer Course': 'https://img-c.udemycdn.com/course/750x422/3449184_0400_2.jpg',
    'Azure Cloud Practitioner': 'https://img-c.udemycdn.com/course/750x422/3449498_5943_2.jpg',
    'Groovy Scripting': 'https://img-c.udemycdn.com/course/750x422/1493710_397e_2.jpg',
    'Linux Scripting': 'https://img-c.udemycdn.com/course/750x422/3444642_6bf0_2.jpg',
    'Python Scripting': 'https://img-c.udemycdn.com/course/750x422/2696862_515a_2.jpg'
}

# Update course images
updated_count = 0
for course in Course.objects.all():
    if course.title in course_images:
        course.image_url = course_images[course.title]
        course.save()
        updated_count += 1
        print(f'Updated image for course: {course.title}')

print(f'\nTotal courses updated: {updated_count}') 