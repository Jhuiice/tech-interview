// Memory Pull what you know about JS arrays
// Methods: .reverse() .push() .pop() .filter(callback returns values that make it true) .lower() .upper()
// arr1.concat(arr2, ...) .splice() .slice(start, end) this creates a new array of values
// .length .sort()
// for each
// for of
// for any ?
// do while
// while

// arrays are index [::] like python? nope its indexed with single indexes

// ! .splice(start, end)
arr = [1,2,3,4,5]
arr2 = arr.splice(1,2) // splice mutates the array being spliced
// arr is now [1,4,5]
// arr2 is now [2,3]

console.log(arr.length)

arr3 = [1,2,3,4,5,6,7,8]
arr3.forEach((t) => t^2)

arr4 = arr3.filter(t => t % 2 == 0) // returns all even numbers

// Remember whats in your arsenal
// Excersise to improve memory
arr4.sort((a,b) => a - b) // sort in acsending order
arr4.sort((a,b) => b - a) // sort in descending order

arr_map = arr4.map((num) => num*3 )

