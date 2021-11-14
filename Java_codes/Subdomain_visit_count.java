import java.util.*;
public class Subdomain_visit_count {
    public static List<String> subdomainVisits(String[] arr) {
        HashMap<String,Integer> map= new HashMap<>();
		for(String words:arr){
            String values[]=words.split(" ");
            int val=Integer.parseInt(values[0]);
            
            String domain[]=values[1].split("\\.");
            StringBuilder sb= new StringBuilder();
            for(int i=domain.length-1;i>=0;i--){
                System.out.println(domain[i]);
                
                if(i==domain.length-1){
                    sb.append(domain[i]);
                }else{
                    sb.insert(0,".");
                    sb.insert(0,domain[i]);
                }
                map.put(sb.toString(),map.getOrDefault(sb.toString(),0)+val);
            }
        }
        ArrayList<String> list= new ArrayList<>();
        for(String val:map.keySet()){
            StringBuilder sb2= new StringBuilder();
            sb2.append(map.get(val));
            sb2.append(" ");
            sb2.append(val);
            list.add(sb2.toString());
        }
        return list;
	}
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
		int n = Integer.parseInt(s.nextLine());
		String[] cpd = new String[n];
		for (int i = 0; i < cpd.length; i++) {
			cpd[i] = s.nextLine();
		}
		List<String> ans = subdomainVisits(cpd);
		Collections.sort(ans);
		System.out.println(ans);
        s.close();
    }
}
