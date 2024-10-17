from django.shortcuts import render,get_object_or_404
from .models import Apartment, Areas
import folium
from .forms import AreasForm


def index(request):
    # apartments = Apartment.objects.all().values()
    area = Areas.objects.first()
    apartments = Apartment.objects.filter(area=area).values()
    initial_data = {'area': area.id}
    form = AreasForm(initial=initial_data)
    cordinate = [area.location.latitude, area.location.longitude]
    folium_map = folium.Map(location=cordinate, zoom_start=15).add_child(folium.LatLngPopup())
    # folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community').add_to(folium_map)
    folium.TileLayer('https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.jpg?api_key=73c03d7d-7ca4-4fd0-8d2a-b1d88dcdb6b1',attr='&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors').add_to(folium_map)
        
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
    context = {'mapping':mapping, 'form':form}
    return render(request, 'index.html',context)
 
def detail(request,pk):
    apartment = get_object_or_404(Apartment, id=pk)
    context = {'apartment':apartment}
    return render(request, 'detail.html', context)

def get_map(request):
    if request.method == 'POST':
        place = request.POST.get('area')
        area = get_object_or_404(Areas, id=place)
        apartments = Apartment.objects.filter(area=area).values()
        cordinate = [area.location.latitude, area.location.longitude]
        folium_map = folium.Map(location=cordinate, zoom_start=15).add_child(folium.LatLngPopup())
        # folium.TileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community').add_to(folium_map)
        folium.TileLayer('https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.jpg?api_key=ecd208f0-15b4-4033-b5fb-be438c47318c',attr='&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',).add_to(folium_map)
            
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
                folium.Marker(icon=folium.Icon(icon="cloud"))
            else:
                folium.Marker(locate, popup=f"<a href='/apartment_detail/{apartment['id']}/' target='_top'>View apartment</a><br> "+apartment['name'],tooltip='click me!!',icon=folium.Icon(color="red")).add_to(folium_map)
                folium.Marker(icon=folium.Icon(icon="cloud"))
            locate = []

    mapping = folium_map._repr_html_()
    context = {'mapping':mapping}
    return render(request, 'partial/map.html', context)