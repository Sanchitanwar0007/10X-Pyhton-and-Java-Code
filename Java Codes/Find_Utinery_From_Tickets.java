import java.util.*;
public class Find_Utinery_From_Tickets {
    public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int noofpairs_src_des = scn.nextInt();
		HashMap<String, String> map = new HashMap<>();
		for (int i = 0; i < noofpairs_src_des; i++) {
			String s1 = scn.next();
			String s2 = scn.next();
			map.put(s1, s2);	
		}
        HashMap<String,Boolean> start=new HashMap<>();
        for(String val:map.keySet()){
            String dest=map.get(val);
            start.put(dest,false);
            if(start.containsKey(val)==false){
                start.put(val,true);
            }
        }
        String src="";
        for(String val:start.keySet()){
            if(start.get(val)==true){
                src=val;
                break;
            }
        }
       while(true){
           if(map.containsKey(src)){
               System.out.print(src+"->");
               src=map.get(src);
           }else{
               System.out.print(src+".");
               break;
           }
       }
       scn.close();
	}
}
