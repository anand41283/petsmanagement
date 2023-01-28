from django.shortcuts import render

from petsapp.forms import doctor_form, user_form


# Create your views here.
def index(request):
    return render(request,'index.html')


def admin_index(request):
    return render(request,'admin_index.html')


def doctor_reg(request):
    form=doctor_form()
    if request.method=='POST':
        form=doctor_form(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_doctor=True
            user.save()
    return render(request,'doctor_reg.html',{'form':form})




def user_reg(request):
    form=user_form()
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_user=True
            user.save()
    return render(request,'user_reg.html',{'form':form})



