import java.util.*;
public class High_frequency_char{
    public static void main(String[] args) throws Exception {
        Scanner scan=new Scanner(System.in);
        String str=scan.next();
        HashMap<Character,Integer> map=new HashMap<>();
        for(int i=0;i<str.length();i++){
            char ch=str.charAt(i);
            if(map.containsKey(ch)){
                map.put(ch,map.get(ch)+1);
                
            }else{
                map.put(ch,1);
            }
        }
        int max=Integer.MIN_VALUE;
        char res=' ';
        for(char ch:map.keySet()){
            int val=map.get(ch);
            if(val>max){
                max=val;
                res=ch;
            }
        }
        System.out.println(res);
        scan.close();
    }
}