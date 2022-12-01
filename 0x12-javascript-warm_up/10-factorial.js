#!/usr/bin/node
function factorial (a) {
  if (a === 1 || a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

const a = Math.floor(Number(process.argv[2]));

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
