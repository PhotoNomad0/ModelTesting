// ```javascript
function extractCode(filename) {
  const regex = /^(?:.*-)(\w{3})\.usfm$/;
  const match = filename.match(regex);
  return match ? match[1] : null;
}

function getCode(filename) {
  const code = extractCode(filename);
  console.log(`${filename} = code: ${code}`); // Output: 1Jn
}

// Example usage:
const filenames = [
  "57-1Jn.usfm",
  "1-1Jn.usfm",
  "-1Jn.usfm",
  "1Jn.usfm",
  "-1Jn"
];

for (const filename of filenames) {
  try {
    getCode(filename);
  } catch (e) {
    console.error(`${filename}, error:`, e)
  }
}

// ```

// **Explanation:**
//
// * **Function Definition:** The code defines a function called `extractCode` that takes a single argument, `filename`, representing the filename to process.
// * **Regular Expression:**
// *  `/^(?:.*-)(\w{3})\.usfm$/`: This regular expression is designed to capture the three-character code. Let's break it down:
// * `/ ... /`: Defines the regular expression pattern.
// * `^`: Matches the beginning of the string.
// * `(?:.*-)`: Matches any character (`.`) zero or more times (`*`), followed by a hyphen (`-`). The `?:` makes this a non-capturing group, meaning we're not interested in matching the characters before the hyphen.
// * `(\w{3})`: This is the capturing group that we want. It matches three word characters (`\w`, which includes letters, digits, and underscore) and captures them in group 1.
// * `\.usfm$`: Matches ".usfm" at the end of the string (`$`).
//
//
// * **Matching:** `filename.match(regex)` attempts to find a match for the regular expression in the `filename`. If a match is found, it returns an array containing the matched parts (including the captured group); otherwise, it returns `null`.
// * **Return Value:** The function returns `match[1]`, which is the content of the captured group (the three-character code) if a match was found. Otherwise, it returns `null`.
//
//
//
//
//   Let me know if you have any other questions or need further clarification!