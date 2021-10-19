// function total(string){
//     obj ={};
//     for(var i=0;i<string.length;i++){
//         if(string[i] in obj){
//             obj[string[i]]+=1;
//         }else{
//             obj[string[i]]=1;
//         }
//     }
//     var output="";
//    for(var i in obj){
//        var t=obj[i];
//        output+=i
//        output+=t;
//    }
//    console.log(output);
//     }
// var str="dddcccaaa";
// total(str);

function value(arr,k){
    var sum=0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]<=k){
            sum+=arr[i];
        }
    }
    console.log(sum)
}
var arr=[1,2,3,4,5]
var k=2;
value(arr,k);