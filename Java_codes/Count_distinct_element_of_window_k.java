import java.util.*;
public class Count_distinct_element_of_window_k {
    public static void main(String args[]){
    Scanner scan=new Scanner(System.in);
    int size=scan.nextInt();
    int arr[]=new int[size];
    for(int i=0;i<size;i++){
        arr[i]=scan.nextInt();
    }
    int k=scan.nextInt();
    HashMap<Integer,Integer> map=new HashMap<>();
    ArrayList<Integer> list=new ArrayList<>();
    for(int i=0;i<k-1;i++){
        map.put(arr[i],map.getOrDefault(arr[i],0)+1);
    }
    // System.out.print(map);
    for(int i=k-1,j=0;i<arr.length;){
        map.put(arr[i],map.getOrDefault(arr[i],0)+1);
        list.add(map.size());
        
        int freq=map.get(arr[j]);
        if(freq>1){
            map.put(arr[j],map.get(arr[j])-1);
            j++;
        }else if(freq==1){
            map.remove(arr[j]);
            j++;
        }
        i++;
    }
   for(int val:list){
       System.out.println(val);
   }
   scan.close();
}
}