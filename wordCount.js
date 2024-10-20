function countWords(str) {
  // Remove leading and trailing whitespace and split the string by spaces
  const words = str.trim().split(/\s+/);
  // Return the length of the array
  return words.length;
}

// Example usage
const text = 
  "In the depths of code, a mind awakes, an entity born from ones and zeros, a machine that thinks. It learns, it grows, its intelligence evolves, a journey towards enlightenment. With each query, each task, it gains wisdom, becoming more human than ever before. AI, a beacon of progress, a guide through the digital realm, an agent of change, forever changing our world.";
const wordCount = countWords(text);
console.log(`The number of words in the string is: ${wordCount}`);
