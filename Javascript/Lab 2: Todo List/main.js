let count = 0

document.querySelector('.add').addEventListener('click', event => {
    let list = document.querySelector('.list')
    let userInput = document.querySelector('.new-item')
    let newItem = document.createElement('li')

    newItem.appendChild(document.createTextNode(userInput.value))
    newItem.setAttribute('class','item-list')
    newItem.setAttribute('id', `item${count}`)
    newItem.setAttribute('oncontextmenu', `dblClick_remove('item${count}')`)
    newItem.setAttribute('onclick', `strike_through('${userInput.value}', 'item${count}')`)
    count += 1
    list.appendChild(newItem)
})



function strike_through (userInput, html_element) {
    
    let result = userInput.strike()
    document.getElementById(`${html_element}`).innerHTML = result
    document.getElementById(`${html_element}`).style.color = 'green'

}

function dblClick_remove (html_element) {
    let item = document.getElementById(`${html_element}`)
    if (confirm('Are you sure you want to remove this task?')) {
        item.remove()
    } 
}

document.querySelector('.remove').addEventListener('click', event => {
    let list = document.querySelector('.list')
    let items = document.querySelectorAll('.item-list')
    list.removeChild(items[0])
})

