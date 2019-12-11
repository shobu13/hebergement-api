from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render

import googlemaps

from .forms import HostedForm, BaseUserForm
from core.models import User, Hosted, City, Host


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def test(request):
    return render(request, 'core/home.html')


def hosted_register(request):
    title = "Formulaire d'inscription : Hébergé"
    if request.method == 'POST':
        form = HostedForm(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                data = form.cleaned_data
                gmap = googlemaps.Client(key='AIzaSyDTWhyU1bDH84_PXA_sN3TbB0_mRCPlawU')
                results = gmap.find_place(data['city_id'], 'textquery')['candidates']
                validate_password(data['password'])
                if len(results):
                    place = gmap.place(results[0]['place_id'])['result']
                    place_name = place['address_components'][1]['long_name']
                    location = place['geometry']['location']
                    user = User.objects.create_user(username=data['mail'], email=data['mail'],
                                                    password=data['password'])
                    user.last_name = data['last_name']
                    user.first_name = data['first_name']
                    user.phone_number = data['phone_number']
                    user.city_name = place_name
                    user.city_lat = location['lat']
                    user.city_lng = location['lng']
                    user.description = data['description']

                    new_hosted = Hosted()
                    new_hosted.localisation_radius = data['radius']
                    new_hosted.addictions = data['addictions']
                    new_hosted.video = data['file']
                    new_hosted.compensations = data['compensations']
                    new_hosted.hosted = user

                    user.save()
                    new_hosted.save()

                    return render(request, 'core/registered.html', locals())

                else:
                    form.add_error('city_id', "ville non trouvée.")
            except ValidationError as e:
                for error in e.error_list:
                    form.add_error('password', error)

    else:
        form = HostedForm()
    return render(request, 'core/register.html', locals())


def host_register(request):
    title = "Formulaire d'inscription : Hébergeur"
    if request.method == 'POST':
        form = BaseUserForm(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                data = form.cleaned_data
                gmap = googlemaps.Client(key='AIzaSyDTWhyU1bDH84_PXA_sN3TbB0_mRCPlawU')
                results = gmap.find_place(data['city_id'], 'textquery')['candidates']
                validate_password(data['password'])
                if len(results):
                    place = gmap.place(results[0]['place_id'])['result']
                    place_name = place['address_components'][1]['long_name']
                    location = place['geometry']['location']
                    user = User.objects.create_user(username=data['mail'], email=data['mail'],
                                                    password=data['password'])
                    user.last_name = data['last_name']
                    user.first_name = data['first_name']
                    user.phone_number = data['phone_number']
                    user.city_name = place_name
                    user.city_lat = location['lat']
                    user.city_lng = location['lng']
                    user.description = data['description']

                    new_host = Host()
                    new_host.hosted = user

                    user.save()
                    new_host.save()

                    return render(request, 'core/registered.html', locals())

                else:
                    form.add_error('city_id', "ville non trouvée.")
            except ValidationError as e:
                for error in e.error_list:
                    form.add_error('password', error)

    else:
        form = BaseUserForm()
    return render(request, 'core/register.html', locals())
