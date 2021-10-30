import java.util.*;
public class Get_subsequence {
    public static void main(String[] args) throws Exception {
        Scanner scan= new Scanner(System.in);
        String str=scan.next();
        ArrayList<String> list=gss(str);
        System.out.print(list);
        scan.close();
    }

    public static ArrayList<String> gss(String str) {
        if(str.length()==0){
            ArrayList<String> lis= new ArrayList<>();
            lis.add("");
            return lis;
        }
        char ch=str.charAt(0);
        String res=str.substring(1);
        ArrayList<String> list= gss(res);
        ArrayList<String> ans=new ArrayList<>();
        for(String rs:list){
            ans.add(ch+rs);
            ans.add(""+rs);
            
        }
        return ans;
    }
}
