import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdOut;

public class RandomWord {
  public static void main(String[] args) {
    /*
     * insert a strig of text and use Kruths method to reandomly print a word.
     * When reading the ith word, select it with probability 1/i to be the champion,
     * Replacing the previous champion. After reading all the words print the
     * surviving champion.
     */
    String word = "";
    // for (int i = 0; i<args.length; i++) {
    // if (stdRandom.bernoulli(1/args.length)) {
    // word = args[i];
    // }
    // }
    // System.out.println(args);
    // for (int i = 0; i < args.length; i++) {
    // System.out.println(args[i]);
    // System.out.println(StdIn.readString());
    // }
    // System.out.println(args[0]);
    // String[] arrStr = args[1].split(" ", 0);
    // int i = arrStr.length; // should be equal to length of words ? How do I get
    // that?
    // System.out.println(i);
    String temp;
    while (!StdIn.isEmpty()) {
      temp = StdIn.readString();
      // System.out.println(StdIn.readString());
      if (StdRandom.bernoulli(1 / 8.0)) { // remember type division by int truncates the number = no remainder...
        word = temp;
      }
      // // System.out.println(StdIn.readString());
      // }

    }
    System.out.println(word);
  }
}
