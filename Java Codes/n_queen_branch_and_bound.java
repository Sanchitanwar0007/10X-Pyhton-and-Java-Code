import java.io.BufferedReader;
import java.io.InputStreamReader;
public class n_queen_branch_and_bound {
    public static void main(String[] args) throws Exception{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        boolean chess[][]=new boolean[n][n];
        boolean dc[]=new boolean[n];
        boolean rd[]=new boolean[2*n-1];
        boolean ld[]= new boolean[2*n-1];
        nqueens(chess,n,0,dc,ld,rd,"");
    }
    public static void nqueens(boolean chess[][],int n,int row,boolean[] dc,boolean[] ld,boolean[] rd,String ans){
        if(row==n){
            System.out.println(ans+".");
            return;
        }
        for(int col=0;col<chess.length;col++){
            if(dc[col]==false && ld[row-col+chess.length-1]==false && rd[row+col]==false){
                chess[row][col]=true;
                dc[col]=true;
                ld[row-col+chess.length-1]=true;
                rd[row+col]=true;
                nqueens(chess,n,row+1,dc,ld,rd,ans+row+"-"+col+",");
                chess[row][col]=false;
                dc[col]=false;
                ld[row-col+chess.length-1]=false;
                rd[row+col]=false;
            }
        }

    }
}
