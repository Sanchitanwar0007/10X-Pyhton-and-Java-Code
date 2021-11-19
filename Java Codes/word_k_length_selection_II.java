import java.util.*;
import java.io.*;
public class word_k_length_selection_II {
    public static void generate(HashSet<Character> set,String rch,int start,String ans,int k){
      if(start==k){
        System.out.println(ans);
        return;
      }
      for(int i=0;i<rch.length();i++){
        char ch=rch.charAt(i);
        if(set.contains(ch)==false){
          set.add(ch);
          generate(set, rch, start+1, ans+ch,k);
          set.remove(ch);
        }
      }
    }
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    int k = Integer.parseInt(br.readLine());

    HashSet<Character> unique = new HashSet<>();
    String ustr = "";
    for (char ch : str.toCharArray()) {
      if (unique.contains(ch) == false) {
        unique.add(ch);
        ustr += ch;
      }
    }
    generate(new HashSet<Character>(),ustr,0,"",k);
  }

}
