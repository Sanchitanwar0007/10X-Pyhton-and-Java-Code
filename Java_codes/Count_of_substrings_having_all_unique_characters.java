import java.util.*;
public class Count_of_substrings_having_all_unique_characters {
    public static int total_unique_substring(String str){
        int ans=0;
        int i=0;
        int j=0;
        int len=str.length();
        HashMap<Character,Integer> map= new HashMap<>();
        while(true){
            boolean f1=true;
            boolean f2=true;
            while(i<len){
                f1=false;
                char ch=str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                i++;
                if(map.get(ch)==2){
                    break;
                }else{
                    ans+=i-j;
                }    
            }
            while(j<i){
                f2=false;
                char ch=str.charAt(j);
                map.put(ch,map.get(ch)-1);
                j++;
                if(map.get(ch)==1){
                    ans+=i-j;
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
        String str=scan.next();
        System.out.print(total_unique_substring(str));
        scan.close();
    }
}
