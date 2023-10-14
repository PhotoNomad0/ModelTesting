function getCode(filename) {
    var re = /(\d*[A-Za-z]{3})\.(usfm)/;
    var result = filename.match(re);
    return (result && result.length > 0) ? result[1] : '';
}

////////////////////


const tests = ['66-1jn.usfm', '65-jas.usfm', '66-1JN.usfm', '65-JAS.usfm', 'jas.usfm', '65-jas', '15.jas']

for (const test of tests) {
    let results
    try {
        results = getCode(test)
        console.log(`'${test}' = '${results}'`)
    } catch (e) {
        console.error(`'${test}' failed '`,e)
    }
}


//
// This code will create a dictionary with three keys and values, and then use the `sort()` method to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.
//
//     You can also specify the sorting function using the `Comparator` class from the `java.util` package. Here's an example code snippet:
//


// This code will create a dictionary with three keys and values, and then use the `Comparator` class to sort it based on the difference between each key and its corresponding value. The sorted dictionary will be stored in the `myDict` variable.