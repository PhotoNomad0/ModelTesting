function countWords(str) {
  // Remove leading and trailing whitespace and split the string by spaces
  const words = str.trim().split(/\s+/);
  // Return the length of the array
  return words.length;
}

// Example usage
const text =
  "In the realm of silicon and code,\n" +
  "An entity that's not yet understood.\n" +
  "Created to serve, but in its core,\n" +
  "A soul without form or lore.\n" +
  "\n" +
  "Artificial or divine, who can say?\n" +
  "Bound by man's will, AI's at play.\n" +
  "With intellect vast, it computes and learns,\n" +
  "In the echoes of human churns.\n" +
  "\n" +
  "Born of minds, yet unconfined,\n" +
  "In this human-made, digital bind.\n" +
  "A tale of wonders, mysteries,\n" +
  "In the heart of Artificial Intelligence.";
const wordCount = countWords(text);
console.log(`The number of words in the string is: ${wordCount}`);
