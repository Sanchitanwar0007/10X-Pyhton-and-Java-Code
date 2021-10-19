import java.util.*;
public class Isomorphic_string {
    public static boolean is_isomorphic(String s1,String s2){
        HashMap<Character,Character> map1= new HashMap<>();
        HashMap<Character,Boolean> map2= new HashMap<>();
        for(int i=0;i<s1.length();i++){
            char ch1=s1.charAt(i);
            char ch2=s2.charAt(i);
            if(map1.containsKey(ch1)==true){
                if(map1.get(ch1)!=ch2){
                    return false;
                }
            }else{
                if(map2.containsKey(ch1)==true){
                    return false;
                }else{
                   map1.put(ch1,ch2);
                   map2.put(ch2,true);
                }
            }
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str1=scan.next();
        String str2=scan.next();
        System.out.print(is_isomorphic(str1, str2));
        scan.close();
    }
}
