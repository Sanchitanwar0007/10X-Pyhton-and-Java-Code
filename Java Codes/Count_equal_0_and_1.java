import java.util.*;
public class Count_equal_0_and_1 {
    public static int count(char[] arr){
        HashMap<Integer,Integer> map=new HashMap<>();
        map.put(0,1);
        int ans=0;
        int sum=0;
        for(int i=0;i<arr.length;i++){
            if(arr[i]=='0'){
                sum-=1;
            }else{
                sum+=1;
            }
            if(map.containsKey(sum)){
                ans+=map.get(sum);
                map.put(sum,map.get(sum)+1);
            }else{
                map.put(sum,1);
            }
            
        }
        return ans;
    }
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in);
        String zero_one=scan.next();
        int res=count(zero_one.toCharArray());
        System.out.print(res);
        scan.close();
    }
}
