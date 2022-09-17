
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', asosiy),
    path('friends/', friends),
    path('students/', all_students),
    path('students/<int:son>/', students_edit),
    path('muallif/<int:son>/', muallif_edit),
    path('books/<int:son>/', kitob_edit),
    path('books/', hamma_kitoblar),
    path('recordlar/', hamma_recordlar),
    path('recordlar/<int:son>/', record_edit),
    path('muallif/', hamma_mualliflar),
    path('qarzdorlar/', qarzdorlar),
    path('student/<int:son>/', bitta_student),
    path('student_ochir/<int:t_id>/', student_ochir),
]
