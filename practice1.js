// Welcome to FizzBuzz
// starting at 1 and moving to 60, print the word 'Fizz' for all numbers divisible by 3, the word 'Buzz for divisible by 5
// print 'FizzBuzz'for all divisible by 15, if it is not divisible by any, print the number


function fizzBuzz () {
    // step 1 is go through all numbers 1 to 60
    // options: for loop, while loop, or manually iterate, recursion
    for(var i = 1; i <= 60; i++){
        if(i %15 === 0){
            console.log('FizzBuzz');
        }
        else if(i %3 === 0){
            console.log('Fizz');
        }
        else if(i %5 === 0){
            console.log('Buzz');
        }
        else {
            console.log(i);
        }
    }
}

// console.log(fizzBuzz());

function fizz2(){
    for(var i = 1; i <= 60; i ++){
        var output = i;
        if(i %15 === 0){
            output = 'Fizzbuzz';
        } else if(i %5 === 0 ){
            output = 'Buzz';
        } else if(i %3 === 0){
            output = 'Fizz';
        }
        console.log(output);
    }
}

console.log(fizz2());