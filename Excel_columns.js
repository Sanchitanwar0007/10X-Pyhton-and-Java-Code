let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1].trim();
}

// -------- Do NOT edit anything above this line ----------
// Use readLine() for taking input, it will read one line of from the input  and is stored in string format
function getAlpha(val){
    let revChar=((26-val-1)+"A".charCodeAt(0));
    return String.fromCharCode(revChar);
}

let testcase = parseInt(readLine());
for(let i=0;i<testcase;i++){
    let n=parseInt(readLine())-1;
    let ans=[];
    while(n>=0){
        let rem=n%26;
        ans.push(getAlpha(rem));
        
        n=parseInt(n/26);
        n--;
    }
    // ans+=arr[n]+"";
    
    console.log(ans.reverse().join(""));
}
