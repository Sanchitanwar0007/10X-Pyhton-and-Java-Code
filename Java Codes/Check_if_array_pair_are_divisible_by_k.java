import java.util.*;
public class Check_if_array_pair_are_divisible_by_k {
    public static boolean solution(int arr[],int k){
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int val:arr){
            int rem=val%k;
            if(rem<0){
                rem+=k;
            }
            if(map.containsKey(rem)){
                map.put(rem,map.get(rem)+1);
            }else{
                map.put(rem,1);
            }
        }
        for(int val:arr){
            int rem=val%k;
            if(rem<0){
                rem+=k;
            }
            if(rem==0){
                if(map.get(rem)%2!=0){
                    return false;
                }
            }else if(2*rem==k){
                if(map.get(rem)%2!=0){
                    return false;
                }
            }else{
                int freq=map.get(rem);
                int other_freq=0;
                if(map.containsKey(rem)){
                    other_freq=map.get(k-rem);
                }
                if(freq!=other_freq){
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=scan.nextInt();
        }
        int k=scan.nextInt();
        System.out.print(solution(arr,k));
        scan.close();
    }
}
