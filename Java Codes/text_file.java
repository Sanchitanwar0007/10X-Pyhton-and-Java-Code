import java.util.*;
public class text_file {
    public static void main(String[] args){
        // int arr[]={1,4,2,5,3};
        // int s=odd_len_suarray_sum(arr, 0);
        print_pattern(4);
        
    }
    public static int odd_len_suarray_sum(int arr[],int sum){
        
        // int n=arr.length;
        HashMap<Integer,Integer> map=new HashMap<>();
        int i=-1;
        int j=-1;
        int odd_teller=1;
        while(true){
            while(i<arr.length){
                i++;
                map.put(arr[i],i);
                if(map.size()==odd_teller){
                    break;
                }
            }
            odd_teller+=2;
            while(j<i){
                j++;
                
            }


        }


        // return sum;
    }
    public static void print_pattern(int n){
        
        for(int i=1;i<n+1;i++){
            for(int p=0;p<n-i;p++){
                System.out.print(" ");
            }

            for(int j=1;j<i+1;j++){
                System.out.print(j);
            }
            for(int k=i-1;k>=1;k--){
                System.out.print(k);
            }
            System.out.println();
        }
    }
}
