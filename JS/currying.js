// First class functions

// can use lodash for curry function

// why is it useful

let dragon = name => size => element => {
    console.log(name)
    console.log(size)
    console.log(element)
    let statement = name + " is a " + size + " dragon that breathes " +
    element + "!"

    return statement
}

console.log(dragon('Daisy')('Huge')("Water"))
console.log(dragon('Daisy'))

// filter?