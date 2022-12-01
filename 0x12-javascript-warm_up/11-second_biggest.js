#!/usr/bin/node

function bubbleSort (arr) {
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (Number(arr[j]) > Number(arr[j + 1])) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
}

const myArr = process.argv.slice(2);

if (myArr.length === 0 || myArr.length === 1) {
  console.log(0);
} else {
  const newArr = bubbleSort(myArr);
  console.log(newArr[newArr.length - 2]);
}
