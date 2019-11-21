//lab name: palindrome
const readline = require('readline-sync');

function reverse_string (user_input) {
    if (user_input === "") {return "";}
    return reverse_string(user_input.substr(1)) + user_input[0];
}

function main() {
    let user_input = readline.question("Enter a phrase or word to check for palindrome: ");
    let reverse_phrase = reverse_string(user_input);
    if (user_input == reverse_phrase) {
        console.log(`${user_input} is a palindrome.`);
    }else {
        console.log(`${user_input} is not a palindrome.`);
    }
}
main();

