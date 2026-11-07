// package java;

public class ReturnMethod {
    public static void main(String[] args) {
        int[] arr=m();
        for (int i=0;i<arr.length;i++) {
            System.out.println(arr[i]);
        }
    }

    public static int[] m(){
        return new int[]{1,2,3};
    }
    
}
