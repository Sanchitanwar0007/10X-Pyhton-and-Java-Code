import java.util.*;
public class Word_pattern {
    public static boolean wordPattern(String strs,String word){
        String[] words=word.split(" ");
        if(words.length!=strs.length()){
            return false;
        }
        HashMap<Character,String> map1= new HashMap<>();
        HashMap<String,Boolean> map2= new HashMap<>();
        for(int i=0;i<words.length;i++){
            String str=words[i];
            char ch=strs.charAt(i);
            if(map1.containsKey(ch)==true){
                if(!(map1.get(ch).equals(str))){
                    return false;
                }
            }else{
                if(map2.containsKey(str)){
                    return false;
                }else{
                    map1.put(ch,str);
                    map2.put(str,true);
                }
            }
        }
        return true;
    }
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
		String pattern = scn.nextLine();
		String words = scn.nextLine();
		System.out.println(wordPattern(pattern,words));
        scn.close();
    }
}
