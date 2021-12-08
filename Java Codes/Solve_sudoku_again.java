import java.util.*;
public class Solve_sudoku_again {
    public static void display(int[][] board){
        for(int i = 0; i < board.length; i++){
          for(int j = 0; j < board[0].length; j++){
            System.out.print(board[i][j] + " ");
          }
          System.out.println();
        }
      }
    public static void solveSudoku(int arr[][],int i,int j){
        if(i==arr.length){
            display(arr);
            return;
        }
        int ni=0;
        int nj=0;
        if(j==arr.length-1){
            ni=i+1;
            nj=0;
        }else{
            ni=i;
            nj=j+1;
        }
        if(arr[i][j]!=0){
            solveSudoku(arr,ni,nj);
        }else{
            for(int pos=1;pos<=9;pos++){
                if(isValid(arr,i,j,pos)){
                    arr[i][j]=pos;
                    solveSudoku(arr, ni,nj);
                    arr[i][j]=0;
                }
            }
        }
    }
    public static boolean isValid(int arr[][],int x,int y,int val){
        for(int i=0;i<arr.length;i++){
            if(arr[x][i]==val){
                return false;
            }
        }
        for(int i=0;i<arr.length;i++){
            if(arr[i][y]==val){
                return false;
            }
        }
        int smi=(x/3)*3;
        int smj=(y/3)*3;
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                if(arr[smi+i][smj+j]==val){
                    return false;
                }
            }
        }
        return true;
    }
    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        int[][] arr = new int[9][9];
        for (int i = 0; i < 9; i++) {
          for (int j = 0; j < 9; j++) {
            arr[i][j] = scn.nextInt();
          }
        }
    
        solveSudoku(arr, 0, 0);
        scn.close();
      }
}
