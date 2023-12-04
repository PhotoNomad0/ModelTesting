function extractCode(filename) {
    // Regular expression pattern for the code and extension
    var regex = /(\d+)-([A-Za-z0-9]{3})\.usfm$/;

    // Execute regular expression on filename
    var match = regex.exec(filename);

    if (match) {
        return match[2];  // Return the three character code
    } else {
        throw new Error("Invalid file name format");
    }
}

const tests = ['66-1jn.usfm', '65-jas.usfm', '66-1JN.usfm', '65-JAS.usfm', 'jas.usfm', '65-jas', '15.jas']
for (const test of tests) {
    try {
        const result = extractCode(test)
        console.log(`Test '${test}': ${result}`)
    } catch (e) {
        console.error(`Error on "${test}`, e)
    }
}

//
// This code will create a dictionary with three keys and values, and then use the `sort()` method to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.
//
//     You can also specify the sorting function using the `Comparator` class from the `java.util` package. Here's an example code snippet:
//


// This code will create a dictionary with three keys and values, and then use the `Comparator` class to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.