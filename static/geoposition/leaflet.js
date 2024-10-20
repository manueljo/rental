if (jQuery != undefined) {
    if (django ==  undefined) {
        var django = {
            'jQuery': jQuery,
        }
    } else {
        if (django['jQuery'] == undefined) {
            django['jQuery'] = jQuery;
        }
    }
}


(function($) {

    $(document).ready(function() {

        try {
            var _ = L; // eslint-disable-line no-unused-vars
        } catch (ReferenceError) {
            console.log('geoposition: "L" not defined. You might not be connected to the internet.');
            return;
        }
        // url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        // attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',

        $('.geoposition-widget').each(function() {
            var $container = $(this),
                $mapContainer = $('<div class="geoposition-map" />'),
                $latitudeField = $container.find('input.geoposition:eq(0)'),
                $longitudeField = $container.find('input.geoposition:eq(1)'),
                latitude = parseFloat($latitudeField.val()) || null,
                longitude = parseFloat($longitudeField.val()) || null,
                mapOptions = {
                    // url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
                    url: 'https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.{ext}?api_key=ecd208f0-15b4-4033-b5fb-be438c47318c',
                    attribution: '&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
                    ext: 'jpg',
                    // attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
                    maxZoom: 19,
                    dataZoom: 16,
                    initialZoom: 2,
                    initialCenter: [25, 0],
                    parentSelector: '#tabs',
                    isDjangoAdmin: false
                },
                mapNonProviderOptions = ['url', 'dataZoom', 'initialZoom', 'initialCenter'],
                mapProviderOptions = {},
                mapCustomOptions,
                map,
                marker;

            $mapContainer.css('height', $container.attr('data-map-widget-height') + 'px');
            mapCustomOptions = JSON.parse($container.attr('data-map-options'));
            $.extend(mapOptions, mapCustomOptions);

            for (var option in mapOptions) {
                if (mapNonProviderOptions.includes(option) === false)
                    mapProviderOptions[option] = mapOptions[option];
            }

            function setLatLng(latLng) {
                $latitudeField.val(latLng.lat);
                $longitudeField.val(latLng.lng);
            }

            function getLatLng() {
                latitude = parseFloat($latitudeField.val()) || null;
                longitude = parseFloat($longitudeField.val()) || null;
                return {lat: latitude, lng: longitude};
            }

            function mapClickListen(e) {
                setMarker(e.latlng);
            }

            function setMarker(latLng) {
                if (marker) marker.remove();
                marker = L.marker(latLng, {draggable: true});
                marker.on('dragend', function(e) {
                    setLatLng(e.target.getLatLng());
                    map.panTo(e.target.getLatLng());
                });
                marker.addTo(map);
                map.setView(latLng, mapOptions.dataZoom);
                setLatLng(latLng);
                // only one single marker allowed
                map.off('click', mapClickListen);
            }

            // create the map
            $container.append($mapContainer);
            map = L.map($mapContainer[0]).setView(mapOptions.initialCenter, mapOptions.initialZoom);
            L.tileLayer(mapOptions.url, mapProviderOptions).addTo(map);
            map.on('click', mapClickListen);

            // add a search bar
            L.Control.geocoder({
                collapsed: false,
                defaultMarkGeocode: false
            }).on('markgeocode', function(e) {
                setMarker(e.geocode.center);
            }).addTo(map);

            // set marker if model has data already
            if ($latitudeField.val() && $longitudeField.val()) {
                setMarker(getLatLng());
                map.setView(getLatLng(), mapOptions.dataZoom, {animate: false});
            }

            // listen to keyboard input
            $latitudeField.add($longitudeField).bind('keyup', function() {
                setMarker(getLatLng());
            });

            if (mapOptions.isDjangoAdmin) {
                // refresh map if active custom tab changed
                $(mapOptions.parentSelector).on('click', function() {
                    setTimeout(function() {
                        map.invalidateSize();
                    }, 400);
                });
            } else {
                // refresh map if inside jquery ui tabs widget and active tab changed
                $container.parents(mapOptions.parentSelector).on('tabsactivate', function() {
                    map.invalidateSize();
                });
            }
        });
    });
})(django.jQuery);
