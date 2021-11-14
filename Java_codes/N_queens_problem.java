import java.util.*;
public class N_queens_problem {
   public static void main(String[] args){
       Scanner scan= new Scanner(System.in);
       int size=scan.nextInt();
       int arr[][]= new int[size][size];
       queentoPlace(arr,"",0);
       scan.close();
   } 
   public static void queentoPlace(int arr[][],String ans,int row){
       if(row==arr.length){
           System.out.println(ans);
           return;
       }
       for(int col=0;col<arr.length;col++){
           if(isQueenSafe(arr,row,col)==true){
            arr[row][col]=1;
            queentoPlace(arr, ans+row+"-"+col+",", row+1);
            arr[row][col]=0;
           }
           
       }
   }
   public static boolean isQueenSafe(int arr[][], int row,int col){
       for(int i=row-1,j=col;i>=0;i--){
           if(arr[i][j]==1){
               return false;
           }
       }
       for(int i=row-1,j=col-1;i>=0 && j>=0;i--,j--){
            if(arr[i][j]==1){
                return false;
            }
       }
       for(int i=row-1,j=col+1;i>=0 && j<arr.length;i--,j++){
        if(arr[i][j]==1){
            return false;
        }
   }
         return true;
   }

}
