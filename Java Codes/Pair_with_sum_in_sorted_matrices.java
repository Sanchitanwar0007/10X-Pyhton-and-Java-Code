import java.util.*;
public class Pair_with_sum_in_sorted_matrices {
    public static int solve(int[][] matrix1,int[][] matrix2,int target){
        HashMap<Integer,Integer> set= new HashMap<>();
        for(int i=0;i<matrix1.length;i++){
            for(int j=0;j<matrix1.length;j++){
                set.put(matrix1[i][j],set.getOrDefault(matrix1[i][j],0)+1);
            }
        }
        int ans=0;
        for(int i=0;i<matrix2.length;i++){
            for(int j=0;j<matrix2.length;j++){
                int val=target-matrix2[i][j];
                if(set.containsKey(val)){
                    ans+=set.get(val);
                }
            }    
    }
    return ans;
}
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[][] mat1 = new int[N][N];
		for (int i = 0; i < mat1.length; i++) {
			for (int j = 0; j < mat1[0].length; j++) {
				mat1[i][j] = sc.nextInt();
			}
		}

		int[][] mat2 = new int[N][N];
		for (int i = 0; i < mat2.length; i++) {
			for (int j = 0; j < mat2[0].length; j++) {
				mat2[i][j] = sc.nextInt();
			}
		}
		int K = sc.nextInt();
		System.out.println(solve(mat1, mat2, K));
        sc.close();
    }
}
