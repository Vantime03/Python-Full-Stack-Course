(function() {
	Const url = 'https://jsonplaceholder.typicode.com/todos/1';
	axios.get(url)
	.then(requst => console.log(request.data))
	.catch(error => console.log(error))
})()