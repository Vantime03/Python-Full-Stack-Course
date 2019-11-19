const readline = require('readline-sync');

// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: {${userInput}`);


function conversion(unit_conversion, distance) {
    let dist_conversion = {
        "m-ft": 1/0.3048,
        "m-mi": 1/1609.34,
        "m-km": 1/1000,
        "ft-m": 0.3048,
        "ft-mi": 0.000189394,
        "ft-km": 0.0003048,
        "mi-m": 1609.34,
        "mi-ft": 5280,
        "mi-km": 1.60934,
        "km-m": 1000,
        "km-mi": 0.621371,
        "km-ft": 3280.84,
        "m-m": 1,
        "km-km": 1,
        "ft-ft": 1,
        "mi-mi": 1
    }

    return distance * dist_conversion[unit_conversion];
}


function main() {
    let distance_input = parseInt(readline.question('What is the distance? '));
    let input_unit = readline.question('What is the input unit? (e.g. ft,mi,m,km)');
    let output_unit = readline.question('What is the output unit? (e.g. ft,mi,m,km)');
    let concat_unit = input_unit.concat('-', output_unit);
    // console.log(`${concat_unit}`);

    let result = conversion(concat_unit, distance_input);
    console.log(`${distance_input} ${input_unit} is ${result} ${output_unit}`);
}

main();

