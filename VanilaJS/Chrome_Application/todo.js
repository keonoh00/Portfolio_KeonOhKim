const toDoForm = document.querySelector(".js-toDoForm");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector(".js-toDoList");

const TODOS_LS = 'toDos';

let toDos = [];

function filterFn(toDo) {
    return toDo.id === 1;
}

function delToDo(event) {
    const delTarget = event.target.parentNode;
    toDoList.removeChild(delTarget);
    // filter creates a new array tha has returned true in the fuction so in this case all the remaining
    // items except the delTarget will be remaining
    const deletedToDos = toDos.filter(function(toDo){
        return toDo.id !== parseInt(delTarget.id)
    });
    toDos = deletedToDos;
    saveToDos();
}

function saveToDos() {
    // JSON.stringify converts JS objects into string 
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}

function paintToDo(text) {
    const line = document.createElement("ul");
    const delBtn = document.createElement("button");
    const span = document.createElement("span");
    const newId = toDos.length + 1;
    delBtn.innerText = "❌";
    delBtn.addEventListener("click", delToDo);
    span.innerText = text;
    line.appendChild(span);
    line.appendChild(delBtn);
    line.id = newId;
    toDoList.append(line); 
    const toDoObj = {
        text: text,
        id: newId
    };
    toDos.push(toDoObj);
    saveToDos(); 
}

function handleSubmit(event) {
    event.preventDefault();
    const currentValue = toDoInput.value;
    paintToDo(currentValue);
    toDoInput.value = "";
}

function loadToDos() {
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if (loadedToDos !== null) {
        // conversts string back to the object
        const parsedToDos = JSON.parse(loadedToDos);
        // forEach executes function on every item in the array
        parsedToDos.forEach(function(toDo){
            paintToDo(toDo.text);
        });
    }
}

function init() {
    loadToDos();
    toDoForm.addEventListener("submit", handleSubmit);
}

init();