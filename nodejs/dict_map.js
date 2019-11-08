/*
Given n names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each 'name' queried, print the associated entry from your phone book on a new line
name=phoneNumber;
*/

function processData(input) {
    var tempArray = input.split("\n");
    var entriesLength = tempArray.splice(0, 1);
    var queries = tempArray.splice(entriesLength);

    for(let i=0; i<entriesLength; i++) {
        tempArray[i] = tempArray[i].split(" ");
    }
    var phonebook = new Map(tempArray);

    for (let i=0; i<queries.length; i++) {
        if(phonebook.has(queries[i])){
            console.log(queries[i] + "=" + phonebook.get(queries[i]));
        } else {
            console.log("Not found");
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
let _input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
