document.querySelector('.add').addEventListener('click', event => {
    let list = document.querySelector('.list')
    let userInput = document.querySelector('.new-item')
    let newItem = document.createElement('li')

    newItem.appendChild(document.createTextNode(userInput.value))
    newItem.setAttribute('class','item-list')
    list.appendChild(newItem)
})


document.querySelector('.remove').addEventListener('click', event => {
    let list = document.querySelector('.list')
    let items = document.querySelectorAll('.item-list')
    list.removeChild(items[0])
})

