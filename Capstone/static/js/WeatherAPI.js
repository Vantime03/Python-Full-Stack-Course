function getLocation() {
    let temp  = document.getElementById("temperature").textContent

    if ( temp == '' ) {
        if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
        } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
        }
    }
}
  
function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;

    console.log(lon);
    process_data(lat, lon)
}

window.onload(getLocation())


// document.getElementById("temperature").onload = function() {getLocation()};

// if (document.getElementById("temperature").value == "Hello") {
//     window.onload(getLocation())
// }

// document.getElementById('zipcode').addEventListener('keyup', event => {
//     if (event.keyCode === 13) {
//         process_data()
//     }
// })


// document.getElementById('search').addEventListener('click', () => {
//     process_data()
// })


function process_data(lat, lon) {
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=imperial&appid=${key}`
    axios.get(url)

        .then(function (response) {

            // document.getElementById('mapid').remove()

            // display temperature
            let temp = document.getElementById('temperature')
            // temp.setAttribute('class', 'card light-blue darken-1' )
            temp.innerHTML = `${response.data.main.temp} &#8457`
            let temp_icon_tag = document.getElementById('temp-icon')
            temp_icon_tag.style.width = '5%'
            temp_icon_tag.style.height = 'auto'
            let get_image = `${response.data.weather[0].icon}`
            temp_icon_tag.setAttribute("src", `http://openweathermap.org/img/wn/${get_image}@2x.png`)
        })
        .catch(error => console.log(error))

}


