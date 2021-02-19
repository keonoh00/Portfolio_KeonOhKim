// Alert creates error pop up;
alert("I have to work hard");

// console.log does not appear on the browser but prints on console
console.log("You also have to work hard")


// let, var, const exists const cannot be changed
let A = 221;
let B = A - 9;
console.log(B);

/* multi=line comment */


// Data type Array
// Use camelcase for javascript --> not wrong but most people uses camelcase
const daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

// Data type Object
const keonohInfo = {
    name: "Keon Oh Kim", 
    age: 23, 
    gender: "Male", 
    nationality: "Korean", 
    favFood: [
        {
            name: "Something",
            color: "someColor"
        },
        {
            name: "something2", 
            color: "someColor"
        }
    ]
}

// To call or modify object
console.log(keonohInfo.name);
keonohInfo.age = 10;

// Creating a function
// Backtick to create a string with variable inside
function sayHello(name, age){
    console.log(`Hello, ${name} you are ${age} years old`)
    return `Hello, ${name} you are ${age} years old`
}

const greeting = sayHello("name", 23)

console.log(greeting)

const calculator = {
    plus: function(a, b){
        return a + b;
    }
}

console.log(calculator.plus(4, 7))


// Getting something from html file
// Something that you select from the document will be an object in JS
const title = document.getElementById("title");

console.log(title)

title.innerHTML = "Hi! from Javascript"