const myGuess = 1;
const actualNum = Math.floor(Math.random() * 99);
let score = actualNum - myGuess;
if (score > 0) {
    alert (`your score is ${score}`)
} else {
    score = Math.abs (score)
    alert (`your score is ${score}`)
};
