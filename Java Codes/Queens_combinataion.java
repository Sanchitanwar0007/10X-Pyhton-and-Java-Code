// import java.util.*;
import java.io.*;
public class Queens_combinataion {
    public static void main(String[] args) throws Exception{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean chess[][]= new boolean[n][n];
        queens_combination(chess,n,0,1);
    }
    public static void queens_combination(boolean chess[][],int n,int tq,int arr){
        if(tq==n){
            for(int i=0;i<chess.length;i++){
                for(int j=0;j<chess.length;j++){
                    if(chess[i][j]==true){
                        System.out.print("q\t");
                    }else{
                        System.out.print("-\t");
                    }
                    
                }
                System.out.println();
            }
            System.out.println();
            return;
        }
        for(int i=arr;i<chess.length*chess.length;i++){
            int row=i/chess.length;
            int col=i%chess.length;
            if(chess[row][col]==false){
                chess[row][col]=true;
                queens_combination(chess, n, tq+1, arr+1);
                chess[row][col]=false;
            }
        }
    }
}
