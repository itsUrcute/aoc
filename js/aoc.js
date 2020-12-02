const arr = require("./input.json")

function day1(arr){
  for(a=0;a<arr.length;a++){
    if(arr.includes(2020-arr[a])){
      return (2020-arr[a])*arr[a]
    }
  }
}

function day2(arr){
  for(a=0;a<arr.length;a++){
    for(b=1;b<arr.length;b++)
    if(arr.includes(2020-arr[a]-arr[b])){
      return (2020-arr[a]-arr[b])*arr[a]*arr[b]
    }
  }
}
console.log(day1(arr))
console.log(day2(arr))