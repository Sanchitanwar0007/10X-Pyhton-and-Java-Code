import java.util.*;
public class GEt_stair_path {
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int n= scan.nextInt();
        
        ArrayList<String> list=get_stair_list(n);
        System.out.print(list);
        scan.close();
    }
    public static ArrayList<String>  get_stair_list(int n){
        if(n==0){
            ArrayList<String> list1= new ArrayList<>();
            list1.add("");
            return list1;
        }
        if(n<0){
            ArrayList<String> list1= new ArrayList<>();
            return list1;
        }
        ArrayList<String> path1=get_stair_list(n-1);
        ArrayList<String> path2=get_stair_list(n-2);
        ArrayList<String> path3=get_stair_list(n-3);
        ArrayList<String> list= new ArrayList<>();
        for(String val:path1){
            list.add(1+val);
        }
        for(String val:path2){
            list.add(2+val);
        }
        for(String val:path3){
            list.add(3+val);
        }
        return list;
    }   
}
