let age = 20;
// condition ? value_if_true : value_if_false
let result = age >= 18 ? "Adult" : "Minor";
// in python
// result = 'adult' if age >= 18 else 'minor'
console.log(result);

let yourAnswer = true;
let your_result = yourAnswer === true ? "Passed" : "Failed";
console.log(your_result);

let score = 83;

if (score >= 90) {
    console.log("Grade : A");
}else if (score < 90 && score >= 80) {
    console.log("Grade : B");
} else if (score < 80 && score >= 50 ) {
    console.log("Grade : C")
} else {
    console.log("You failed")
};

// 🎯 Practice Task
// Write a script that:

// Takes a temperature variable.
let temperature = 30;

// If temp > 30, log: "It's hot".
if (temperature > 30) {
    console.log("It's hot");
} else if (temperature >= 20 && temperature <=30){
    console.log("Nice weather");
} else {
    console.log("It's cold");
}
// If temp >= 20 && temp <= 30, log: "Nice weather".

// Else, log: "It's cold".

// Try it both with if...else and a switch version for a weather condition string.

// Want the solution? Let me know — or try firs