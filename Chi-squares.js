let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
// Use readLine() for taking input, it will read one line of from the input  and is stored in string format

function mininsertions(st, n)
{
  let map = new Map();
  for(let i=0;i<n;i++)
  {
    if(map.has(st[i]))
    {
      map.set(st[i], 1 + map.get(st[i]));
    }
    else
    {
      map.set(st[i], 1);
    }
  }
  let oddcounts = 0;
  for(let m of map)
  {
    if(m[1]%2!==0)
    {
      oddcounts++;
    }
    
    // return oddcounts-1;
  }
  if(oddcounts==0)
    {
      return 0;
    }
  return oddcounts-1;
}
let test = parseInt(readLine());
while(test--)
{
  let st = readLine().trim();
  console.log(mininsertions(st, st.length));
}
