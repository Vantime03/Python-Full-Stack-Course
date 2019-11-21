//lab name: blackjack advice

const readline = require('readline-sync');

function blackjack_wizard (user_input) {
    let sum = 0;
    let card_value_dict = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "j": 10,
        "q": 10,
        "k": 10,
        "a": 11
    }
    for (let i = 0; i < user_input.length; i++) {
        if (user_input[i] == "a" && sum < 11) {
            sum = card_value_dict[user_input[i]] + sum;
            continue;
        } else if (user_input[i] == "a" && sum >= 11) {
            sum = sum + 1;
            continue;
        } else {
            sum = card_value_dict[user_input[i]] + sum;
        }
    }

    if (sum == 21) {
        return ["BlackJack", sum];
    } else if(sum == 17 || sum > 17 && sum < 21) {
        return ["Stay", sum];
    } else if (sum < 17) {
        return ["Hit", sum];
    } else {
        return ["Busted", sum];
    }
}

function main() {
    console.log("Welcome to BlackJack Advice!");
    let first_card = readline.question("What's your first card? ");
    let second_card = readline.question("What's your second card? ");
    let third_card = readline.question("What's your third card? ");
    let user_input = [first_card, second_card, third_card];
    let result = blackjack_wizard(user_input);
    console.log(`You have ${result[1]} points. ${result[0]}`);

}

main();