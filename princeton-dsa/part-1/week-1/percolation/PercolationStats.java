import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;
// import java.;

public class PercolationStats {
  double[] percTrials; // this is how many tiles are filled

  public PercolationStats(int n, int trials) {
    percTrials = new double[trials];

    // Percolation perc = new Percolation(n);

  }

  public double mean() {
    return 1;
  }

  public double stddev() {
    return 1;
  }

  public double confidenceLow() {
    return 1;
  }

  public double confidenceHi() {
    return 1;
  }

  public static void main(String[] args) {
    int n = 0;
    int trials = 0;
    try {
      n = Integer.valueOf(args[0]);
      trials = Integer.valueOf(args[1]);
      if (n <= 0) {
        throw new IllegalArgumentException("N Must be larger than 0.");
        // ! Must create new instances when using class ^^
      }
    } catch (Exception e) {
      StdOut.println("Error, ", e);
    }

    // Percolation perc = new Percolation(n);
    int fillCount = 0;
    int openCount = 0;
    int row, col;
    while (trials > 0) {
      Percolation perc = new Percolation(n);
      WeightedQuickUnionUF wquf = new WeightedQuickUnionUF((n - 2) * (n - 2));
      while (perc.percolates() != true) {
        row = StdRandom.uniformDouble(1, n);
        col = StdRandom.uniformDouble(1, n);
        if (perc.isOpen(row, col)) {
          continue;
        } else {
          perc.open(row, col);
          openCount++;
        }
        fillCount++;
      }
      trials--;
    }
  }

}
