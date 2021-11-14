import java.util.*;
public class Count_if_Longest_Substring_with_atmost_k_unique_characters {
    public static int count_substring(String str,int k){
        int ans=0;
        int i=-1;
        int j=-1;
        HashMap<Character,Integer> map= new HashMap<>();
        while(true){
            while(i<str.length()-1){
                i++;
                char ch =str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                if(map.size()<=k){
                    ans+=i-j;
                }else{
                    break;
                }
            }
            if(i==str.length()-1 && map.size()<=k){
                break;
            }

            while(j<i){
                j++;
                char ch=str.charAt(j);
                if(map.get(ch)==1){
                    map.remove(ch);
                }else{
                    map.put(ch,map.get(ch)-1);

                }
                if(map.size()==k){
                    ans+=i-j;
                    break;
                }
            }
        }


        return ans;
    }
    public static void main(String[] args){
    Scanner scan= new Scanner(System.in);
    String str=scan.next();
    int k=scan.nextInt();
    int res=count_substring(str,k);
    System.out.print(res);
    scan.close();
    }
}
