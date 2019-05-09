var fs = require('fs');

// function getFile(filename,enc) {
//     return new Promise(function(resolve, reject) {
//         fs.readFile(filename, enc, function(err, data){
//             if (err) 
//                 reject(err); 
//             else
//                 resolve(data);
//         });
//     });
// }

// getFile('./input1.txt', 'utf8')
// .then(data => console.log(data));

function printer(arr){
    console.log("|" + arr[0] + '|' + arr[1] + '|' + arr[2] + '|');
}

var data = fs.readFileSync('input1.txt');
var dataarray = [...data.toString().replace(/,/g, '')]

console.log('-----------')
//console.log(dataarray.slice(0,3))
printer(dataarray.slice(0,3));
printer(dataarray.slice(3,6));
printer(dataarray.slice(6,9));
console.log('-----------')

// dataarray.forEach(function(value){
//     console.log("|" + value + '|' + value + '|' + value + '|');
//   });
// console.log('-----------')