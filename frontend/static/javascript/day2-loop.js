// For loop
for (let x = 0; x <= 5; x++) {
    console.log(x)
}
// while loop
let z = 0;
while (z <= 5) {
    console.log(z);
    z += 1;
}

// do...while loop

let y = 0;
do{
    console.log("I love You");
    y++;
} while (y <= 5);

// for...in vs for...of
// Both are used to loop through collections — but behave differently.

let person = {name: "jack", age : 22};
for (let key in person) {
    console.log(key, person[key]);
}

let colors = ["red", "bule", "green"];
for (let color of colors) {
    console.log(color);
};


let fruits = ["banana", "jackfruit", "mongo"];

for (let y =0; y < fruits.length; y++) {
    console.log(fruits[y]);
}

fruits[1] = 'apple';
console.log(fruits[1]);
console.log(fruits)