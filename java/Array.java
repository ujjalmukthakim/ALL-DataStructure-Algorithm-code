package java;


public class Array{
    public static void main(String[] args){
        // int arr[];
        // arr={1,2,3}
        int arr[]={1,2,3,4,5};
        int newArr[]=new int[]{12,13,14};
        System.out.println("Never Open - "+arr[3]+" But Open - " +newArr[1]);
        for(int i=0;i<arr.length;i++){
            System.out.println("Arr - "+arr[i]);
        }
    }
}