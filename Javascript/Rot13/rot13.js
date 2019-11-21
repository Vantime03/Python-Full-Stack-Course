const readline = require('readline-sync');

// lowercase a - z = 97 - 122  | String.fromCharCode(122); | strin.charcodeat()

function encrypt (phrase, rotate) {
    let lower_case = 'abcdefghijklmnopqrstuvwxyz';
    let upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    // str.split("").reverse().join("");
    let converted_phrase = "";
    const rotatei = rotate; 

    for (i = 0; i < phrase.length; i++) {

        //this will skip any special characters number or spaces
        if (upper_case.includes(phrase[i]) == false && lower_case.includes(phrase[i]) == false) {
            converted_phrase = converted_phrase.concat(phrase[i]); 
            continue;
        }

        //converting captital letter
        for (c = 0; c < upper_case.length; c++) {
            if (phrase[i] == upper_case[c]) {

                if (rotatei < -26) {
                    rotate = Math.abs(rotatei % 26);
                    let n = c - rotate;
                    if (n < 0) {
                        n = 26 - (n * -1); 
                    }

                    // upper_case.split('').reverse().join('');
                    converted_phrase = converted_phrase.concat(upper_case[n]);
                    n = 0; 
                    break;
                    

                } else {
                    rotate = Math.abs(rotatei % 26);
                    let n = c + rotate;
                    if (n >= 26) {
                        n = n % 26;
                    }
                    converted_phrase = converted_phrase.concat(upper_case[n]);
                    break;
                }
            }
        }
        
        //converting lower letter
        for (c = 0; c < lower_case.length; c++) {
            if (phrase[i] == lower_case[c]) {

                if (rotatei < -26) {
                    rotate = Math.abs(rotatei % 26);
                    let n = c - rotate;
                    if (n < 0) {
                        n = 26 - (n * -1); 
                    }

                    converted_phrase = converted_phrase.concat(lower_case[n]);
                    n = 0; 
                    break;

                } else {
                    rotate = Math.abs(rotatei % 26);
                    let n = c + rotate;
                    if (n >= 26) {
                        n = n % 26;
                    }
                    converted_phrase = converted_phrase.concat(lower_case[n]);
                    break;
                }
            }
        }
        
    }
    return converted_phrase;
}

function main() {
    let rotation = parseInt(readline.question("Enter number of rotation: "));
    let user_input = readline.question("Enter a phrase with only from a to z to encrypt or decrypt: ");
    let encrypted_phrase = encrypt(user_input, rotation);
    console.log(`Your encrypted or decrypted phrase is ${encrypted_phrase}`); 
    
    let try_again = readline.question("Do you want to try again (y or n) ? ");
    if (try_again == 'y') {
            main();
        } else {return; }
}
main();



