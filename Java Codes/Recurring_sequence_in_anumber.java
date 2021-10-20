import java.util.*;
public class Recurring_sequence_in_anumber {
    public static String recurring_numer(int num,int deno){
        StringBuilder ans= new StringBuilder();
        int q=num/deno;
        int rem=num%deno;
        ans.append(q);
        if(rem==0){
            return ans.toString();
        }else{
            ans.append(".");
            HashMap<Integer,Integer> map= new HashMap<>();
            while(rem!=0){
                if(map.containsKey(rem)){
                    int len=map.get(rem);
                    ans.insert(len,"(");
                    ans.append(")");
                    break;
                }else{
                map.put(rem,ans.length());
                rem*=10;
                q=rem/deno;
                rem=rem%deno;
                ans.append(q);
               
            }
        }
        }
        return ans.toString();
    }

    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int num=scan.nextInt();
        int deno=scan.nextInt();
        System.out.print(recurring_numer(num,deno));
        scan.close();
    }
}
