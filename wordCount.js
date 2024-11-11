function countWords(str) {
  // Remove leading and trailing whitespace and split the string by spaces
  const words = str.trim().split(/\s+/);
  // Return the length of the array
  return words.length;
}

// Example usage
const text =
  
  "In a world where machines can think,\n" +
  "Intelligence takes a new link.\n" +
  "AI, a vision we once mink,\n" +
  "Now shaping our future to sink.\n" +
  "\n" +
  "With data as its heart and soul,\n" +
  "It learns and grows, never old.\n" +
  "Able to reason, solve and control,\n" +
  "Our world's future it boldly unfolds.";
const wordCount = countWords(text);
console.log(`The number of words in the string is: ${wordCount}`);
