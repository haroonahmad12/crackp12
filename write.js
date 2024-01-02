const fs = require("fs");

function appendNumbersToFile(start, end, filename) {
  let data = "";
  for (let i = start; i <= end; i++) {
    data += i + "\n";
  }

  fs.appendFile(filename, data, (err) => {
    if (err) throw err;
    console.log(`Numbers appended to ${filename} successfully.`);
  });
}

// Example usage
const startNumber = 140000000;
const endNumber = 180000000;
const outputFilename = "4.txt";

appendNumbersToFile(startNumber, endNumber, outputFilename);
