import java.util.*;
public class Find_all_anagrams_in_string {
    public static boolean compare(HashMap<Character,Integer> smap,HashMap<Character,Integer> lmap){
        for(char ch:smap.keySet()){
            if(smap.get(ch)!=lmap.getOrDefault(ch,0)){
                return false;
            }
        }
        return true;
    }
    public static void total_anagram(String long_string,String short_string){
        HashMap<Character,Integer> smap=new HashMap<>();
        
        for(int i=0;i<short_string.length();i++){
            char ch=short_string.charAt(i);
            smap.put(ch,smap.getOrDefault(ch,0)+1);
        }
        HashMap<Character,Integer> map=new HashMap<>();
        for(int i=0;i<short_string.length();i++){
            char ch=long_string.charAt(i);
            map.put(ch,map.getOrDefault(ch,0)+1);
        }
        int ans=0;
        int j=0;
        String idx="";
        for(int i=short_string.length();i<long_string.length();i++){
            char ch=long_string.charAt(i);
            if(compare(smap,map)==true){
                ans++;
                idx+=j+" ";
            }
            map.put(ch,map.getOrDefault(ch,0)+1);
            char chr=long_string.charAt(j);
            if(map.get(chr)==1){
                map.remove(chr);
            }else{
                map.put(chr,map.get(chr)-1);
            }
            j++;
        }
        if(compare(smap,map)==true){
            ans++;
            idx+=j+" ";
        }
        System.out.println(ans);
        System.out.print(idx);
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str=scan.next();
        String str2=scan.next();
        total_anagram(str, str2);
        scan.close();
    }
}
