import java.util.*;
public class Max_consectuve_ones_by_flipping_k_zeroes {

    public static int max_ones(int arr[],int k){
        int ans=0;
        int j=-1;
        int count=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==0){
                count++;
            }
            while(count>k){
                j++;
                if(arr[j]==0){
                    count--;
                }
            }
            ans=Math.max(ans,i-j);
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();

        }
        int k=scan.nextInt();
        System.out.println(max_ones(arr,k));
        scan.close();
    }
}


