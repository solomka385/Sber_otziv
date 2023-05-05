import requests
from pathlib import Path
from shutil import rmtree
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import qrcode
from django.contrib.auth.models import User
from segno import helpers
from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist

@login_required
def home(request):
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            try:
                user = request.user
                number1 = form.cleaned_data['number1']
                number2 = form.cleaned_data['number2']
                number3 = form.cleaned_data['number3']
                number4 = form.cleaned_data['number4']
                number5 = form.cleaned_data['number5']
                Anketa.objects.create(user=user,
                                      number1=number1,
                                      number2=number2,
                                      number3=number3,
                                      number4=number4,
                                      number5=number5,
                                      )
                return redirect('home')
            except:
                return redirect('home')

    else:
        form = AnketaForm()
    anketa = Anketa.objects.filter(user=request.user)
    opros = Opros.objects.filter(user = request.user)
    return render(request, 'home.html', {'form': form, 'anketa': anketa, 'opros': opros})


@login_required
def transport(request):
    qr_image = True
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            user = request.user
            model = form.cleaned_data['model']
            number = form.cleaned_data['number']
            #qrcode = helpers.make_mecard(user, reading=None, email=None, phone=None, videophone=None, memo=None, nickname=None, birthday=None, url="https://metanit.com/python/recipes/4.1.php", pobox=None, roomno=None, houseno=None, city=None, prefecture=None, zipcode=None, country=None)
            #qrcode = segno.make_qr("https://metanit.com/python/recipes/4.1.php")
            qr_image = True
            url = "http://127.0.0.1:8000/anketa/"
            otzov_by = f'{user},{number}'
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            data = url + "?otzov_by=" + otzov_by
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            img.save(f'media/qr/{model}_{number}.png')

            Transport.objects.create(user=user,
                                     model=model,
                                     number=number,
                                     image=f'../media/qr/{model}_{number}.png'
                                     )
            # for path in Path('media/qr').glob('*'):
            #   if path.is_dir():
            #       rmtree(path)
            #   else:
            #       path.unlink()
            return redirect('transport')
    else:
        form = TransportForm()
    transport = Transport.objects.filter(user=request.user)
    return render(request, 'transport.html', {'form': form, 'transport': transport, 'qr_image': qr_image})


@login_required
def personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        # print(form.data)
        # user1 = request.user
        # print(user1)
        if form.is_valid():
            # try:
            user = request.user
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            job = form.cleaned_data['job']
            date_of_dirth = form.cleaned_data['date_of_dirth']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']

            Personal.objects.create(user=user,
                                    name=name,
                                    last_name=last_name,
                                    email=email,
                                    job=job,
                                    date_of_dirth=date_of_dirth,
                                    phone=phone
                                    )

            return redirect('personal')
            # except:
            # form.add_error(None, 'Ошибка добавления поста')
    else:
        form = PersonalForm()
    personal = Personal.objects.filter(user=request.user)

    return render(request, 'personal.html', {'form': form, 'personal': personal})


def anketa(request):
    url_referer = request.META.get('QUERY_STRING')
    url_referer = url_referer
    a = url_referer.find('=')
    b = url_referer.find(',')
    user = url_referer[a+1:b]
    username = user
    number = url_referer[b+1::]
    #user = 'Andrew'
    if request.method == 'POST':
        otzov_by = request.POST.get('otzov_by')
        form = OprosForm(request.POST)
        # print(form.data)
        # user1 = request.user
        # print(user1)
        if form.is_valid():
            # try:
            text = form.cleaned_data['text']
            #user = url_referer[a + 1:b]


            Opros.objects.create(text=text,
                                 user=otzov_by
                                 )
            return redirect('bay')
            # except:
            # form.add_error(None, 'Ошибка добавления поста')
    else:
        otzov_by = username
        form = OprosForm()
    opros = Opros.objects.filter(user = user)
    anketa = Anketa.objects.filter(user = user)
    return render(request, 'anketa.html', {'form': form, 'opros': opros, 'anketa': anketa, 'url': number, 'otzov_by':otzov_by})

@login_required
def support(request):
    return render(request, 'support.html', locals())

def bay(request):
    return render(request, 'bay.html', locals())
