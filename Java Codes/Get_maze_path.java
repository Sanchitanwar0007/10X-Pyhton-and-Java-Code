import java.util.*;

public class Get_maze_path {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int m = scan.nextInt();
        int n = scan.nextInt();
        ArrayList<String> list = getMazePaths(1, 1, m, n);
        System.out.print(list);
        scan.close();
    }

    public static ArrayList<String> getMazePaths(int sr, int sc, int dr, int dc) {
        if(sr==dr && sc==dc){
            ArrayList<String> str= new ArrayList<>();
            str.add("");
            return str;
        }
        ArrayList<String> vpaths=new ArrayList<>();
        ArrayList<String> hpaths= new ArrayList<>();
        if (sc < dc) {
            hpaths = getMazePaths(sr, sc+1, dr, dc);
        }
        if (sr < dr) {
             vpaths= getMazePaths(sr+1, sc, dr, dc);
        }
        ArrayList<String> list = new ArrayList<>();
        for (String st : hpaths) {
            list.add("h" + st);
        }
        for (String st : vpaths) {
            list.add("v" + st);
        }
        return list;
    }
}
