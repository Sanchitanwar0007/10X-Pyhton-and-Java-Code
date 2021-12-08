import java.util.*;
public class Gold_Mine_2 {
    static int max = 0;
    public static void collect_goled(ArrayList<Integer> list, int arr[][], int i, int j, boolean[][] visited) {
        if (i < 0 || j < 0 || i == arr.length || j == arr[0].length || visited[i][j] == true || arr[i][j] == 0) {
            return;
        }
        visited[i][j] = true;
        list.add(arr[i][j]);
        collect_goled(list, arr, i + 1, j, visited);
        collect_goled(list, arr, i, j + 1, visited);
        collect_goled(list, arr, i - 1, j, visited);
        collect_goled(list, arr, i, j - 1, visited);
    }
    public static void getMaxGold(int[][] arr) {
        boolean visited[][] = new boolean[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                if (arr[i][j] != 0 && visited[i][j] == false) {
                    ArrayList<Integer> list = new ArrayList<>();
                    collect_goled(list, arr, i, j, visited);
                    int sum = 0;
                    for (int val : list) {
                        sum += val;
                    }
                    max = Math.max(sum, max);
                }
            }

        }
    }
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int m = scn.nextInt();
        int[][] arr = new int[m][n];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                arr[i][j] = scn.nextInt();
            }
        }
        getMaxGold(arr);
        System.out.println(max);
        scn.close();
    }
}
