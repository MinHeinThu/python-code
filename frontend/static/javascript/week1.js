// Day 1: Variables, Data Types & Basic Syntax
let name = "John"; // Block-scoped, can be reasssigned
const age = 23; // block-scoped, cannot be reassigned
var city = "Bangkok"; // Function-scoped (avoid using)

// In python
// name = "John"
// age = 23

// Hands-On Practice (60 minutes)

// Exercise 1: Variable Declaration Paractice

let firstName = "Krirk";
const birthYear = 1998;
let isUniversity = true;
let major = ['ICT', 'BBA', 'Aviation'];
let person = {
    name: "John",
    age: 19,
    city: "Bangkok"
};


// This will show error 
try {
    birthYear = 2003;
}
catch(err) {
    console.log("Cannot assigne to const");
}

console.log(typeof(firstName));
console.log(typeof birthYear);

// Exercise 2: Python vs JavaScrpt Syntax
// Python
// name = "Python"
// age = 35
// print(f"Name: {name}, Age: {age}")


// JavaScript
console.log(`hello,${name}!, You are ${age} years old`);

// Dalily Challenge (30 minutes)

// Create a simple "About me" program that store adn displays your information

let userName = "JavaScript";
let userAge = 23;
let userCity = "Bangkok";
console.log(`My name is ${userName}, I am ${userAge} years old and live in ${userCity}`);

// Day 2: Functions - The JavaScript Way

// 1. Function declaration (similar to Python def.)
function greeting(name = userName, age = userAge) {
    console.log(`Hello, ${name}, So you are ${age} years old`);
}
// Calling function 
greeting();

// In python
// def greeting(name, age):
//      print(f"Hello, {name}, So you are {age} years old")

// Arrow function (shortened and ES6 version)
const greet = () => {
    return "Hello, Who's calling me?";
}
console.log(greet())

// Hands-On Practice (60 minutes)
// Exercise 1: Function Conversion
// Convert these Python functions to JavaScript:

// Python:
// def add_numbers(a, b):
//     return a + b
function addNumbers(a, b) {
    return a + b;
}
console.log(`Adding two numbers: ${addNumbers(2, 4)}`)
// def calculate_area(length, width):
//     area = length * width
//     return area
function calculateArea(length, width) {
    let area = length * width;
    return area;
}
console.log(`Calculate Area: ${calculateArea(23, 3)}`);


// Ecercise 2: Advanced Function Practice
// 1. Calculator functions:
const calculator = (num1, num2, operator) => {
    switch(operator) {
        case 'add':
            return num1 + num2;
            break
        case 'subtract':
            return num1 - num2;
            break
        case 'multiply':
            return num1 * num2;
            break
        case 'divide':
            return num2 !== 0 ? num1 / num2 : "Cannot divide by zero";
            break
        default:
            return "Invalid operator";
    }
}

console.log(calculator(10, 1, 'divide'));

// 2. Arrray processing function
const processNumbers = (number) => {
    const sum = number.reduce((acc, num) => acc + num, 0);
    const average = sum / addNumbers.length;

    return {
        sum: sum,
        average: average,
        max: Math.max(...number),
        min: Math.min(...number)
    };
};
console.log(processNumbers([1,2,3,4,5]))


// Day 3 Control Structures & Comparisons

if (userName = "JavaScript") {
    console.log(`You can access`);
} else {
    console.log('Wrong User');
}

// Important JavaScript Quirks:
// Equality comparisons - Major difference from python

console.log(5 == '5') // true (type coercion)
console.log(5 === '5') // false (strict equality)j

// Loops in JavaScript

// for loop

for (let i = 0; i <= 5; i++) {
    console.log(i, "for loop");
}

// while loop
let j = 0;
while (j <= 5) {
    console.log(j, "while loop");
    j++;
}

// do...while loop
// do...while loop
do {
    console.log(j, "do while loop");
    j++;
}
while (j <= 2);

// Comparison:
// - for loop: checks condition before each iteration, best when you know how many times to loop.
// - while loop: checks condition before each iteration, good for unknown number of iterations.
// - do...while loop: always runs at least once, checks condition after each iteration.

// for ... of (linke python for fruit in fruits)

const fruits = ['apple', 'banana', 'orange'];
fruits.push('mango');
for (const fruit of fruits){
    console.log(fruit);
}


const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;
for (const num of numbers) {
    sum += num;
}
console.log("Sum:",sum)

let max = numbers[0];
for (const num of numbers) {
    if (num > max) {
        max = num;
    }
}
console.log("Maximum:", max);

// Day 4: Objects & arrays Deep dive
// JavaScript Object

const personOne = {
    name: 'Alice',
    age: 30,
    city: 'bangkok',
    hobbies: ['reading', 'coding'],
    // Methods in objects
    ingroduce: function() {
        return `Hi, I'm ${this.name}`;
    }
};

// accessing properties
console.log(personOne.name); // Dot notation
console.log(personOne["age"]); // Bracket notation
console.log(personOne.ingroduce()); // Method call


// result = 'adult' if age > 18 else 'minor'
// Ternary operation in JavaScript
const result = age > 18 ? 'adult' : 'minor';
console.log(result);

// Array methods (siliar to python list comprehensions)

const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const total_sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(doubled, evens, total_sum);

// Day 5: Understanding this, Scope & Hoisting

// In python 'self' is explict
// In JavaScript 'this' is implicit and conte-000-p-0p0-p--00000p-00p0-pp0p-p-p-0-xt-dependent

const person_object = {
    name: "Alice",
    age: 30,

    introducing: function() {
        return `Hi, I'm ${this.name}`; // 'this'  refers to the person object
    },

    // Arrow functions don't have their own 'this'
    introduceArrow: () => {
        return `Hi, I'm ${this.name}`; // 'this' is undefined here!
    }
};

console.log(person_object.introducing());
console.log(person_object.introduceArrow());

// Scope Differneces:
// JavaScrpt has function scope and block scope

function testScope() {
    var funScope = "I'm Fun Scope";
    let bloScope = "I'm Blo Scope";

    if(true){
        var funScope2 = "Still fun";
        let bloScope2 = "Still boock";
    }

    console.log(funScope2);
    // console.log(bloScope2);
}

testScope();

// Counter object 

const counters = {
    count: 0,

    increasing: function() {
         this.count++;
        console.log(`Count is now: ${this.count}`);
    }
};

counters.increasing();
counters.increasing();