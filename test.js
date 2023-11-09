function generatePrimes(limit) {
    const primes = [];
    const isPrime = new Array(limit + 1).fill(true);

    for (let num = 2; num <= limit; num++) {
        if (!isPrime[num]) continue;

        primes.push(num);

        // Mark multiples of the current prime as non-prime
        for (let multiple = num * 2; multiple <= limit; multiple += num) {
            isPrime[multiple] = false;
        }
    }

    return primes;
}

const count = 100000;
const primes = generatePrimes(count); // The 100th prime number is less than 8000
console.log(`Number of primes for count ${count} is ${primes.length}`, primes);

//
// This code will create a dictionary with three keys and values, and then use the `sort()` method to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.
//
//     You can also specify the sorting function using the `Comparator` class from the `java.util` package. Here's an example code snippet:
//


// This code will create a dictionary with three keys and values, and then use the `Comparator` class to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.