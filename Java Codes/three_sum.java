import java.util.*;
public class three_sum {
    public static void append(ArrayList<ArrayList<Integer>> list,ArrayList<ArrayList<Integer>> temp,int val){
        for(ArrayList<Integer> li:temp){
            li.add(val);
            list.add(li);
        }

    }
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
    public static ArrayList<ArrayList<Integer>> three_sum_sol(int[] arr,int target,int i,int j){
        ArrayList<ArrayList<Integer>> list= new ArrayList<>();
        for(int k=i;k<=j;k++){
            if(k!=i && arr[k]==arr[k-1]){
                continue;
            }
            ArrayList<ArrayList<Integer>> temp= two_sum_sol(arr, target-arr[k], i+1, j);
            append(list,temp,arr[k]);
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
        ArrayList<ArrayList<Integer>> res= three_sum_sol(arr,target,0,arr.length-1);
        System.out.print(res);
        scan.close();
    }
}
