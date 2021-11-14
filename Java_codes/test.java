import java.util.*;

public class test {
        public static void main(String[] args)
        {
            Scanner scan= new Scanner(System.in);
            String str=scan.nextLine();
            HashMap<String,Integer> map= new HashMap<>();
            String temp="";
            for(int i=0;i<str.length();i++){
                char ch=str.charAt(i);
                if(ch!=' '){
                    temp+=ch+"";
                }else{
                    if(map.containsKey(temp)){
                        map.put(temp,map.get(temp)+1);
                    }else{
                        map.put(temp,1);
                    }
                    temp="";
                }
            }
            if(map.containsKey(temp)){
                map.put(temp,map.get(temp)+1);
            }else{
                map.put(temp,1);
            }
            for(Map.Entry<String,Integer> entry:map.entrySet()){
                System.out.print(entry.getKey()+"->"+entry.getValue()+"\n");
            }
            scan.close();
           }
    }

