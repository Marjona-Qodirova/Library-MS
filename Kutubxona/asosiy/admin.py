from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *
@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ("id","ism","tugulgan_yil")
    list_filter = ("tirik","jins")
    list_display = ("id","ism","tugulgan_yil", "tirik","kitob_soni")
    list_display_links = ("ism",)
    list_editable = ("tugulgan_yil","kitob_soni",)
    ordering = ("-ism","tugulgan_yil")
@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    list_filter = ("janr",)
    search_fields = ("id", "nom", "janr")
    list_display = ("id","nom","janr", "muallif", "sahifa")
    list_editable = ("janr", "sahifa",)
    list_display_links = ("id","nom",)
    autocomplete_fields = ("muallif",)
@admin.register(Student)
class StudentAdmin(ModelAdmin):
    list_filter = ("ism",)
    search_fields = ("id", "ism", "guruh",)
    list_display = ("id","ism","guruh", "bitiruvchi", "kitob_soni",)
    list_editable = ( "bitiruvchi", "kitob_soni",)
    list_display_links = ("id","ism",)


@admin.register(Record)
class RecordAdmin(ModelAdmin):
    search_fields = ("id","student",)
    list_filter = ("student","olingan_sana")
    list_display = ("id","student","kitob", "qaytarish_sana","qaytardi")
    list_display_links = ("id", "student",)
    list_editable = ( "qaytardi","qaytarish_sana",)
    autocomplete_fields = ("student", "kitob",)






