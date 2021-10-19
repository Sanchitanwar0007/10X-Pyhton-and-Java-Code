import java.util.*;
public class GetCommon_Elements {
    public static void main(String args[]){
    Scanner scan=new Scanner(System.in);
    int n1=scan.nextInt();
    int arr[]=new int[n1];
    for(int i=0;i<n1;i++){
        arr[i]=scan.nextInt();
    }
    int n2=scan.nextInt();
    int arr2[]=new int[n2];
    for(int i=0;i<n2;i++){
        arr2[i]=scan.nextInt();
    }
   HashMap<Integer,Integer> map=new HashMap<>();
   for(int i=0;i<n1;i++){
       if(map.containsKey(arr[i])){
           map.put(arr[i],map.get(arr[i])+1);
       }else{
           map.put(arr[i],1);
       }
   }
  for(int val:arr2){
      if(map.containsKey(val)){
      System.out.println(val);
      map.remove(val);
  }
}
scan.close();
    }
}