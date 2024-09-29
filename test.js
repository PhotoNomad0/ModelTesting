// To sort the keys of a dictionary (JavaScript object) alphabetically and output the corresponding values, you can follow these steps:
//
//   1. Create an array of keys from the object.
// 2. Sort the array of keys alphabetically using `sort()` method.
// 3. Iterate through the sorted keys and output the corresponding values.
//
// Here's a sample JavaScript code to do this:
//
// ```javascript
// Sample dictionary (JavaScript object)
const dictionary = {
  "banana": "yellow",
  "apple": "red",
  "orange": "orange",
  "grape": "purple"
};

// Create an array of keys from the dictionary
const keys = Object.keys(dictionary);

// Sort the keys alphabetically
keys.sort();

// Iterate through the sorted keys and output the corresponding values
for (let i = 0; i < keys.length; i++) {
  console.log(`${keys[i]}: ${dictionary[keys[i]]}`);
}
// ```
//
// Output:
// ```
// apple: red
// banana: yellow
// grape: purple
// orange: orange
// ```
//
// In this code snippet, we create an array of keys from the `dictionary` object using `Object.keys()`. Then, we sort the array alphabetically using the `sort()` method. Finally, we iterate through the sorted keys and output the corresponding values with their keys using a `for` loop.
//  

///////////////////////////////////////////////////////////////

// const myDictionary = {
//   "banana": 3,
//   "apple": 1,
//   "cherry": 2
// };
//
// // Output the sorted array
// console.log(entries);


///////////////////////////////////////////////////////////////

// function getCode(filename) {
//   const code = extractThreeCharCode(filename);
//   console.log(`${filename} = code: ${code}`); // Output: 1Jn
// }
//
// // Example usage:
// const filenames = [
//   "57-1Jn.usfm",
//   "14-tit.usfm",
//   "1-1Jn.usfm",
//   "-1Jn.usfm",
//   "1Jn.usfm",
//   "-1Jn"
// ];
//
// for (const filename of filenames) {
//   try {
//     getCode(filename);
//   } catch (e) {
//     console.error(`${filename}, error:`, e)
//   }
// }

