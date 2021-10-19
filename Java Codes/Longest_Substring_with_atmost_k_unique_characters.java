import java.util.*;
public class Longest_Substring_with_atmost_k_unique_characters {
    public static int longest_substring(String str,int k){
        int ans=0;
        int i=-1;
        int j=-1;
        HashMap<Character,Integer> map= new HashMap<>();
        while(true){
            boolean f1=true;
            boolean f2=true;
            while(i<str.length()-1){
                f1=false;
                i++;
                char ch= str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                if(map.size()<=k){
                    ans=Math.max(ans,i-j);
                }else{
                    break;
                }
            }
            while(j<i){
                j++;
                f2=false;
                char ch=str.charAt(j);
                if(map.get(ch)==1){
                    
                    map.remove(ch);
                }else{
                    map.put(ch,map.get(ch)-1);
                }
                if(map.size()==k){
                    break;
                }
                
            }
            if(f1 && f2){
                break;
            }
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str= scan.next();
        int k=scan.nextInt();
        int res=longest_substring(str,k);
        System.out.print(res);
        scan.close();
    }
}
