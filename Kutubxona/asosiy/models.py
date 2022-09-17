from django.db import models

import random
from random import randint




class Student(models.Model):
    ism=models.CharField(max_length=50)
    st_raqam=models.PositiveSmallIntegerField()
    guruh=models.CharField(max_length=10)
    bitiruvchi=models.BooleanField(default=False)
    kitob_soni=models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return  self.ism


class Muallif(models.Model):
    ism=models.CharField(max_length=50)
    jins=models.CharField(max_length=10, choices=(("Man", "Man"), ("Woman", "Woman")))
    tirik=models.BooleanField()
    tugulgan_yil=models.DateField()
    kitob_soni=models.IntegerField()
    def __str__(self):
        return  self.ism

class Kitob(models.Model):
    JANR=[
        ("Badiiy","Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli"),
        ("Detektiv","Detektiv"),
    ]
    nom=models.CharField(max_length=30)
    sahifa=models.IntegerField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    janr=models.CharField(max_length=30, choices=JANR)
    def __str__(self):
        return self.nom

class Record(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob, on_delete=models.CASCADE)
    olingan_sana=models.DateTimeField(auto_now_add=True)
    qaytarish_sana=models.DateTimeField(null=True, blank=True)
    qaytardi=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.student}"


