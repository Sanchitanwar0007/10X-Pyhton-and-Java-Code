import java.io.*;
import java.util.HashSet;
public class Word_k_selection_II {
    public static void main(String[] args) throws Exception {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        String str=br.readLine();
        int k=Integer.parseInt(br.readLine());
        String nstr="";
        HashSet<Character> set= new HashSet<>();
        for(int i=0;i<str.length();i++){
            char ch= str.charAt(i);
            if(!set.contains(ch)){
                nstr+=ch;
                set.add(ch);
            }
        }
        generat_combination(-1,nstr,1,"",k);

    }
    public static void generat_combination(int tar,String nstr,int sel,String ans,int k){
        if(sel>k){
            System.out.println(ans);
            return;
        }
        for(int i=tar+1;i<nstr.length();i++){
            char ch=nstr.charAt(i);
            generat_combination(i, nstr, sel+1, ans+ch, k);
        }

    }
}
