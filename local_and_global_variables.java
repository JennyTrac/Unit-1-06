public class local_and_global_variables {
  
 public static void main(String[] args)
 {

int variableX = 30;

// local variable
    int variableX = 10;
    int variableY = 30;
    int variableZ = variableX + variableY;
    System.out.println(variableZ);

// global variable
    global variableX;
    int variableX = variableX + 1;
    int variableY = 30;
    int variableZ = variableX + variableY;
    System.out.println(variableZ);

 }

}
