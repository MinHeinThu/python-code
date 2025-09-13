// Array is like store data in a list 
// Same as python list
let array = [1, 2, 3, 5, 2]; 
// in python list
// array = [1,3]
// we have methods 
array.pop(); // remove from end of array
console.log(array); // In python array.pop()

array.push(3); // Add in the end
console.log(array); // In python array.push(3)

array.shift(); // Remove from the beginning
console.log(array) // In python we need to pop() at index zero

array.unshift(10); // Add in the start
console.log(array);

console.log(array.indexOf(10)); // Find the inde in python .index(10)

const new_str = array.join(""); // Convert to string
console.log(new_str);

console.log(array.includes(3));

// console.log(array.slice(1, 3)); // start to end copy part

// console.log(array.splice(1, 3)); // index , count like from indext and total is upto 3

const square = array.map((x) => x ** 2);
console.log(square);

const sq = (x) => x * 2;
console.log(sq(5));

const able = array.filter((x) => x % 2 === 0);
console.log(able);

// Tenary operator in JavaScript

let x = 5;
let result = (x > 0) ? "Positive" : "Negative";
console.log(result);

// result = 'Positive' if x > 0 else "Negative"
