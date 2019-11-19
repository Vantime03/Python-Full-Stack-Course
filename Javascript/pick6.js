const readline = require('readline-sync');

function winning_number() {
    let count = 0;
    let win_numb = [];
    while (count < 6) {
        let draw = Math.ceil(Math.random()*99);
        if (win_numb.includes(draw) == true) {
            break;
        }
        win_numb.push(draw);
        count = count + 1;
    }
    
    //win_numb.sort(function(a,b) {return a-b}); //this will sort in order
    return win_numb;
}

function ticket_number() {
    let count = 0;
    let ticket_numb = [];
    while (count < 6) {
        let draw = Math.ceil(Math.random()*99);
        if (ticket_numb.includes(draw) == true) {
            break;
        }
        ticket_numb.push(draw);
        count = count + 1;
    }

    //ticket_numb.sort(function(a,b) {return a-b}); //this will sort in order
    return ticket_numb;
}

function num_matches (winning, ticket) {
    let match_count = 0;

    let winning_dict = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    };

    // for (x in winning) {
    //     for (y in ticket) {
    //         if (winning[x] == ticket[y]){
    //             match_count = match_count + 1; 
    //         }
    //     }
    // }

    for (x in winning) {
        if (winning[x] == ticket[x]) {
            match_count++; 
        }
    }

    return winning_dict[match_count];
}

function main() {
    let wallet = 100000;
    const original_wallet = wallet;
    let net_winning = 0;
    let round = 0;
    let count_4 = 0;
    let count_7 = 0;
    let count_100 = 0;
    let count_50000 = 0;
    let count_1000000 = 0;
    let count_25000000 = 0;
    


    while (wallet != 0) {
        round = round + 1; 
        wallet = wallet - 2;

        let x = winning_number(); 
        let y = ticket_number();
        // console.log("The winning number is  " + x);
        // console.log("The ticket number is   " + y);
        let netWinCurrentPick = num_matches(x, y);

        if (netWinCurrentPick == 4) {
            count_4 = count_4 + 1;
        } else if (netWinCurrentPick == 7) {
            count_7 = count_7 + 1;
        } else if (netWinCurrentPick == 100) {
            count_100 = count_100 + 1;
        } else if (netWinCurrentPick == 50000) {
            count_50000 = count_50000 + 1;
        } else if (netWinCurrentPick == 1000000) {
            count_1000000 = count_1000000 + 1;
        } else if (netWinCurrentPick == 25000000) {
            count_25000000 = count_25000000 + 1;
        }

        net_winning = net_winning + netWinCurrentPick;
        // console.log("Round " + round +  ": $" + netWinCurrentPick);     
    }
    
    const winning_ratio = (net_winning/original_wallet) * 100;

    console.log("winning ratio: " + Math.round(winning_ratio) + "%");
    console.log("Net win: $" + net_winning);
    console.log("# of $4 win: " + count_4);
    console.log("# of $7 win: " + count_7);
    console.log("# of $100 win: " + count_100);
    console.log("# of $50000 win: " + count_50000);
    console.log("# of $1000000 win: " + count_1000000);
    console.log("# of $25000000 win: " + count_25000000);

}

main()

