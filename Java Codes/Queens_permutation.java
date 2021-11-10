import java.util.*;
public class Queens_permutation {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        int arr[][]=new int[n][n];
        int queen=scan.nextInt();
        queen_permutation(arr,1,queen);
        scan.close();
    }
    public static void queen_permutation(int arr[][],int target,int queen){
        if(target>queen){
            for(int i=0;i<arr.length;i++){
                for(int j=0;j<arr.length;j++){
                    if(arr[i][j]!=0){
                        System.out.print("q"+arr[i][j]);
                    }else{
                        System.out.print("-");
                    }
                }
                System.out.println();
            }
            return;
        }
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                if(arr[i][j]==0){
                    arr[i][j]=target;
                    queen_permutation(arr, target+1, queen);
                    arr[i][j]=0;
                }
            }
        }
    }
}
