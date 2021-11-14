import java.util.*;
public class Count_of_substring_with_exactly_k_unique_characters {
    public static int for_kequal_1(String str){
        int ans=0;
        int i=-1;
        int j=-1;
        HashMap<Character,Integer> map= new HashMap<>();
        while(true){
            boolean f1=true;
            boolean f2=true;
            while(i<str.length()-1){
                f1=false;
                i++;
                char ch=str.charAt(i);
                map.put(ch,map.getOrDefault(ch,0)+1);
                if(map.size()==2){
                    removemap(map, ch);
                    i--;
                    break;
                }
            }
            while(j<i){
                f2=false;
                
                if(map.size()==1){
                    ans+=i-j;
                }
                j++;
                char ch=str.charAt(j);
                removemap(map, ch);
                if(map.size()==0){
                    break;
                }
            }
            if(f1 && f2){
                break;
            }
        }

        return ans;
    }
    public static int k_unique_character(String str,int k){
        if(k==1){
            return for_kequal_1(str);
        }
        int ans=0;
        HashMap<Character,Integer> map_big= new HashMap<>();
        HashMap<Character,Integer> map_small= new HashMap<>();
        int ib=-1;
        int is=-1;
        int j=-1;
        while(true){
            boolean f1=true;
            boolean f2=true;
            boolean f3=true;
            while(ib<str.length()-1){
                f1=false;
                ib++;
                char ch= str.charAt(ib);
                map_big.put(ch,map_big.getOrDefault(ch,0)+1);
                if(map_big.size()==k+1){
                    ib--;
                    removemap(map_big, ch);
                    break;
                }
            }
            while(is<ib){
                f2=false;
                is++;
                char ch=str.charAt(is);
                map_small.put(ch,map_small.getOrDefault(ch,0)+1);
                if(map_small.size()==k){
                    removemap(map_small, ch);
                    is--;
                    break;
                }
            }
            while(j<is){
                j++;
                f3=false;
                if(map_big.size()==k && map_small.size()==k-1){
                    ans+=ib-is;
                }
                char ch=str.charAt(j);
                removemap(map_big,ch);
                removemap(map_small,ch);
                if(map_big.size()<k || map_small.size()<k-1){
                    break;
                }
            } 
            if(f1 && f2 && f3){
                break;
            }  
        }

        return ans;
    }
    public static void removemap(HashMap<Character,Integer> map, char ch){
        if(map.get(ch)==1){
            map.remove(ch);
        }else{
            map.put(ch,map.getOrDefault(ch,0)-1);
        }
    }
public static void main(String arga[]){
    Scanner scan= new Scanner(System.in);
    String str= scan.next();
    int k=scan.nextInt();
    System.out.print(k_unique_character(str, k));
    scan.close();
}
}
