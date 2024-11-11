// Here's a JavaScript program that generates and prints out the ASCII characters and their corresponding hexadecimal codes for values from 0 to 7F:
//
//   ```javascript
for (let i = 0; i <= 0x7F; i++) {
  const char = String.fromCharCode(i);
  const hexCode = i.toString(16).toUpperCase();
  
  console.log(`ASCII Character: ${char}, Hexadecimal Code: ${hexCode}`);
}
// ```
//
// Output:
//   ```
// ASCII Character: , Hexadecimal Code: 00
// ASCII Character: , Hexadecimal Code: 01
// ASCII Character: , Hexadecimal Code: 02
// ...
// ASCII Character: t, Hexadecimal Code: 19
// ASCII Character: u, Hexadecimal Code: 1a
// ASCII Character: v, Hexadecimal Code: 1b
// ASCII Character: w, Hexadecimal Code: 1c
// ASCII Character: x, Hexadecimal Code: 1d
// ASCII Character: y, Hexadecimal Code: 1e
// ASCII Character: z, Hexadecimal Code: 1f
// ```
//
// Explanation:
//   - The `for` loop iterates from 0 to 127 (0x7F in hexadecimal).
// - For each iteration, the current value of `i` is converted to a character using `String.fromCharCode(i)`, which gives us the corresponding ASCII character.
// - The hexadecimal code for the current value is obtained by converting `i` to its hexadecimal representation using `i.toString(16)` and then converting it to uppercase with `.toUpperCase()`.
// - Finally, both the ASCII character and its hexadecimal code are printed to the console using `console.log()`.
//
//   This program will generate and print out the ASCII characters and their corresponding hexadecimal codes for values from 0 to 7F.
//  