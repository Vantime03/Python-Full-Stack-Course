//lab name: anagram
const readline = require('readline-sync');

function turn_string_to_array(user_input){
    let input_array = [];
    if (user_input == "") {return "";}
    let c = user_input[0];
    if (c != " ") { input_array.push(c);}    
    return turn_string_to_array(user_input.substr(1)) + input_array;
}

function anagram_check (user_input) {
    let first_array = [];
    let second_array = [];
    for ( let i = 0; i < user_input.length; i++) {
        if (i == 0) {first_array = turn_string_to_array(user_input[i]); }
        if (i == 1) {second_array = turn_string_to_array(user_input[i]); }
    }
    first_array = first_array.split("");
    second_array = second_array.split("");
    first_array.sort();
    second_array.sort();
    if (first_array.length != second_array.length) {return false;}
    for (i = 0; i < first_array.length; i++) {
        if (first_array[i] == second_array[i]) { continue;} 
        else {return false;}
    }
    return true;
}

function main() {
    let first_word = (readline.question("Enter the first word: ")).toLowerCase();
    let second_word = (readline.question("Enter the second word: ")).toLowerCase();
    let user_input = [first_word, second_word];    
    let Is_anagram = anagram_check(user_input); // turn input into array
    if (Is_anagram === true){
        console.log(`'${first_word}' and '${second_word}' are anagram`);
    } else {console.log(`'${first_word}' and '${second_word}' are not anagram`);}
}
main();