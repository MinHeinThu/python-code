// Normal Function

const { get } = require("http");
const { json } = require("stream/consumers");

function multiple (a, b) {
    return a * b;
}

const mul = multiple( 4, 5);
console.log(mul);

// Arrow function 
const multi  = (a, b) => {
    return a * b;
}

console.log(multi(3, 5));


// Template literals 

const name = "JavaScript";
const msg = `Hello, ${name}`;
console.log(msg)

// Destructuring

const arr  = [10, 20, 30];
const [x, y] = arr;

console.log(x);
// Destructure
const user = {
    userName : "javaScript",
    userAge : 3
};
const {userName, userAge} = user;
console.log(userName);

const arr1 = [3, 4, 6]
const arr2 = [1, 2,...arr1];
console.log(arr2);


// function sum(...numbers) {
//     return numbers.reduce((total, n) => total + n, 0);
// }

function sum(...num) {
    return num.reduce((totalSum, n) => totalSum + n, 0);// 
}

console.log(sum(1,3,4,5,6,1));
const jsonString = JSON.stringify(user);
console.log(jsonString);

const  backToObject = JSON.parse(jsonString);
console.log(backToObject);

// Revisting javaScript 

// Json (javascript object notation) is a lightweight data format used ofr data exchange between a client and a server. It's like a string version of a JavaScript object

// object of js
const phone = {brand: "vivo", model: "y29", price: "200$"};
console.log(phone.brand);

// We can change json to js object or js object to json

const jsonStr = JSON.stringify(phone);
console.log(jsonStr);
const jsObj = JSON.parse(jsonStr);
console.log(jsObj);

// fetch("http://localhost:8000/hello")
// .then(res => res.json())
// .then(data => console.log(data))
// .catch(err => console.log(err));

// Closure
function outer() {
    let count = 0;
    return function inner() {
        count++;
        console.log(count);
    };
}

const counter = outer();
counter();
counter();

async function getData() {
    try {
        const res = await fetch("http://localhost:8000/hello");
        const data = await res.json();
        console.log(data);
    } catch (err) {
        console.log("Error", err);
    }
}

getData()