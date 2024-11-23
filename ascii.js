// write a JavaScript program to generate and print out the ascii character and hexadecimal codes for 0 to 7f
//   ```javascript

function convertToAscii(char) {  // Write your code here.    
	if ((char >= 'A' && char <= "Z") ||   /// Uppercase letters are in the range of A-z, so we can use this to check for that condition as well                                      ////////////////////////
		('a'+(char)+'') === String(((char).toUpperCase()))){  // The + is used because JavaScript converted it into a string and then put together with "". So the above line will be true when char = 'A' or any other letters in range of A-z, else false
		return parseInt(String('0x'+(((char).toUpperCase()))));  // We can use this to get an integer value for each character and then print it out as a number. The above line will be true when char = 'A' or any other letters in range of A-z, else false
	}else{   /// If the condition is not met we need some way that can check whether this particular string has been converted into an integer value and if it was then just use its number as a character code.  /////////////////////////    ///////////     

		return char;                                       ////////////////////////////      
	}                                                            /* We have to make sure the condition is met before we continue with our program, otherwise there will be some errors in execution of this function */ ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
}

// function convertToHex(char) {                                    // We can also use the same method to get its corresponding number for each char in range of 0-f, 0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
// }
//
// function convertToAsciiAndHex(char) {                            // We can also use the same method to get its corresponding number for each char in range of 0-f, 0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
// }
//
// function main() {                                                // We can also use the same method to get its corresponding number for each char in range of 0-f, 0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
// }
//
// main();                                                          // We can also use the same method to get its corresponding number for each char in range of 0-f, 0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
// ```
//
// ### Example:    // We can also use the same method to get its corresponding number for each char in range of 0-f, 0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
//   ```javascript

function convertToAsciiAndHex(char) {                            // We can also use the same method to get its corresponding number for each char in range of 0-f, 0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	if ((char >= 'A') &&(('a'+String(((char).toUpperCase()))) === String("0x"+Char))) { // We can use this to get the corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
		return parseInt(String('0x'+(((char).toUpperCase())))); // We can use this to get the corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	}else{                                                         /* Again we have some way to check the condition before executing our program in this function so make sure you are using only one of them */    ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
		return char;                                               /* We have to put the condition here before we can execute our program, otherwise there will be some errors in execution of this function */   ///     */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	}                                                               /* We have to make sure the condition is met before we continue with our program, otherwise there will be some errors in execution of this function */ ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
}

function main() {                                                // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	var ch = "A";                                                // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	var ascii = convertToAscii(ch);                               // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	var hex = convertToHex(ch);                                    // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	var asciiAndHex = convertToAscii(ch);                         // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
}

main();                                                          // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
```

### Output:    // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
  ```javascript

function convertToAsciiAndHex(char) {                            // We can also use the same method to get its corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	if ((char >= 'A') &&(('a'+String(((char).toUpperCase()))) === String("0x"+Char))) { // We can use this to get the corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
		return parseInt(String('0x'+(((char).toUpperCase())))); // We can use this to get the corresponding number for each char in range of 0-f,0-9 *////////////////////////     ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	}else{                                                         /* Again we have some way to check the condition before executing our program in this function so make sure you are using only one of them */    ///   */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
		return char;                                               /* We have to put the condition here before we can execute our program, otherwise there will be some errors in execution of this function */   ///     */        /*** This line checks whether it's a letter or not and then returns that character code as an integer value.  **/
	}                                                               /* We have to make sure the condition is met before we continue with our program, otherwise there will be some errors