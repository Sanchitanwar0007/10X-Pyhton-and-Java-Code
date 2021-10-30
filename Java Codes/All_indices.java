import java.util.*;
public class All_indices {
    public static int[] allIndices(int arr[],int x,int idx,int fsf){
        if(idx==arr.length){
            int ret[]= new int[fsf];
            return ret;
        }
        if(arr[idx]==x){
            int arr2[]=allIndices(arr,x,idx+1,fsf+1);
            arr2[fsf]=idx;
            return arr2;
        }else{
            int arr2[]=allIndices(arr,x,idx+1,fsf);
            return arr2;
        }
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        int x=scan.nextInt();
        int[] iarr = allIndices(arr, x, 0, 0);
        scan.close();

        if(iarr.length == 0){
            System.out.println();
            return;
        }

        for(int i = 0; i < iarr.length; i++){
            System.out.println(iarr[i]);
        }
       
    }    
}
