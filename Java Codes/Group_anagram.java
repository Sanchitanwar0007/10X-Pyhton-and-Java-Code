import java.util.*;
public class Group_anagram {
    public static ArrayList<ArrayList<String>> group(String[] arr){
        HashMap<HashMap<Character,Integer>,ArrayList<String>> bmap= new HashMap<>();
        for(String str:arr){
            HashMap<Character,Integer> map= new HashMap<>();
            for(int i=0;i<str.length();i++){
                char ch=str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
            }
            if(!bmap.containsKey(map)){
                ArrayList<String> list= new ArrayList<>();
                list.add(str);
                bmap.put(map,list);
            }else{
                ArrayList<String> llist=bmap.get(map);
                llist.add(str);
            }
        }
        ArrayList<ArrayList<String>> ans= new ArrayList<>();
        for(ArrayList<String> s:bmap.values()){
            ans.add(s);
        }
        return ans; 
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        String arr[]= new String[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.next();
        }
        display(group(arr));
        scan.close();
    }
    public static void display(ArrayList<ArrayList<String>> list) {
		for (int i = 0; i < list.size(); i++) {
			ArrayList<String> currList = list.get(i);
			for (int j = 0; j < currList.size(); j++) {
				System.out.print(currList.get(j) + " ");
			}
			System.out.println();
		}
	}
}
