// ? main uses are Ternary Operator, Optional Chaining, Nullish Coalescing


var obj = {a:1, b:2}

console.log(obj?.b) // optional chaining
console.log(obj?.c) // optioanl chaining

console.log(0 || '') // OR oprators
console.log(0 ?? '') // Nullish Coalescing
// the above will allow the 0 to be logged or used instead of an || operator thinking it is a falsey value

