import java.util.*;
public class Print_maze_path {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int m=scan.nextInt();
        int n=scan.nextInt();
        maze_path(1,1,m,n,"");
        scan.close();

    }
    public static void maze_path(int sr,int sc,int dr,int dc,String ans){
        if(sr==dr && sc==dc){
            System.out.print(ans+" ");
            return;
        }
        if(sr<dr){
            maze_path(sr+1, sc, dr, dc, ans+"h");
        }
        if(sc<dc){
            maze_path(sr, sc+1, dr, dc, ans+"v");
        }
    }
}
