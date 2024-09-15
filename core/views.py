from django.shortcuts import render,get_object_or_404
from .models import Apartment, Areas
import folium


def index(request):
    apartments = Apartment.objects.all().values()
    area = Areas.objects.first()
    cordinate = [area.location.latitude, area.location.longitude]
    folium_map = folium.Map(location=cordinate, zoom_start=15).add_child(folium.LatLngPopup())
    folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community').add_to(folium_map)
        
    locate = []
    # cordinates = []
    for apartment in apartments:
        lat = apartment.get('location').latitude
        lng = apartment.get('location').longitude
        locate.append(lat)
        locate.append(lng)
        # print(apartment.get('available'))
        if apartment.get('available'):
            folium.Marker(locate, popup=f"<a href='/apartment_detail/{apartment['id']}/' target='_top'>View apartment</a><br> "+apartment['name'],tooltip='click me!!',icon=folium.Icon(color="green")).add_to(folium_map)
        else:
            folium.Marker(locate, popup=f"<a href='/apartment_detail/{apartment['id']}/' target='_top'>View apartment</a><br> "+apartment['name'],tooltip='click me!!',icon=folium.Icon(color="red")).add_to(folium_map)
        locate = []

    mapping = folium_map._repr_html_()
    context = {'mapping':mapping}
    return render(request, 'index.html',context)

def detail(request,pk):
    apartment = get_object_or_404(Apartment, id=pk)
    context = {'apartment':apartment}
    return render(request, 'detail.html', context)