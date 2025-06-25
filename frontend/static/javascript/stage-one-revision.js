// Variables

let x = 5;
const name = "someone";
var z = 3; // function-scoped, outdated


// Data Types in JavaScript
/* String/ str
Number/ int/float
Boolean/ bool
Null/none
undefined/
Object/
Symbol/
 */

// Data types in python
// str
// int/float
// bool
// none
// typle
// dict
// set
// list

// Types Checking
// typeof (in python type())

// Ternary operator
let age = 19;
let result = age >= 18 ? "Adult" : "Minor";

// In python

// age_checking = "adult" if age >= 18 else "Minor";

function greet() {
    return "Holal";
}

greet();

let greeting = (name) => {
    return "Hello " + name;
}

console.log(greeting("Jack"));

const binarySearch = (arr, target) => {
    let l = 0;
    let r =arr.length - 1;

    while (l <= r) {
        let floor = Math.floor((r - l) / 2);
        let m = l + floor;
        console.log(m);

        if (arr[m] == target) {
            console.log(true);
            return
        } else if (target < arr[m]) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }

    return console.log(false);
}

let array = [1,2,3,4,5, 6, 7, 8];

binarySearch(array, 8);


// looping through objects


const user = {
    name: "Jackku",
    age: 20,
    country: "Thailand",
};

for (let key in user) {
    console.log(key, "=", user[key]);
}

(function() {
  console.log("I run immediately!");
})();


// Error handling in JavaScript

try {
    let age = - 5;
    if (age < 0) {
        throw new Error("Age cannot be negative");
    }
} catch (err) {
    console.log("Caught an error:", err.message);
}

const userName = "Jack";
const userAge = "20";
console.log(`Hello, my name is ${userName} and I'm ${userAge} years old.`);