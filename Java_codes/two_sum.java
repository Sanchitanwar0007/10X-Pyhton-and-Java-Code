import java.util.*;
public class two_sum {
    public static ArrayList<ArrayList<Integer>> two_sum_sol(int[] arr,int target,int i,int j){
        ArrayList<ArrayList<Integer>> list= new ArrayList<>();
        Arrays.sort(arr);
        while(i<j){
            int sum=arr[i]+arr[j];
            if(sum>target){
                j--;
            }else if(sum<target){
                i++;
            }else{
                ArrayList<Integer> temp = new ArrayList<>();
                temp.add(arr[i]);
                temp.add(arr[j]);
                list.add(temp);
                i++;
                j--;
                while(i<j && arr[i]==arr[i-1]){
                    i++;
                }
                while(i<j && arr[j]==arr[j+1]){
                    j--;
                }
            }
        }
        return list;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]= new int[size];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        int target=scan.nextInt();
        ArrayList<ArrayList<Integer>> res= two_sum_sol(arr,target,0,arr.length-1);
        System.out.print(res);
        scan.close();
    }
}
