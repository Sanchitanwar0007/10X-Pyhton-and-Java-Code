import java.util.*;
public class Task_completion {
    public static void task_completion(int size,int[] arr){
        HashSet<Integer> set= new HashSet<>();
        for(int i=0;i<arr.length;i++){
            set.add(arr[i]);
        }

        int r_arr[]=new int[size];
        for(int i=0;i<size;i++){
            r_arr[i]=i+1;
        }
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<r_arr.length;i++){
            // System.out.print(r_arr[i]+" ");
            if(!set.contains(r_arr[i])){
                // System.out.print(r_arr[i]+" ");
                list.add(r_arr[i]);
            }
        }
        System.out.println(set);
        for(int i=0;i<list.size();i++){
            if(i%2==0){
                System.out.print(list.get(i)+" ");
            }
        }
        System.out.println();
        for(int i=0;i<list.size();i++){
            if(i%2==1){
                System.out.print(list.get(i)+" ");
            }
        }
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int m=scan.nextInt();
        int arr[]=new int[m];
        for(int i=0;i<arr.length;i++){
            arr[i]=scan.nextInt();
        }
        task_completion(size,arr);
        scan.close();

    }
}
