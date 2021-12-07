var arr=[1,"Ram",7,"String",3];
var string_only_arr=[]
for(var i=0;i<arr.length;i++){
    if(typeof(arr[i])=="String"){
        string_only_arr.push(arr[i]);
    }
}
for(var i=0;i<string_only_arr.length;i++){
    console.log(string_only_arr[i]);
}
