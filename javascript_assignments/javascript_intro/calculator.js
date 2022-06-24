var numberOne = parseInt(window.prompt("Enter the greater number: ")) ;

alert("The first number is " + numberOne + " correct?");

var numberTwo = parseInt(window.prompt("Enter the lesser number: "));

alert("The second number is " + numberTwo + " correct? ");

var option = window.prompt(`
**********Help**********
select what you want to do...
a for addition
s for subtraction
m for multiplication
d for division
`);

var answer;

if ((option == "a")) {
  answer = numberOne + numberTwo;
} else if ((option == "s")) {
  answer = numberOne - numberTwo;
} else if ((option == "m")) {
  answer = numberOne * numberTwo;
} else if ((option == "d")) {
  answer = numberOne / numberTwo;
} else {
  window.prompt("You did not select a valid option. Try again... ");
}

window.prompt("The answer is "+ answer)