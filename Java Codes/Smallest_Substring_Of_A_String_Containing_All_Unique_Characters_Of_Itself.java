import java.util.*;
public class Smallest_Substring_Of_A_String_Containing_All_Unique_Characters_Of_Itself {
    public static int smallest_string_length(String s){
        int len=s.length();
        HashSet<Character> set= new HashSet<>();
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            set.add(ch);
        }
        HashMap<Character,Integer> map= new HashMap<>();
        int i=0;
        int j=0;

        while(true){
            boolean flag=false;
            boolean flag2=false;
            while(i<s.length() && map.size()<set.size()){
                char ch=s.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                i++;
                flag=true;
            }
            // System.out.print(i+" "+j);
            while(j<i && map.size()==set.size()){

                int temp_len=i-j;
                // System.out.print(temp_len);
                if(len>temp_len){
                    len=temp_len;
                }
                char ch= s.charAt(j);
                if(map.get(ch)==1){
                    map.remove(ch);
                }else{
                    map.put(ch,map.get(ch)-1);
                }
                flag2=true;
                j++;
            }
            if(flag==false && flag2==false){
                break;
            }
        }       
 
        return len;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String str= scan.next();
        System.out.println(smallest_string_length(str));
        scan.close();
    }
}
