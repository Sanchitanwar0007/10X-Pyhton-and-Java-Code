import java.util.*;
public class Squqre_box_pattern {
    public static void main(String[] args)
        {
        Scanner scan= new Scanner(System.in);
        int num=scan.nextInt();
        String space="";
        int arr[]=new int[num];
        for(int i=0;i<num;i++){
            arr[i]=2*i;
        }
        for(int i=1;i<=arr[num-2];i++){
            space+=" ";
        }
        String str="";
        for(int i=1;i<=num;i++){
            str="";
            for(int j=1;j<=num;j++){
                if(i==1){
                    str+="*"+" ";
                }else if(i==num){
                    str+="*"+" ";
                }else{
                    str="";
                    str+="* "+space+"*";
                }
            }

            System.out.println(str);
            // str="";
        }
        scan.close();
    }

}
