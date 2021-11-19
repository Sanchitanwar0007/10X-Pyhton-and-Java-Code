import java.util.HashMap;
import java.util.Scanner;


public class word_k_selection_with_repeatation {
    public static void main(String[] args) {
        Scanner scan= new Scanner(System.in);
        String str= scan.next();
        int k=scan.nextInt();
        HashMap<Character,Integer> map= new HashMap<>();
        String temp="";
        for(int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            if(map.containsKey(ch)==false){
                map.put(ch,1);
                temp+=ch;
            }else{
                map.put(ch,map.get(ch)+1);
            }
        }
        generate(temp,map,"",0,k);
        scan.close();
    }
    public static void generate(String s,HashMap<Character,Integer> map,String s2,int start,int end){
        if(start==end){
            System.out.println(s2);
            return;
        }
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            if(map.get(ch)>0){
                map.put(ch,map.get(ch)-1);
                generate(s, map, s2+ch, start+1, end);
                map.put(ch,map.get(ch)+1);
            }
        
        }
    }
}
