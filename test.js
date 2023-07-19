for (let i = 0; i <= 7; i++) {
  let character = String.fromCharCode(i);
  console.log(`ASCII code for ${character}: ${String(character).charCodeAt(0)}`);
  console.log(`Hexadecimal code for ${character}: ${character.toHex()}`);
}