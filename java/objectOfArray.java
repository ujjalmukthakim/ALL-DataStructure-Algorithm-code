package java;

class Students{
    String name;
    int id;

    Students(String name,int id){
        this.name=name;
        this.id=id;
    }
}

public class objectOfArray {
    public static void main(String[] args) {

        Students[] stObj=new Students[3];
        stObj[0]=new Students("Shagor", 1);
        stObj[1]=new Students("Sanim", 2);
        stObj[2]=new Students("Echo", 3);

        for(int i=0;i<stObj.length;i++){
            System.out.println("The Object's Name - "+stObj[i].name+" The Object's Id - "+stObj[i].id);
        }
        
    }
}
