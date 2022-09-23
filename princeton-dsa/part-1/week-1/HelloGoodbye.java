
public class HelloGoodbye {
  // ? What if I wanted to create fields with command line arguments?? Would that
  // be neccisary?
  // String name1;
  // String name2;

  public static void main(String[] args) {
    System.out.println("Hello " + args[0] + " and " + args[1] + ".");
    System.out.println("Goodbye " + args[1] + " and " + args[0] + ".");
  }

  // public void setNames(String[] args) {
  // this.name1 = args[0];
  // this.name2 = args[1];
  // }
}
