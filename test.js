function generatePrimes(n) {
    // Create an array from 2 to n with all values initially set to true
    const primes = Array.from({ length: n-1 }, (_, i) => i + 2);
    for (let p = 2; p * p <= n; p++) {
        // If the current number is still marked as prime, it's a prime and we can cross out all its multiples
        if (primes[p - 2]) {
            for (let i = p * p; i <= n; i += p) {
                primes[i - 	2] = false;
            }
        }
    }
    // Return the prime numbers as an array
    return primes.filter(p => p).slice(0, 100);
}


const first100Primes = generatePrimes(1542); // 154 is the smallest number that's greater than or equal to 100 and an even number
console.log(first100Primes);

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