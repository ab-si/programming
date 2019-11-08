'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function reverse(arr) {
    arr.reverse()
    for (let i=0; i<arr.length; i++) {
        process.stdout.write(`${arr[i]} `);
    }
}

function main() {
    // Send your input as "printf "1 2 3 5\n" | node filename.js"
    const n = parseInt(readLine(), 10);
    const arr = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    reverse(arr);
}
