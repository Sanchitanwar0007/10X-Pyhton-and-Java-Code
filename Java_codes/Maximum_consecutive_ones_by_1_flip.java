import java.util.*;
public class Maximum_consecutive_ones_by_1_flip {
    public static int max_ones(int arr[]){
        int ans=0;
        int j=-1;
        int count=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]==0){
                count++;

            }

            while(count>1){
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
        System.out.println(max_ones(arr));
        scan.close();
    }
}
