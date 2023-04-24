from django.forms import model_to_dict
from django.shortcuts import render, redirect
from form.models import Form
# from django.views import View
# from .form import UpdateForm


def fetch():
    data = Form.objects.all()
    return data


def base(request):

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        profile_pic = request.FILES['file']
        insert = Form(name=name, age=age, email=email, profile_pic=profile_pic)
        insert.save()
        msg = {
            'msg': 'Successful',
            'color': 'success',
            'data': fetch()
        }
        return render(request, 'form.html', msg)
    else:
        model_data = {
            'data': fetch()
        }
        return render(request, 'form.html', model_data)


def edit(request, id):
    data = {
        'get': Form.objects.get(id=id)
    }
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        file = request.POST['file']
        updateEmp = Form.objects.filter(id=id).update(
            name=name, age=age, email=email ,file=file)
        print('Update status:', updateEmp)
        data = fetch()
        d = {
            'data': data
        }
        return redirect('/', d)

    return render(request, 'edit.html', data)


def destroy(request, id):
    if request.method == 'GET':
        Form.objects.get(id=id).delete()
        d = {
            'data': fetch()
        }
        return redirect('/',d)




