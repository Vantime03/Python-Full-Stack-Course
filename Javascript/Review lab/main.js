
function get_api() {
    const url = `https://randomuser.me/api/`
    axios.get(url)
        .then(function (response) {
            console.log(response.data);
            document.getElementById('name').innerHTML = `Name: ${response.data.results[0].name.first + " " + response.data.results[0].name.last}`
            document.getElementById('username').innerHTML = `Username: ${response.data.results[0].login.username}`
            document.getElementById('email').innerHTML = `Email: ${response.data.results[0].email}`
            document.getElementById('phone').innerHTML = `Phone: ${response.data.results[0].cell}`
            document.getElementById('street').innerHTML = `Street: ${response.data.results[0].location.street.number + response.data.results[0].location.street.name}`
            document.getElementById('city').innerHTML = `City: ${response.data.results[0].location.city}`
            document.getElementById('state').innerHTML = `State: ${response.data.results[0].location.state}`
            document.getElementById('zip').innerHTML = `Zip: ${response.data.results[0].location.postcode}`
        })
        .catch(error => console.log(error))
    
    //get cookie value
    let cookie = document.getElementById('cookie-jar').textContent

    //drop cookie
    document.getElementById('drop_cookie').textContent = cookie

    //remove cookie from jar
    document.getElementById('cookie-jar').textContent = ''
    
    //get the value from the element
    let string = document.getElementById('styleThis').textContent
    let string2 = document.getElementById('styleThis2').textContent

    style_text(string2,'styleThis2') 
    style_text(string,'styleThis')     
}

function style_text(string, elm) {
    for (i=0;i<string.length;i++) {
        let rgba = get_color()
        let placement = document.getElementById('styleText')
        let char = document.createElement('span')
        char.setAttribute('style', `color:rgba(${rgba[0]}, ${rgba[1]}, ${rgba[2]})`)
        char.setAttribute('id', `char${i}`)
        placement.appendChild(char)
        document.getElementById(`char${i}`).innerHTML = string[i]
    }
    document.getElementById(elm).remove()
}

function get_color(){
    let r = Math.ceil(Math.random()*255)
    let g = Math.ceil(Math.random()*255)
    let b = Math.ceil(Math.random()*255)
    let a = Number(((Math.random()*1)).toFixed(1))
    return [r,g,b,a]
}
get_color();
get_api();
