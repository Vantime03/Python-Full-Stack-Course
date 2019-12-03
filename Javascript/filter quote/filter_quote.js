let keyword = ''
let combo_selection = ''

// allow user to click search to list quotes
document.getElementById('search').addEventListener('click', () => {
    keyword = document.getElementById('keyword').value
    combo_selection = document.getElementById('combo_option').value
    get_api()
})

// allow the user to use the enter key to list quotes
document.getElementById('keyword').addEventListener('keyup', event => {
    if (event.keyCode === 13) {
        keyword = document.getElementById('keyword').value
        combo_selection = document.getElementById('combo_option').value
        get_api()
    } 
})


function get_api () {
    const url = `https://favqs.com/api/quotes/?filter=${keyword}&type=${combo_selection}`

    axios.get(url, {
        headers: {
            'authorization': `Token token=${key}`
        }
    }) 
    .then(function (request) {
        let result = ""
        document.getElementById("result").removeAttribute("style")
        for (i=0;i<(request.data.quotes.length);i++) {
            result += '\"' + request.data.quotes[i].body + '\" ~ ' + request.data.quotes[i].author + '<br><br>'
        }
        document.getElementById("filter_by").innerHTML = "Quotes Filter by \"" + keyword + "\" " + combo_selection  
        document.getElementById("p2").innerHTML = result
    })
    .catch(error => console.log(error))
}

function quote_of_the_day () {
    const url = 'https://favqs.com/api/qotd'

    axios.get(url)
    .then (function (request) {
        console.log(request.data);
        let result = '\"' + request.data.quote.body + '\" ~ ' + request.data.quote.author
        document.getElementById("p1").innerHTML = result
    })
    .catch(error => console.log(error))
}

quote_of_the_day()
