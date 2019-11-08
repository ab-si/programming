/*
We define super digit of an integer x using the following rules:

    Given an integer, we need to find the super digit of the integer.
    If x has only 1 digit, then its super digit is x.
    Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
*/
'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function superDigit(n, k) {
    if (n < 10) {
        return n;
    }

    return superDigit(
        n
        .toString()
        .split('')
        .reduce((sum, num) => sum + (num | 0), 0) * k,
        1);
}

function main() {
    // Send your input as "printf "123456 7\n" | node filename.js"
    const nk = readLine().split(' ');
    const n = nk[0];
    const k = parseInt(nk[1], 10);
    const result = superDigit(n, k);
    console.log(result)
}
