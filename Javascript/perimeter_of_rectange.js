let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

var num1=data[0];
var num2=data[1];
if(num1<0 || num2<0){
	console.log(0);
}else{
	var ans=2*(num1+num2);
	console.log(ans);
}
