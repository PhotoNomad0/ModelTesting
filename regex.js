// Certainly! Below is a JavaScript function that uses regular expressions to extract a three-character code like "1Jn" from a filename in the format "57-1Jn.usfm". The characters can be upper or lower case letters or digits, and the filename extension must be ".usfm".
//
//   ```javascript
function extractThreeCharCode(filename) {
    // Regular expression to match the pattern "57-1Jn.usfm"
    const regex = /^.*-(\b[A-Za-z0-9]{3}\b)\.usfm$/;
    
    // Test if the filename matches the pattern
    if (regex.test(filename)) {
        // Extract the three-character code from the match
        return regex.exec(filename)[1];
    } else {
        // Return null or handle the error as needed
        return null;
    }
}

// // Example usage:
// const filename = "57-1Jn.usfm";
// const code = extractThreeCharCode(filename);
// console.log(code);  // Output: "1Jn"
// ```
//
// ### Explanation:
//   1. **Regular Expression**: The regular expression `/^.*-(\b[A-Za-z0-9]{3}\b)\.usfm$/` is designed to match the filename format.
// - `^.*-`: Ensures that there are any characters before a hyphen.
// - `(\b[A-Za-z0-9]{3}\b)`: Captures exactly three characters (letters or digits), surrounded by word boundaries (`\b`) to ensure they form a discrete segment.
// - `\.usfm$`: Ensures the filename ends with `.usfm`.
//
//   2. **Testing and Extracting**: The function uses the `test` method of the regex object to check if the filename matches the pattern. If it does, `exec` is used to extract the captured group (the three-character code).
//
// 3. **Error Handling**: If the filename does not match the pattern, the function returns `null`. You can customize this part to handle errors as needed.
//
//   This function should work correctly for filenames that follow the specified format.
//  
const filenames = [
  "57-1Jn.usfm",
  "14-tit.usfm",
  "1-1Jn.usfm",
  "-1Jn.usfm",
  "1Jn.usfm",
  "-1Jn"
];

for (const filename of filenames) {
  try {
    const code = extractThreeCharCode(filename);
    console.log(`Code for '${filename}' is '${code}'`)
  } catch (e) {
    console.error(`${filename}, error:`, e)
  }
}