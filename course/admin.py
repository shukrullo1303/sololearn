from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from nested_admin import NestedModelAdmin, NestedTabularInline
from .models import Course, PageOfCourse, Quiz, Choice, Lesson, InputQuiz, Tips, Code_snippet

class ChoicesInline(NestedTabularInline):
    model = Choice
    extra = 2
    fields = ["choice_text", "is_true"]

class QuizInline(NestedTabularInline):
    model = Quiz
    extra = 0
    inlines = [ChoicesInline]
    fields = ["question_text"]

class InputQuizInline(NestedTabularInline):
    model = InputQuiz
    extra = 0
    fields = ["question", "answer", "endings", "new_line"]


class TipsInline(NestedTabularInline):
    model = Tips
    extra = 0
    fields = ["tip"]

class CodeInline(NestedTabularInline):
    model = Code_snippet
    extra = 0
    fields = ["code", "answer"]

class PageOfCourseInline(NestedTabularInline):
    model = PageOfCourse
    extra = 0
    inlines = [CodeInline, QuizInline, InputQuizInline, TipsInline]
    fields = ["lesson_name", "context", "page_image"]

class LessonAdmin(NestedModelAdmin):
    inlines = [
    PageOfCourseInline
    ]
    fields = ["course_name", "theme", "lock"]
    
class CourseAdmin(admin.ModelAdmin):
    model = Course
    fields = ["name", 'picture', 'description']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)


