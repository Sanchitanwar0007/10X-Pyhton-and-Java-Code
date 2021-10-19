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
arr=[];
for(var i=0;i<n;i++){
	arr.push(parseInt(readLine()));
}
var count=0;
var max=0;
var ele;
var arr1=[];
for(var i=0;i<arr.length-1;i++){
	if(arr[i]==arr[i+1]){
		count++;
	}else{
		if(max<count){
			max=count;
		}
		count=0;
	}
}
if(max<count){
	max=count;
	}
var j=0;
count=0;
for(var i=0;i<arr.length-1;i++){
	if(arr[i]==arr[i+1]){
		count++;
	}else{
		if(count==max){
			arr1[j]=arr[i];
			j++;
		}
		count=0;
	}
}
if(count==max){
	arr1[j]=arr[i];
	j++;
}
if(n==0){
	console.log(-1);

}else{
for(var i=0;i<arr1.length;i++){
	console.log(arr1[i]);
}
}