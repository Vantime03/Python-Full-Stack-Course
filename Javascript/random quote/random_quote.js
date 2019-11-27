function get_api () {
	const url = 'https://favqs.com/api/qotd'
	axios.get(url)
	.then(function (request) {
        let quote = request.data.quote.body
        document.getElementById("quote").innerHTML = quote 
    })
	.catch(error => console.log(error))
}

get_api()


