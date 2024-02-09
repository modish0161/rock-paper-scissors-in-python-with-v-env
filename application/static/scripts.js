document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("#choices button");
    buttons.forEach(button => {
        button.addEventListener("click", function() {
            const userChoice = this.getAttribute("id");
            playGame(userChoice);
        });
    });
});

function getComputerChoice() {
    const choices = ['rock', 'paper', 'scissors'];
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
}

function determineWinner(userChoice, computerChoice) {
    if (userChoice === computerChoice) {
        return "It's a tie!";
    }

    const rules = {
        rock: 'scissors',
        paper: 'rock',
        scissors: 'paper'
    };

    if (computerChoice === rules[userChoice]) {
        return 'You win!';
    } else {
        return 'You lose!';
    }
}

function playGame(userChoice) {
    const computerChoice = getComputerChoice();
    const result = determineWinner(userChoice, computerChoice);

    document.getElementById('user-choice').innerHTML = `You chose: ${userChoice}`;
    document.getElementById('computer-choice').innerHTML = `Computer chose: ${computerChoice}`;
    document.getElementById('game-result').innerHTML = `<strong>${result}</strong>`;
}