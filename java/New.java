// package java;

public class New {
    public static void main(String[] args) {
        int arr[]=new int[]{1,2,3,4,5,6};
        Sum(arr);
    }
    public static void Sum(int[] arr) {
        int result=0;
        for(int i=0;i<arr.length;i++){
            result=result+arr[i];
        }
        System.out.println("The Sum - "+result);
        
    }
    
}
