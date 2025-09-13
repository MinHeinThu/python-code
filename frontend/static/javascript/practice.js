// Closure 
/* Closure is when a function remembers the variables from the outer scope, even after that outer function has finished running. */

function greet (name) {
    return function () {
        console.log(`Hello, ${name}`);
    };
}

let hi = greet("Min")
hi()

function counter() {
    let count = 0;

    return function () {
        count ++;
        return count;
    };
}

const c = counter();

console.log(c());
console.log(c());

// Destructuring in JavaScript (Cleanear code, fewer lines)

const arr = [1, 2, 3, 4];

const [a, b, e, d] = arr;

console.log(e);

const person = {user_name: "jack", user_age: 22};
const {user_name , user_age} = person;

console.log(user_age);

// Rename in Destructuring
const{user_name: my_name} = person;
console.log(my_name);

// Spread and Rest operators (...) 

// Spread - Unpack values
const arr1 = [1, 2];
const arr2 = [...arr1, 3, 4];
console.log(arr2);

function sum(...nums) {
    return nums.reduce((a,b) => a + b, 0);
}
console.log(sum(1,2,3,4));

// Callbacks
// A function as an argument to another function, to be called later.

function greetUser(name, callback) {
    console.log(`HI ${name}`);
    callback();
}

greetUser("min", () => console.log("Welcome!"));

// Promises 
/* A promise is an object representing the future result of an asynchronous operation. */

const fetchData = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
        resolve("Data loaded");
    } else {
        reject ("Error loading data");
    }
});

