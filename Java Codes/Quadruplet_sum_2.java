import java.util.*;
public class Quadruplet_sum_2 {	
    public static int fourSumCount(int[] A, int[] B, int[] C, int[] D) {
		HashMap<Integer,Integer> map= new HashMap<>();
        for(int val:A){
            for(int val2:B){
                map.put(val+val2,map.getOrDefault(val+val2,0)+1);
            }
        }
        int count=0;
        int target=0;
        for(int val:C){
            for(int val2:D){
                count+=map.getOrDefault(target-(val+val2),0);
            }
	}
    return count;
}


    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr1 = new int[n];
		int[] arr2 = new int[n];
		int[] arr3 = new int[n];
		int[] arr4 = new int[n];
		for (int i = 0; i < n; i++) {
			arr1[i] = sc.nextInt();
		}
		for (int i = 0; i < n; i++) {
			arr2[i] = sc.nextInt();
		}
		for (int i = 0; i < n; i++) {
			arr3[i] = sc.nextInt();
		}
		for (int i = 0; i < n; i++) {
			arr4[i] = sc.nextInt();
		}
		System.out.println(fourSumCount(arr1, arr2, arr3, arr4));
	}

}
