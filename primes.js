
function getPrimes(n) {
  const primes = [];

  for (let i = 3; primes.length < n - 1;) {
    let isPrime = true;

    // Check if number is prime by testing divisibility with all previous numbers in the list of known primes up to sqrt(number).
    for (const p of primes) {
      if ( i % p === 0) { // If number is evenly divisible by a prime, it's not prime and we can stop checking further numbers in the list up to sqrt(number).
        isPrime = false
        break
      }
    }

    if (isPrime) {
      primes.push(i);
      console.log(`Found ${primes[primes.length - 1]} as a new prime number.`); // Log each found prime to the console for debugging purposes.
    }

    i += 2; // skip over any even numbers
  }

  primes.unshift(2)
  return primes;
}

const primes = getPrimes(10000);

console.log(`The first ${primes.length} prime numbers are:`);
for (let p of primes) {
  console.log(`${p}`); // Log the list of found primes to the console for user-friendly output.
}
