document.getElementById('search').addEventListener('click', () => {
    let zipcode = document.getElementById('zipcode').value
    const url = `https://api.openweathermap.org/data/2.5/weather?zip=${zipcode}&units=imperial&appid=${key}`

    axios.get(url)

        .then(function (response) {

            document.getElementById('mapid').remove()

            // display temperature
            let temp = document.getElementById('currentTemperature')
            // temp.setAttribute('class', 'card light-blue darken-1' )
            temp.innerHTML = `Current Temperature: ${response.data.main.temp} &#8457`

            let desc = document.getElementById('description')
            // desc.setAttribute('class', 'card light-blue darken-1' )
            desc.innerHTML = `Current Condition: ${response.data.weather[0].description}`

            let windspeed = document.getElementById('windSpeed')
            // windspeed.setAttribute('class', 'card light-blue darken-1' )
            document.getElementById('windSpeed').innerHTML = `Wind Speed: ${response.data.wind.speed} Mi./Hr.`
            console.log(response.data);


            let map_placement = document.getElementById('map_placement')
            let map = document.createElement('div')
            map.setAttribute('id', 'mapid')
            map.setAttribute('class', 'col s12')
            map_placement.appendChild(map)



            //getting the coordinate
            let lat = response.data.coord.lat
            let long = response.data.coord.lon


            //leaflet mapping
            let mymap = L.map('mapid').setView([lat, long], 13);
            const url_map = `https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${key_map}`
            
            //marker for mapping
            var marker = L.marker([lat, long]).addTo(mymap);
            marker.bindPopup(`<b>Welcome to ${response.data.name}!</b><br>`).openPopup();

            L.tileLayer(url_map, {
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox/streets-v11',
                accessToken: 'your.mapbox.access.token'
            }).addTo(mymap);

        })
        .catch(error => console.log(error))

})

