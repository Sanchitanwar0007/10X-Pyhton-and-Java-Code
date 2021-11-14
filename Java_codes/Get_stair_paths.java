import java.util.*;
public class Get_stair_paths {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n=scan.nextInt();
        print_stair_path(n,"");
        scan.close();
    }
    public static void print_stair_path(int n,String ans){
        if(n==0){
            System.out.print(ans+" ");
            return;
        }
        if(n<0){
            return;
        }
        print_stair_path(n-1, ans+"1");
        print_stair_path(n-2, ans+"2");
        print_stair_path(n-3, ans+"3");
    }
}
