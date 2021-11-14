import java.util.*;
public class Rotated_sorted_array {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]=new int[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();
        }
        int ntr=index(arr);
        System.out.print(ntr);
        scan.close();
    }
    public static int index(int arr[]){
        int n=arr.length;
        int start=0;
        int end=arr.length-1;
        int mid=0;
        while(start<end){
            mid=(start+end)/2;
            int next=(mid+1)%n;
            int prev=(mid+n-1)%n;
            if(arr[next]>=arr[mid] && arr[prev]>=arr[mid]){
                return arr[mid];
            }
            if(arr[start]<=arr[mid]){
                start=mid+1;
            }else if(arr[end]>arr[mid]){
                end=mid-1;
            }
        }
        return arr[start];
    }
}
