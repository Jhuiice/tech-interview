// for
for(let i = 0; i < 10; i++) {
  console.log(i)
}

// for/of grabs item of the array
let arr0 = [1,2,3,4,5]
for (let index of arr0) {
  console.log(index)
}

// for/in grabs index of the array
let arr1 = [1,2,3,4,5]
for (let index in arr1) {
  console.log(index)
}

// while
let x = 1
let y = 1
while (x === y) {
  x++;
  if (x === 4) {
    y = 2;
  }
  console.log(x,y)
}


// do/while