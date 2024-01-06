from django.db import models 
from user.models import User 

class Course(models.Model): 
    picture = models.ImageField(blank=True, upload_to="imgs/course/")
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    active = models.ManyToManyField(User, related_name='active_course', blank=True)
    completed = models.ManyToManyField(User, related_name="completed_course", blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Kurs ")
        verbose_name_plural = ("Kurslar")

class Lesson(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_name_lesson")
    theme = models.CharField(max_length=50)
    completed = models.ManyToManyField(User, related_name='lesson_completed', blank=True)
    lock = models.ManyToManyField(User,related_name="lesson_lock", blank=True)

    def __str__(self):
        return f"{self.course_name} ---- {self.theme}"
    class Meta:
        verbose_name = ("Dars ")
        verbose_name_plural = ("Darslar")


class PageOfCourse(models.Model):
    page_image = models.ImageField(blank=True, upload_to="imgs/page_imgs/")
    lesson_name = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    context = models.TextField(blank=True, null=True)
    completed =models.ManyToManyField(User, related_name="page_completed", blank=True)

    def __str__(self):
        return f"{self.lesson_name.theme} ---- {self.id}-DARS"

    class Meta:
        verbose_name = ("SAHIFA ")
        verbose_name_plural = ("SAHIFALAR")
    

class Quiz(models.Model):
    page = models.ForeignKey(PageOfCourse, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100, blank=True)
    completed = models.ManyToManyField(User, related_name='quiz_completed', blank=True)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = ("TEST ")
        verbose_name_plural = ("TESTLAR")


class Choice(models.Model):
    question = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)   
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = ("VARIANT ")
        verbose_name_plural = ("VARIANTLAR")


class InputQuiz(models.Model):
    page = models.ForeignKey(PageOfCourse, on_delete=models.CASCADE)
    question = models.CharField(max_length=100, blank=True)
    answer = models.CharField(max_length=50)
    # endings = RichTextField(blank=True, null=True)
    endings = models.CharField(max_length=30, blank=True, null=True)
    completed = models.ManyToManyField(User, related_name="inputquiz_completed", blank=True)
    new_line = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} {self.id}"

    class Meta:
        verbose_name = ("OCHIQ TEST ")
        verbose_name_plural = ("OCHIQ TESTLAR")


class Tips(models.Model):
    page = models.ForeignKey(PageOfCourse, on_delete=models.CASCADE)
    tip = models.TextField()

    def __str__(self):
        return self.tip

    class Meta:
        verbose_name = ("ESLATMA ")
        verbose_name_plural = ("ESLATMALAR")


class Code_snippet(models.Model):
    page = models.ForeignKey(PageOfCourse, on_delete=models.CASCADE)
    code = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = ("KOD ")
        verbose_name_plural = ("KODLAR")

