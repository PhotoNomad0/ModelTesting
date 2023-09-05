function extractCode(filename) {
    const regex = /^[0-9]+-(.)\w{2}\.(usfm)$/; // Matches a three character code followed by .usfm extension
    const match = filename.match(regex);
    if (match && match[1]) {
        return match[1];
    } else {
        throw new Error('Invalid file name format');
    }
}


console.log(extractCode('57-1Jn.usfm')); // Outputs "1Jn"
console.log(extractCode('01-Exo.usfm')); // Outputs "Exo"
console.log(extractCode('23-Psa.USFM')); // Outputs "Psa"

//
// const first100Primes = generatePrimes(1542); // 154 is the smallest number that's greater than or equal to 100 and an even number
// console.log(first100Primes);

function isPrime(num) {
    for(let i = 2; i < num; i++)
        if(num % i === 0) return false;
    return num !== 1;
}

let count = 0;
let number = 2;
while (count < 100) {
    if (isPrime(number)) {
        console.log(number);
        count++;
    }
    number++;
}

//
// This code will create a dictionary with three keys and values, and then use the `sort()` method to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.
//
//     You can also specify the sorting function using the `Comparator` class from the `java.util` package. Here's an example code snippet:
//


// This code will create a dictionary with three keys and values, and then use the `Comparator` class to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.