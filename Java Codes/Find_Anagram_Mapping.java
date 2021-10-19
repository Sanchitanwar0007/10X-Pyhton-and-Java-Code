import java.util.*;
public class Find_Anagram_Mapping {
    public static class Pair{
        int idx=0;
        ArrayList<Integer> list= new ArrayList<>();
    }
    public static int[] find_indices(int arr2[],int arr1[]){
        
        HashMap<Integer,Pair> map= new HashMap<>();
        for(int i=0;i<arr2.length;i++){
            if(map.containsKey(arr2[i])){
                Pair p=map.get(arr2[i]);
                p.list.add(i);
                map.put(arr2[i],p);
            }else{
                Pair p= new Pair();
                p.list.add(i);
                map.put(arr2[i],p);
            }
        }
        int arr[]= new int[arr2.length];
        for(int i=0;i<arr1.length;i++){
            Pair p=map.get(arr1[i]);
            int index=p.idx;
            arr[i]=p.list.get(index);
            p.idx++;
        }
        return arr;
    }
    public static void main(String[] args){
        Scanner scan= new Scanner(System.in);
        int size=scan.nextInt();
        int arr[]=new int[size];
        int arr2[]=new int[size];
        for(int i=0;i<size;i++){
            arr[i]=scan.nextInt();
        }
        for(int i=0;i<size;i++){
            arr2[i]=scan.nextInt();
        }
        int arr1[]=find_indices(arr,arr2);
        for(int i=0;i<arr1.length;i++){
            System.out.print(arr1[i]+" ");
        }
        scan.close();
    }

}
