// array is ordered collections of items or objects like a list
// we can access by indexing the array value

let fruits = ["jackfruit", "apple", "pineapple"]
console.log(fruits[0]) // index is always start from zero

// we can aslo update array by indexing
fruits[1] = "mango";
console.log(fruits)

// This part is some useful array methods 

fruits.push("apple"); // push is add at end of array
console.log(fruits)

fruits.pop(); // pop() methond is to pop the value end of array
console.log(fruits)

fruits.shift();// remove from start like pop(0)
console.log(fruits);

fruits.unshift("durian"); // add at start like insert(index: 0, element: value)
console.log(fruits)

console.log(fruits.length);

// looping and  iteration 
// forEach() runs a function on evry element

let nums = [1, 2, 3];
nums.forEach(num => console.log(num));
