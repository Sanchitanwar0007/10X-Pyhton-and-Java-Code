import java.util.*;
public class Get_kpc {
    public static void main(String[] args){
    Scanner scan= new Scanner(System.in);
    String str= scan.next();
    ArrayList<String> list= get_kpc(str);
    System.out.print(list);
    scan.close();
}
    static String[] sarr={"","abc","def","ghi","jkl","mno","pqrs","tu","vwx","yz"};
    public static ArrayList<String> get_kpc(String str){
    if(str.length()==0){
        ArrayList<String> list= new ArrayList<>();
        list.add("");
        return list;
    }
        char ch=str.charAt(0);
        String res=str.substring(1);
        ArrayList<String> temp=get_kpc(res);
        ArrayList<String> ans= new ArrayList<>();
        for(int i=0;i<sarr[Character.getNumericValue(ch)].length();i++){
            char ch2=sarr[Character.getNumericValue(ch)].charAt(i);
            for(String val:temp){
                ans.add(ch2+val);
            }
            
        }
        return ans;
    }   

}

