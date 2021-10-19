import java.util.*;
public class k_anagrams {
    public static boolean is_anagram(String s1,String s2,int k){
        if(s1.length()!=s2.length()){
            return false;
        }
        HashMap<Character,Integer> map= new HashMap<>();
        for(int i=0;i<s1.length();i++){
            char ch=s1.charAt(i);
            map.put(ch,map.getOrDefault(ch,0)+1);
        }
        for(int i=0;i<s2.length();i++){
            char ch=s2.charAt(i);
            if(map.getOrDefault(ch,0)>0){
                map.put(ch,map.get(ch)-1);
            }
        }
        int count=0;
        for(char ch:map.keySet()){
            if(map.get(ch)>0){
                count+=map.get(ch);
            }
        }
        if(count>k){
            return false;
        }else{
            return true;
        }  
    }
    public static void main(String args[]){
        Scanner scan= new Scanner(System.in);
        String s1=scan.next();
        String s2=scan.next();
        int k=scan.nextInt();
        System.out.print(is_anagram(s1,s2,k));
        scan.close();
    }
}
