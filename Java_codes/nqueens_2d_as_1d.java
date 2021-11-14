import java.io.BufferedReader;
import java.io.InputStreamReader;

public class nqueens_2d_as_1d {
    public static void main(String[] args) throws Exception{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int[][] chess = new int[n][n];

        nqueens(0, n, chess);
    }
    public static void nqueens(int queens,int target,int chess[][]){
        if(queens==target){
            for(int i=0;i<chess.length;i++){
                for(int j=0;j<chess.length;j++){
                    if(chess[i][j]>0){
                    System.out.print("q"+chess[i][j]+"\t");
                }else{
                    System.out.print("-\t");
                }
            }
            System.out.println();
            }
            System.out.println();
            return;
        }
        for(int i=0;i<chess.length*chess.length;i++){
            int row=i/chess.length;
            int col=i%chess.length;
            if(chess[row][col]==0 && isqueenSafe(chess,row,col)){
                chess[row][col]=queens+1;
                nqueens(queens+1,target,chess);
                chess[row][col]=0;
            }
        }
    }
    public static boolean isqueenSafe(int chess[][],int row,int col){
        for(int i=row,j=col;i>=0;i--){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;i<chess.length;i++){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;j>=0;j--){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;j<chess.length;j++){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;i>=0 && j>=0;i--,j--){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;i>=0 && j<chess.length;i--,j++){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;i<chess.length && j>=0;i++,j--){
            if(chess[i][j]>0){
                return false;
            }
        }
        for(int i=row,j=col;i<chess.length && j<chess.length;i++,j++){
            if(chess[i][j]>0){
                return false;
            }
        }
        return true;
    }
}
