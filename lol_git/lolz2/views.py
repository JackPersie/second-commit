from django.forms.forms import Form
from django.shortcuts import render
from lolz2.forms import Form_one
from lolz2.models import Result
# Create your views here.


def home(request):
    name = {
        'name': "how could this happen to me"
    }
    return render(request, 'lolz2/home.html', name)


def file_one(request):
    return render(request, 'lolz2/file_1.html')


def file_two(request):
    return render(request, 'lolz2/file_2.html')


def result(request):
    res = Result.objects.all()
    res_dic = {
        'res': res
    }
    return render(request, 'lolz2/result.html', res_dic)


def form_one(request):
    form_one = Form_one()
    if request.method == 'POST':
        form_one = Form_one(request.POST)
        if form_one.is_valid():
            form_one.save()
            return result(request)
        else:
            print('Oh crap')
    return render(request, 'lolz2/form_one.html', {'form_one': form_one})
