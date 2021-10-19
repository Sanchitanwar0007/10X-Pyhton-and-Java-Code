import java.util.*;
public class Group_Shifted_String {
    public static String getKey(String str){
        String key="";
        for(int i=1;i<str.length();i++){
            char ch=str.charAt(i);
            char ch2=str.charAt(i-1);
            int val=ch-ch2;
            if(val<26){
                val+=26;
            }
            key+=val+"#";
        }
        key+=".";
        return key;
    }
    public static ArrayList<ArrayList<String>> groupShiftedStrings(String arr[]){
        HashMap<String,ArrayList<String>> map= new HashMap<>();
        for(String str:arr){
            String key=getKey(str);
            if(map.containsKey(key)){
                ArrayList<String> list= map.get(key);
                list.add(str);
            }else{
                ArrayList<String> list= new ArrayList<>();
                list.add(str);
                map.put(key,list);
            }
        }
        ArrayList<ArrayList<String>> ans= new ArrayList<>();
        for(ArrayList<String> s:map.values()){
            ans.add(s);
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] arr = new String[N];
		for (int i = 0; i < N; i++) {
			arr[i] = sc.next();
		}
		ArrayList<ArrayList<String>> shiftedGroup = groupShiftedStrings(arr);
		for (ArrayList<String> lst : shiftedGroup) {
			Collections.sort(lst);
		}		
        display(shiftedGroup);
        sc.close();
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
