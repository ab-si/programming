/*
Print the result of factorial of a number using only recursion
*/

function factorial(input) {
    if (input <= 1) {
        return 1
    } else {
        return input*factorial(input-1)
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
let _input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   let res = factorial(_input);
   console.log(res);
});
