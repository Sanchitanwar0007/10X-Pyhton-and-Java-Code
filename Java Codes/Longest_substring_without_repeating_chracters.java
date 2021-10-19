import java.util.*;
public class Longest_substring_without_repeating_chracters {
    public static int longest_length(String str){
        int ans=0;
        HashMap<Character,Integer> map= new HashMap<>();
        int i=0;
        int j=0;
        while(true){
            boolean flag=false;
            boolean flag2=false;
            while(i<str.length()){
                char ch= str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                i++;
                flag=true;
                if(map.get(ch)==2){
                    break;
                }else{
                    // System.out.print("ans");
                    int temp_len=i-j;
                    if(temp_len>ans){
                    ans=temp_len;
                    }
                }
                
            }

            while(j<i){
                char ch = str.charAt(j);
                map.put(ch,map.get(ch)-1);
                j++;
                flag2=true;
                if(map.get(ch)==1){
                    break;
                }
                
            }
            if(flag==false && flag2==false){
                break;
            }
        }

        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str= scan.next();
        System.out.print(longest_length(str));
        scan.close();
    }
}
