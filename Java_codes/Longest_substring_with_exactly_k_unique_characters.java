import java.util.*;
public class Longest_substring_with_exactly_k_unique_characters {
    public static int longest_substring(String str, int k){
        int ans=0;
        int i=0;
        int j=0;
        HashMap<Character, Integer> map= new HashMap<>();
        while(true){
            boolean f1=true;
            boolean f2=true;
            while(i<str.length()){
                f1=false;
                char ch=str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                i++;
                if(map.size()>k){
                    break;
                }else{
                    if(map.size()==k){
                    ans=Math.max(ans,i-j);
                }
            }
            }
            while(j<i){
                f2=false;
                char ch=str.charAt(j);
                if(map.get(ch)==1){
                    map.remove(ch);
                }else{
                    map.put(ch,map.get(ch)-1);
                }
                j++;
                if(map.size()==k){
                    Math.max(ans,i-j);
                    break;
                }
                
            }
            if(f1 && f2){
                break;
            }
        }

        return ans;
    }
    public static void main(String[] args0){
        Scanner scan= new Scanner(System.in);
        String str=scan.next();
        int k= scan.nextInt();
        System.out.println(longest_substring(str,k));
        scan.close();
    }
}
