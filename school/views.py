from pprint import pprint

from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    student_list = Student.objects.all().prefetch_related('teacher__students').order_by(ordering)

    context = {'student_list': student_list}
    for st in student_list:
        pprint(st.teacher.all())

    return render(request, template, context)
