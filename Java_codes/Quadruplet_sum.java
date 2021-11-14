
import java.util.*;
public class Quadruplet_sum {
    public static void append(ArrayList<ArrayList<Integer>> list,ArrayList<ArrayList<Integer>> temp,int val){
        for(ArrayList<Integer> li:temp){
            li.add(val);
            list.add(li);
        }

    }
    public static ArrayList<ArrayList<Integer>> two_sum_sol(int[] arr,int target,int i,int j){
        ArrayList<ArrayList<Integer>> list= new ArrayList<>();
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
    public static ArrayList<ArrayList<Integer>> fourSum(int[] arr,int target,int n){
        ArrayList<ArrayList<Integer>> list= new ArrayList<>();
        Arrays.sort(arr);
        int i=0;
        int j=arr.length-1;
        for(int k=i;k<=j;k++){
            if(k!=i && arr[k]==arr[k-1]){
                continue;
            }
            ArrayList<ArrayList<Integer>> temp = three_sum_sol(arr, target-arr[k], k+1, j);
            append(list,temp,arr[k]);
        }
        return list;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		int target = sc.nextInt();
        sc.close();
		ArrayList<ArrayList<Integer>> ans = fourSum(arr, target, n);
		Collections.sort(ans,(a,b)->{
            int i = 0;
            int j = 0;
            
            while(i < a.size()){
                if(a.get(i) == b.get(j)){
                    i++;
                    j++;
                }else{
                    return a.get(i) - b.get(j);
                }
            }
            
            return 0;
        }); 
		for (ArrayList<Integer> a : ans) {
			for (int element : a) {
				System.out.print(element + " ");
			}
			System.out.println();
		}
        
    }
}