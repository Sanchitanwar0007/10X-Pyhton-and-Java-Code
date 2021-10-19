import java.util.*;
public class Smallest_substrig_of_a_string_containing_all_the_characters_of_another_string {
    public static String smallest_string(String main_string,String sub_string){
        String ans="";
        HashMap<Character,Integer> map= new HashMap<>();
        for(int i=0;i<sub_string.length();i++){
            char ch=sub_string.charAt(i);
            map.put(ch,map.getOrDefault(ch,0)+1);
        }
        System.out.print(map);
        HashMap<Character,Integer> map2= new HashMap<>();
        int match_count=0;
        int sub_string_length=sub_string.length();
        int i=0;
        int j=0;
        while(true){
            boolean flag1=false;
            boolean flag2=false;
            while(i<main_string.length() && match_count<sub_string_length){
                char ch=main_string.charAt(i);
                map2.put(ch,map2.getOrDefault(ch,0)+1);

                if(map2.get(ch)<=map.getOrDefault(ch,0)){
                    // System.out.print("Yes");
                    match_count++;  
                }
                i++;
                flag1=true;
            }
            // System.out.println(map2);
            while(j<i && match_count==sub_string_length){
                String str=main_string.substring(j,i);
                if(ans.length()==0 || str.length()<ans.length()){
                   ans=str; 
                }
                char ch=main_string.charAt(j);
                if(map2.get(ch)==1){
                    map2.remove(ch);
                }else{
                    map2.put(ch,map2.get(ch)-1);
                }
                if(map2.getOrDefault(ch,0)<map.getOrDefault(ch,0)){
                    match_count--;
                }
                j++;
                flag2=true;
            }
            if(flag1==false && flag2==false){
                break;
            }
        }
        
        return ans;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        String main_string=scan.next();
        String sub_string=scan.next();
        System.out.println(smallest_string(main_string,sub_string));
    }
    }

