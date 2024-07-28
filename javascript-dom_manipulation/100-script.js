/* eslint-disable */
document.addEventListener('DOMContentLoaded', () => {
  const myList = document.querySelector('.my_list');

  const addButton = document.getElementById('add_item');
  addButton.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    newItem.classList.add('new_item');
    myList.appendChild(newItem);
  }); // add new item

  const removeButton = document.getElementById('remove_item');
  removeButton.addEventListener('click', () => {
    const firstNewItem = document.querySelector('.new_item');
    if (firstNewItem) {
      myList.removeChild(firstNewItem);
    }
  }); // remove a element

  const clearButton = document.getElementById('clear_list');
  clearButton.addEventListener('click', () => {
    while (myList.firstChild) {
      myList.removeChild(myList.firstChild);
    }
  }); // clear the list
});
