import java.util.*;
public class Knight_tour {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        int row=scan.nextInt();
        int col=scan.nextInt();
        int arr[][]=new int[n][n];
        knight_tour(arr, row, col,1);
        scan.close();
    }
    public static void displayBoard(int[][] chess){
        for(int i = 0; i < chess.length; i++){
            for(int j = 0; j < chess[0].length; j++){
                System.out.print(chess[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();
    }
    public static void knight_tour(int arr[][],int row,int col,int moves){
        if(row<0 || col<0 ||row >=arr.length || col>=arr.length || arr[row][col]>0){
            return;
        }
        else if(moves==arr.length*arr.length){
            arr[row][col]=moves;
            displayBoard(arr);
            arr[row][col]=0;
            return;
        }

        arr[row][col]=moves;

        knight_tour(arr, row-2, col+1, moves+1);
        knight_tour(arr, row-1, col+2, moves+1);
        knight_tour(arr, row+1, col+2, moves+1);
        knight_tour(arr, row+2, col+1, moves+1);
        knight_tour(arr, row+2, col-1, moves+1);
        knight_tour(arr, row+1, col-2, moves+1);
        knight_tour(arr, row-1, col-2, moves+1);
        knight_tour(arr, row-2, col-1, moves+1);
        arr[row][col]=0;

    }
}
