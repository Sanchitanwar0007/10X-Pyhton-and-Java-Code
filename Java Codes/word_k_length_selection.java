import java.util.*;
import java.io.*;
public class word_k_length_selection {
        public static void generate(int k,String str,Character[] arr,int total ,int ts){
            if(total==str.length()){
                if(ts==k){
                    for(int i=0;i<arr.length;i++){
                        System.out.print(arr[i]);
                    }
                    System.out.println();
                }
                
                return;
            }
            char ch=str.charAt(total);
            for(int i=0;i<arr.length;i++){
                if(arr[i]==null){
                    arr[i]=ch;
                    generate(k, str, arr, total+1, ts+1);
                    arr[i]=null;
                }
            }
            generate(k, str, arr, total+1, ts);
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
            generate(k, ustr, new Character[k],0,0);
    }
}
