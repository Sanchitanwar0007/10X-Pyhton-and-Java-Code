import java.io.*;
import java.util.*;
public class Words_permutation {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
    
        HashMap<Character, Integer> fmap = new HashMap<>();
        for(char ch: str.toCharArray()){
          if(fmap.containsKey(ch)){
            fmap.put(ch, fmap.get(ch) + 1);
          } else {
            fmap.put(ch, 1);
          }
        }
    
        generateWords(1, str.length(), fmap, "");
      }
      public static void generateWords(int total,int target,HashMap<Character,Integer> map,String ans){
        if(ans.length()==target){
            System.out.println(ans);
            return;
        }
        for(Character ch:map.keySet()){
            if(map.get(ch)>0){
                map.put(ch,map.get(ch)-1);
                generateWords(total+1, target, map, ans+ch);
                map.put(ch,map.get(ch)+1);
            }
        }
      }
}
