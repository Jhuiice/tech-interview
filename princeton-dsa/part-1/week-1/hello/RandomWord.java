import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomWord {
  public static void main(String[] args) {
    /*
     * insert a strig of text and use Kruths method to reandomly print a word.
     * When reading the ith word, select it with probability 1/i to be the champion,
     * Replacing the previous champion. After reading all the words print the
     * surviving champion.
     */
    String text = StdIn.readString(args[0]);
    StdOut(StdRandom(text));
  }
}
