import java.util.*;
public class Equivalent_subarray {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]=new int[size];
        HashSet<Integer> set= new HashSet<>();
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();
            set.add(arr[i]);

        }
        int k=set.size();
        int i=-1;
        int j=-1;
        int ans=0;
        HashMap<Integer,Integer> map= new HashMap<>();
        while(true){
            boolean f1=true;
            boolean f2=true;
            while(i<arr.length-1){
                f1=false;
                i++;
                int n=arr[i];
                
                map.put(n,map.getOrDefault(n,0)+1);
                if(map.size()==k){
                    break;
                }
            }
        
        while(j<i){
            f2=false;
         j++;
         if(map.size()==k){
             ans+=arr.length-i;
        }
         int n=arr[j];
         if(map.get(n)==1){
             map.remove(n);
         }else{
             map.put(n,map.get(n)-1);
            } 
         if(map.size()<k){
             break;
            }
         
            }
        if(f1 && f2){
            break;
            }
       }
    System.out.print(ans);
    scan.close();
    }
}
