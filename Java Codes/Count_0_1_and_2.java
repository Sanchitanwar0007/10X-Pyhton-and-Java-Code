import java.util.*;
public class Count_0_1_and_2 {
    public static int count(int arr[]){
        int ans=0;
        int c0=0;
        int c1=0;
        int c2=0;
        String key=(c1-c0)+"#"+(c2-c1);
        HashMap<String,Integer> map=new HashMap<>();
        map.put(key,1);
        for(int val:arr){
            if(val==0){
                c0+=1;
            }else if(val==1){
                c1+=1;
            }else{
                c2+=1;
            }
            key=(c1-c0)+"#"+(c2-c1);
            if(map.containsKey(key)){
                ans+=map.get(key);
                map.put(key,map.get(key)+1);
            }else{
                map.put(key,1);
            }
        }

        return ans;
    }
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        int s=scan.nextInt();
        int arr[]= new int[s];
        for(int i=0;i<s;i++){
            arr[i]=scan.nextInt();
        }
        System.out.println(count(arr));
        scan.close();
    }
}
