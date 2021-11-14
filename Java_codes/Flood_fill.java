import java.util.*;
public class Flood_fill {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[][] arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = scan.nextInt();
            }
        }
        boolean[][] visited=new boolean[n][m];
        floodfill(arr, 0, 0, "",visited);
        scan.close();
    }
    public static void floodfill(int[][] arr,int row,int col,String str,boolean[][] visited){
            if(row<0 || col<0 || row==arr.length || col==arr[0].length|| arr[row][col]==1 || visited[row][col]==true){
                return;
            }
            if(row==arr.length-1 && col==arr[0].length-1){
                System.out.print(str+" ");
                return;
            }
            visited[row][col]=true;
            floodfill(arr, row-1, col, str+"t", visited);
            floodfill(arr, row, col-1, str+"l", visited);
            floodfill(arr, row+1, col, str+"d", visited);
            floodfill(arr, row, col+1, str+"r", visited);
    }
}
