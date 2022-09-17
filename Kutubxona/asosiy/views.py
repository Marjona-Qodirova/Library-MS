from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from.forms import *





# def home(request):
#     return HttpResponse("Salom Dunyo")



def asosiy(request):
    return render(request, 'asosiy.html')


def friends(request):
    l=["Ali", "Nozim", "Kamol"]

    return render(request, 'table.html', {"names":l})
def all_students(request):
    if request.method=='POST':
        forma=StudentForm(request.POST)
        if forma.is_valid():
            Student.objects.create(
                ism=forma.cleaned_data.get("ism"),
                st_raqam=forma.cleaned_data.get("st_raqam"),
                guruh=forma.cleaned_data.get("guruh"),
                bitiruvchi=forma.cleaned_data.get("bitiruvchi"),
                kitob_soni=forma.cleaned_data.get("kitob_soni"),

            )
            return redirect("/students/")
    #     if request.POST.get('b')=='on':
    #         bitiruvchi_st=True
    #     else:
    #         bitiruvchi_st=False

    #
    #
    #     Student.objects.create(
    #         ism=request.POST.get("i"),
    #         st_raqam=request.POST.get("st"),
    #         guruh=request.POST.get("g"),
    #         kitob_soni=request.POST.get("k"),
    #         bitiruvchi=bitiruvchi_st
    #     )
    #     return redirect("/students/")

    qidiruv_sozi=request.GET.get("soz")
    if qidiruv_sozi is None:
        talabalar = Student.objects.all()
    else :

        talabalar = Student.objects.filter(ism__contains=qidiruv_sozi)

    data={

        "students":talabalar,
        "forma":StudentForm()
    }
    return render(request, "students.html", data)

def hamma_mualliflar(request):
    if request.method=='POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            Muallif.objects.create(
                ism=forma.cleaned_data.get("ism"),
                jins=forma.cleaned_data.get("jins"),
                tirik=forma.cleaned_data.get("tirik"),
                tugulgan_yil=forma.cleaned_data.get("tugulgan_yil"),
                kitob_soni=forma.cleaned_data.get("kitob_soni"),

            )
            return redirect("/muallif/")
        # if request.POST.get('t')=='on':
        #     tirik_muallif=True
        # else:
        #     tirik_muallif=False
        # Muallif.objects.create(
        #     ism=request.POST.get("i"),
        #     jins=request.POST.get("j"),
        #     tirik=tirik_muallif,
        #     tugulgan_yil=request.POST.get("t_y"),
        #     kitob_soni=request.POST.get("k"),
        #
        # # )
        # return redirect("/muallif/")

    yozuvchilar=Muallif.objects.all()
    data={
        "mualliflar":yozuvchilar,
        "forma": MuallifForm()
    }
    return render(request, "mualliflar.html",data)
def bitta_student(request, son):
    data={
        "talaba": Student.objects.get(id=son)

    }
    return render(request, "student.html", data)

def qarzdorlar(request):
    data={
        "students":Student.objects.filter(kitob_soni__gte=0)
    }
    return render(request, "qarzdor_studentlar.html",data)
def student_ochir(request, t_id):
    Student.objects.filter(id=t_id).delete()
    return redirect("/students/")

def hamma_kitoblar(request):
    if request.method=='POST':
        forma=KitobForm(request.POST)
        if forma.is_valid():
            Kitob.objects.create(
                nom=forma.cleaned_data.get("nom"),
                sahifa=forma.cleaned_data.get("sahifa"),
                janr=forma.cleaned_data.get("janr"),
                muallif=forma.cleaned_data.get("muallif"),
            )
            return redirect("/books/")
    k1=Kitob.objects.all()
    data={
        "kitoblar":k1,
        "mualliflar": Muallif.objects.all(),
        "k":KitobForm()

    }
    return render(request,"kitoblar.html" , data)


def hamma_recordlar(request):
    if request.method=='POST':
        forma=RecordForm(request.POST)
        if forma.is_valid():
            forma.save()

            # s1=Student.objects.get(id=request.POST.get('st'))
            # s1.kitob_soni+=1
            # s1.save()
        return redirect("/recordlar/")



    r1=Record.objects.all()
    data={
        "records":r1,
        "students":Student.objects.all(),
        "kitoblar":Kitob.objects.all(),
        "f":RecordForm()

    }
    return render(request,"recordlar.html" , data)

def students_edit(request, son):
    if request.method=='POST':
        if request.POST.get('t') == 'on':
            bitiruvchi = True
        else:
            bitiruvchi= False

        Student.objects.filter(id=son).update(
        ism=request.POST.get("i"),
        st_raqam=request.POST.get("st"),
        guruh=request.POST.get("g"),
        bitiruvchi=bitiruvchi,
        kitob_soni=request.POST.get("k")
    )
        return redirect("/students/")

    data={
        "talaba":Student.objects.get(id=son)
    }
    return render(request, "student-edit.html", data)
def record_edit(request, son):
    r1= Record.objects.get(id=son)
    if request.method=='POST':
        if not r1.qaytarish_sana:
            r1.qaytarish_sana=request.POST.get("qaytarish_sana")
            r1.qaytardi=True
            r1.save()
        return redirect("/recordlar/")
    data={
        "record":r1
    }
    return render(request, "record_edit.html", data)

def muallif_edit(request, son):
    if request.method=='POST':
        if request.POST.get('t') == 'on':
            tirik_muallif = True
        else:
            tirik_muallif= False

        Muallif.objects.filter(id=son).update(
            ism=request.POST.get("i"),
            jins=request.POST.get("j"),
            tirik=tirik_muallif,
            kitob_soni=request.POST.get("k"),
        )
        return redirect("/muallif/")

    data = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, "muallif_edit.html", data)

def kitob_edit(request, son):
    if request.method=='POST':
        Kitob.objects.filter(id=son).update(
            nom=request.POST.get("n"),
            sahifa=request.POST.get("s"),
            janr=request.POST.get("j"),


        )
        return redirect("/books/")
    data={
        "kitob":Kitob.objects.get(id=son)
    }
    return render(request, "kitob_edit.html",data)
