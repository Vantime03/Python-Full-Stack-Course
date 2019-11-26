let count = 0

document.querySelector('.add').addEventListener('click', event => {
    let list = document.querySelector('.list')
    let userInput = document.querySelector('.new-item')
    
    let newItem = document.createElement('li')
    newItem.appendChild(document.createTextNode(`${userInput.value}`))  
    newItem.setAttribute('class','item-list')
    newItem.setAttribute('id', `item${count}`)
    newItem.setAttribute('name', 'todoitem')
    // newItem.setAttribute('oncontextmenu', `dblClick_remove('item${count}')`)
    // newItem.setAttribute('onclick', `strike_through('${userInput.value}', 'item${count}')`)
    list.appendChild(newItem)

    let checkbox = document.createElement('input')
    checkbox.type = "checkbox"
    checkbox.id = `item_checkbox${count}`  
    checkbox.setAttribute('onclick', `checked_strike('${count}')`)
    newItem.appendChild(checkbox)
    count += 1
})

function checked_strike (item){
    let selected_box = document.getElementById(`item_checkbox${item}`)
    let value = document.getElementById(`item${item}`)
    if (selected_box.checked == true) {
        value.style.textDecoration = 'line-through'
        value.style.color = 'green'

    }
}

// function strike_through (userInput, html_element) {
//     let result = userInput.strike()
//     document.getElementById(`${html_element}`).innerHTML = result
//     document.getElementById(`${html_element}`).style.color = 'green'
// }

// function dblClick_remove (html_element) {
//     let item = document.getElementById(`${html_element}`)
//     if (confirm('Are you sure you want to remove this task?')) {
//         item.remove()
//     } 
// }

document.querySelector('.remove').addEventListener('click', event => {
    let list = document.querySelector('.list')
    let items = document.querySelectorAll('.item-list')
    list.removeChild(items[0])
    let elements = document.getElementsByName('todoitem')
    
    // for (let i = 0; i < elements.length; i++) {
    //     let checkbox_item = document.getElementById(`item_checkbox${i}`)
    //     let text_item = document.getElementById(`item${i}`)
    //     if (checkbox_item.checked == true) {
    //         checkbox_item.remove()
    //         text_item.remove()
    //     }
    // }
    
})

