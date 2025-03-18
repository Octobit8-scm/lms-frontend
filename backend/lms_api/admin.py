from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Course, Module, Content, Enrollment, Progress

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1
    ordering = ['order']

class ContentInline(admin.StackedInline):
    model = Content
    extra = 1
    ordering = ['order']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'created_at', 'updated_at', 'get_modules_count')
    list_filter = ('instructor', 'created_at')
    search_fields = ('title', 'description', 'instructor__username')
    inlines = [ModuleInline]
    
    def get_modules_count(self, obj):
        return obj.modules.count()
    get_modules_count.short_description = 'Number of Modules'

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'get_contents_count')
    list_filter = ('course',)
    search_fields = ('title', 'description', 'course__title')
    ordering = ['course', 'order']
    inlines = [ContentInline]
    
    def get_contents_count(self, obj):
        return obj.contents.count()
    get_contents_count.short_description = 'Number of Contents'

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'content_type', 'order')
    list_filter = ('content_type', 'module__course')
    search_fields = ('title', 'description', 'module__title')
    ordering = ['module', 'order']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at', 'completed')
    list_filter = ('completed', 'enrolled_at', 'course')
    search_fields = ('student__username', 'course__title')
    date_hierarchy = 'enrolled_at'

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'content', 'completed', 'completed_at')
    list_filter = ('completed', 'completed_at')
    search_fields = ('student__username', 'content__title')
    date_hierarchy = 'completed_at'

# Customize the User admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_courses_count')
    
    def get_courses_count(self, obj):
        return obj.courses_taught.count()
    get_courses_count.short_description = 'Courses Teaching'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
