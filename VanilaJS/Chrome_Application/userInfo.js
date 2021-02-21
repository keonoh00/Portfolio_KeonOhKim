// querySelector takes the first selector in CSS way
// Other method is querySelectorAll takes all the selector and returns the array of the selectors
const form = document.querySelector(".js-form");
const userName = form.querySelector("input");
const greeting = document.querySelector(".js-gre");

const USER_LS = "currentUser";
const SHOWING_CN = "showing";

function saveUser(text) {
    localStorage.setItem(USER_LS, text);
}

function handleSubmit(event) {
    // preventDefault is used to block refreshing of the website
    event.preventDefault();
    // initialize and set currentValue as userName.value
    const currentValue = userName.value;
    // activate paintGreeting for instant change after the submit
    paintGreeting(currentValue);
    // save the username to allow user to continuously activate
    saveUser(currentValue);
}

function paintGreeting(text) {
    // remove css of with SHOWING_CN --> "showing" which visualize the block in other words the form will
    // not be visible
    form.classList.remove(SHOWING_CN);
    greeting.classList.add(SHOWING_CN);
    greeting.innerText = `Hello ${text}`;
}

function askForName() {
    // the from block will be visible
    form.classList.add(SHOWING_CN);
    // When somthing is submited to the form then activate handleSubmit
    form.addEventListener("submit", handleSubmit);
}


// get the value on the local storage and if there is no value set, then will ask for name
// else paintGreeting
function loadName() {
    const currentUser = localStorage.getItem(USER_LS);
    if (currentUser === null) {
        askForName();
    } else {
        paintGreeting(currentUser);
    }
}


function init() {
    loadName();
}

init();