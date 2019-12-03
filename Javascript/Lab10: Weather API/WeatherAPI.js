document.getElementById('search').addEventListener('click', () => {
    let zipcode = document.getElementById('zipcode').value 
    const url = `https://api.openweathermap.org/data/2.5/weather?zip=${zipcode}&units=imperial&appid=${key}`

    axios.get(url)
        
    .then (function (response) {
        // console.log(response.data);
        document.getElementById('currentTemperature').innerHTML = `Current Temperature: ${response.data.main.temp}`
        document.getElementById('description').innerHTML = `Current Condition: ${response.data.weather[0].description}`
        document.getElementById('windSpeed').innerHTML = `Current Condition: ${response.data.wind.speed} miles per hour`

        console.log(response.data);
    })
    .catch(error => console.log(error))
})

