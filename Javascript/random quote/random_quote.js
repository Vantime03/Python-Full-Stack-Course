let Quote = []
let Tag = []

function get_api () {
    const url = 'https://favqs.com/api/quotes'

    axios.get(url, {
        headers: {
            'authorization': `Token token=${key}`
        }
    }) 
	// .then(function (request) {
    //     console.log(request.data);
    //     // let quote = request.data.quote.body
    //     // document.getElementById("quote").innerHTML = quote 
    // })
    .then(function (request) {
        console.log(request.data)
        console.log(request.data.quotes[3].author)
        let tag = []
        let quote = []
        for (i=0; i < (request.data.quotes.length); i++){
            // tag.push(request.data.quotes[i].tags[0])
            let len = (request.data.quotes[i].tags).length
            for (a=0; a<len; a++){
                let body = request.data.quotes[i].body
                let author = request.data.quotes[i].author
                quote.push([body, author])
                let Is_tag_in_array = tag.includes(request.data.quotes[i].tags[a])
                if (Is_tag_in_array == false) {
                    tag.push(request.data.quotes[i].tags[a])
                }
            }
        }
        let string = 'Filter Keywords: '
        for (i=0;i<tag.length;i++){string = string + tag[i] + ', '; if (i == tag.length-1){string += tag[i]}}
        document.getElementById("filter_list").innerHTML = string
        Tag = tag
        Quote = quote
    })
    .catch(error => console.log(error))
}

document.getElementById("search_by_tag").addEventListener('click', () => {
    search_quote();
})

function search_quote() {
    let search_value = document.getElementById("tag_textbox").value
    let Is_searchValue_in_Tag_array = Tag.includes(search_value)
    let result = `quotes with '${search_value}': <br><br>`
    let arr = []
    if (Is_searchValue_in_Tag_array == true){
        for(i=0;i<Quote.length;i++){
            let n = Quote[i].includes(search_value)
            if (n == true) {
                if (arr.includes(Quote[i]) == false){
                    arr.push([Quote[i][0], Quote[i][1]])
                }
            }
        }
        console.log(arr);
    }
    for (i=0;i<arr.length;i++){
        result += arr[i] + "<br><br>"
    }
    document.getElementById("result").innerHTML = result

}

get_api()


