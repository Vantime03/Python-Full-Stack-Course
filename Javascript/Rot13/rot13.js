const readline = require('readline-sync');

// lowercase a - z = 97 - 122  | String.fromCharCode(122); | strin.charcodeat()

function encrypt (phrase) {
    phrase = phrase.toLowerCase();
    let converted_phrase = "";
    for (i = 0; i < phrase.length; i++) {
        let n = phrase.charCodeAt(i) + 13; 
        if (n > 122) {
            n = 97 + (n-122) - 1; 
        }
        let char = String.fromCharCode(n); 
        converted_phrase = converted_phrase.concat(char);
    }
    return converted_phrase;
}

function main() {
    let user_input = readline.question("Enter a phrase with only from a to z to encrypt or decrypt: ");
    let encrypted_phrase = encrypt(user_input);
    console.log(`Your encrypted or decrypted phrase is ${encrypted_phrase}`);    
    
    let try_again = readline.question("Do you want to try again (y or n) ? ");
    if (try_again == 'y') {
            main();
        } else {return; }
}
main();



