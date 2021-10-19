// var fi="2 5 2";
// var si="4 2";
// var first="";
// var second="";
// for(var i=0;i<fi.length;i++){
//     if(fi[i]!=" "){
//         first+=fi[i]+"";
//     }
// }
// for(var j=0;j<si.length;j++){
//     if(si[j]!=" "){
//         second+=si[j]+"";
//     }
// }
// if(first.length<second.length){
//     var temp=first;
//     first=second;
//     second=temp;
// }
// console.log(first,second)
// var carry=0;
// var ans="";

// for(var i=0;i<first.length;i++){
//     var f=parseInt(first[i]);
//     var temp;
//     if(i<second.length){
//         var s=parseInt(second[i]);
//         temp=f+s+carry;
//     }else{
//         temp=f+carry;
//     }
//     if(temp>=10){
//         carry=Math.floor(temp/10);
//         temp=temp%10;
//     }else{
//         carry=0;
//     }
//     ans+=temp;
// }
// if(carry>0){
//     ans+=carry;
// }
// console.log(ans);





let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var n=parseInt(readLine());
for(var ll=0;ll<n;ll++){
	var fi=readLine();
	var si=readLine();
	var first="";
var second="";
for(var i=0;i<fi.length;i++){
    if(fi[i]!=" "){
        first+=fi[i]+"";
    }
}
for(var j=0;j<si.length;j++){
    if(si[j]!=" "){
        second+=si[j]+"";
    }
}
if(first.length<second.length){
    var temp=first;
    first=second;
    second=temp;
}
var carry=0;
var ans="";

for(var i=0;i<first.length;i++){
    var f=parseInt(first[i]);
    var temp;
    if(i<second.length){
        var s=parseInt(second[i]);
        temp=f+s+carry;
    }else{
        temp=f+carry;
    }
    if(temp>=10){
        carry=Math.floor(temp/10);
        temp=temp%10;
    }else{
        carry=0;
    }
    ans+=temp;
}
if(carry>0){
    ans+=carry;
}
console.log(ans);

}
