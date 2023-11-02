from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Course, PageOfCourse, Quiz, Choice, Lesson, InputQuiz
from user.models import User
from django.contrib import messages 

from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import landscape, letter

def get_certificate(request, pk): 
    full_name = f"{request.user.first_name} {request.user.last_name}"
    course = Course.objects.get(id=pk)

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=landscape(letter), bottomup=0)

    def drawMyRuler(pdf):
        pdf.drawString(100,600, 'x100')
        pdf.drawString(200,600, 'x200')
        pdf.drawString(300,600, 'x300')
        pdf.drawString(400,600, 'x400')
        pdf.drawString(500,600, 'x500')
        pdf.drawString(600,600, 'x600')
        pdf.drawString(700,600, 'x700')

        pdf.drawString(10,0, 'y0')
        pdf.drawString(10,100, 'y100')
        pdf.drawString(10,200, 'y200')
        pdf.drawString(10,300, 'y300')
        pdf.drawString(10,400, 'y400')
        pdf.drawString(10,500, 'y500')
        pdf.drawString(10,600, 'y600')
        pdf.drawString(10,700, 'y700')
        pdf.drawString(10,800, 'y800')    

    
    c.drawImage("bg.jpeg", 0, 0, width=800,height=600)
    # drawMyRuler(c)

    c.setFont('Helvetica', 60)
    # c.setFillColorRGB(0, 0, 255)
    c.drawCentredString(400, 225, "CERTIFICATE")

    c.setFont('Helvetica', 40)
    c.drawCentredString(400, 300, course.name)

    c.setFont('Helvetica', 20)
    c.drawCentredString(400, 350, "kursimizni tamomlagani uchun")

    c.setFont('Helvetica', 40)
    c.drawCentredString(400, 400, full_name)

    c.setFont('Helvetica', 20)
    c.drawCentredString(400, 450, "taqdirlanadi")

    c.setFont('Helvetica', 20)
    c.drawCentredString(100, 500, "Director")

    c.drawImage("signature.png", 350, 470, width=100, height=50)

    c.setFont('Helvetica', 20)
    c.drawCentredString(650, 500, "Palonchiyev Pistonchi")

    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="cert.pdf ")


def coursehome(request, url_name):
    if request.user.is_authenticated:
        course_completed = Course.objects.filter(completed=request.user.id)
        completed = Lesson.objects.filter(completed=request.user.id)
        course = Course.objects.get(name=url_name.replace('-', ' ')) 
        lessons = Lesson.objects.filter(course_name=course.id)
        lesson_list = list(lessons)

        if lesson_list[0].lock.filter(id=request.user.id): 
            pass
        else:
            lesson_list[0].lock.add(request.user.id)
        
        context = {
            "url_name": url_name.title().replace('-', ' '),
            "course": course,
            "lessons": lessons,
            "completed": completed,
            "course_completed": course_completed,
        }
        return render(request, "lessons.html", context)
    else: 
        return redirect('register')
 

def check_answer(request, pk, pk2):
    if request.user.is_authenticated:
        selected_choice = Choice.objects.get(id=pk2)
        if selected_choice.is_true == True: 
            quiz = get_object_or_404(Quiz, id=pk)
            if quiz.completed.filter(id=request.user.id):
                messages.success(request, ("Javobingiz to\'g\'ri! Barakalla"))
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                user = get_object_or_404(User, id=request.user.id)
                quiz.completed.add(request.user.id)
                messages.success(request, ("Javobingiz to\'g\'ri! Barakalla"))
                return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, ("Javobingiz xato! Qaytadan urinib ko\'ring"))
            return redirect(request.META.get('HTTP_REFERER'))
    else: 
        return redirect('register')


def check_input(request, pk): 
    if request.user.is_authenticated: 
        if request.method == "POST":
            inputted = request.POST[f"answer_input_{pk}"]
            quiz = get_object_or_404(InputQuiz, id=pk)
            if quiz.answer == inputted:
                if quiz.completed.filter(id=request.user.id):
                    messages.success(request, ("Javobingiz to\'g\'ri! Barakalla"))
                    return HttpResponse("you right")
                else:
                    user = get_object_or_404(User, id=request.user.id)
                    quiz.completed.add(request.user.id)
                    messages.success(request, ("Javobingiz to\'g\'ri! Barakalla"))
                    return HttpResponse("you right")
                    # return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.success(request, ("Javobingiz xato! Qaytadan urinib ko\'ring"))
                return HttpResponse("you right")
                # return redirect(request.META.get('HTTP_REFERER'))
        else: 
            return redirect(request.META.get('HTTP_REFERER'))
    else: 
        return redirect('register')

    
def lesson(request, url_name, pk, pk2):
    if request.user.is_authenticated:
        course = Course.objects.get(name=url_name) 
        lesson = Lesson.objects.get(id=pk)
        all_pages = PageOfCourse.objects.filter(lesson_name=lesson.id)
        all_pages = list(all_pages)
        lesson_first_page = all_pages[0]
        lesson_last_page = all_pages[-1]
        pages = PageOfCourse.objects.get(id=pk2) 
        all_quizes = Quiz.objects.filter(page=pages.id)
        all_lessons = Lesson.objects.all()
        course_all_lessons = list(Lesson.objects.filter(course_name=course.id))
        input_quiz_all = InputQuiz.objects.filter(page=pk2)

        if request.method == 'POST':
            iquiz_completed_all = 1
            for iquiz in input_quiz_all:
                try:
                    inputted = request.POST[f"answer_input_{iquiz.id}"]
                    quiz = get_object_or_404(InputQuiz, id=iquiz.id)
                    if quiz.answer.lower() == inputted.lower():
                        iquiz_completed = 1
                        if quiz.completed.filter(id=request.user.id):
                            pass
                        else:
                            quiz.completed.add(request.user.id)
                    else:
                        iquiz_completed = 0
                except:
                    pass
            iquiz_completed_all *= iquiz_completed
            if iquiz_completed_all == 0:
                messages.success(request, ("Javobingiz xato! Qaytadan urinib ko\'ring"))
            else:
                messages.success(request, ("Javobingiz to\'g\'ri! Barakalla"))
            return redirect(request.META.get('HTTP_REFERER'))
        else: 

            # COURSE
            if course.active.filter(id=request.user.id): 
                pass
            else: 
                course.active.add(request.user.id)

            course_is_completed_all = 1
            for p in all_lessons:
                if p.completed.filter(id=request.user.id): 
                    is_completed = 1
                else:
                    is_completed = 0
                course_is_completed_all = course_is_completed_all * is_completed

            if course_is_completed_all == 1:
                if course.completed.filter(id=request.user.id):
                    pass
                else:
                    course.completed.add(request.user)

            # LESSON
            if lesson in course_all_lessons:
                try:
                    next_lesson = course_all_lessons.index(lesson) + 1 
                    next_lesson = course_all_lessons[next_lesson]
                    next_l = Lesson.objects.get(id=next_lesson.id)
                    try: 
                        lesson == next_l.course_name
                    except:
                        next_lesson = 0
                except:
                    next_lesson = 0
                # try:
                    # prev_lesson = course_all_lessons.index(lesson) - 1 
                    # prev_lesson = course_all_lessons[prev_page]
                    # prev_l = Lesson.objects.get(id=prev_lesson.id)
                    # try: 
                        # lesson == prev_l.course_name
                    # except:
                        # prev_lesson = -1
                # except:
                    # prev_lesson = -1
            else:
                pass


            # PAGES
            is_completed_all = 1
            for p in all_pages:
                if p.completed.filter(id=request.user.id): 
                    is_completed = 1
                else:
                    is_completed = 0
                is_completed_all = is_completed_all * is_completed
            if is_completed_all == 1: 
                if lesson.completed.filter(id=request.user.id):
                    try:
                        if next_lesson.lock.filter(id=request.user.id): 
                            pass
                        else:
                            next_lesson.lock.add(request.user.id)
                    except:
                        pass
                else:
                    lesson.completed.add(request.user)
                    request.user.xp += 10
                    request.user.save()
                    try:
                        if next_lesson.lock.filter(id=request.user.id): 
                            pass
                        else:
                            next_lesson.lock.add(request.user.id)
                    except:
                        pass
            if pages.completed.filter(id=request.user.id):
                pass
            else:
                pages.completed.add(request.user)
                # request.user.xp += 1
                # request.user.save()
                course = Course.objects.get(name=url_name) 

            if pages in all_pages:
                try:
                    next_page = all_pages.index(pages) + 1 
                    next_page = all_pages[next_page]
                    next_p = PageOfCourse.objects.get(id=next_page.id)
                    try: 
                        lesson == next_p.lesson_name
                    except:
                        next_page = 0
                except:
                    next_page = 0
                try:
                    prev_page = all_pages.index(pages) - 1 
                    prev_page = all_pages[prev_page]
                    prev_p = PageOfCourse.objects.get(id=prev_page.id)
                except:
                    prev_page = 0
            else:
                pass


            # QUIZ
            is_completed_all_quizes = 1
            for q in all_quizes:
                if q.completed.filter(id=request.user.id): 
                    is_completed_quiz = 1
                else:
                    is_completed_quiz = 0
                is_completed_all_quizes = is_completed_all_quizes * is_completed_quiz
            for q in input_quiz_all:
                if q.completed.filter(id=request.user.id): 
                    is_completed_quiz = 1
                else:
                    is_completed_quiz = 0
                is_completed_all_quizes = is_completed_all_quizes * is_completed_quiz

                
            # try: 
            #     next_lesson = Lesson.objects.get(id=pk+1)
            #     try:
            #         course == next_lesson.course_name
            #     except:
            #         next_lesson = 0
            # except:
            #     next_lesson = 0

            context = {
                "course": course,
                "lesson": lesson,
                "url_name": url_name,
                "lesson_first_page": lesson_first_page,
                "lesson_last_page": lesson_last_page,
                "next_lesson": next_lesson,
                # "prev_lesson": prev_lesson,
                "prev_page": prev_page,
                "next_page": next_page,
                "current_pk": pk,
                "pages": pages,
                "all_pages": all_pages,
                "all_quizes": all_quizes,
                "is_completed_all_quizes": is_completed_all_quizes,
            }
            return render(request, "page.html", context)
    else: 
        return redirect('register')


 