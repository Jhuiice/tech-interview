import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

// TODO implemet WeightedQuickUnionUF into the percolation class
// Must solve the graph and check for percolation

public class Percolation extends WeightedQuickUnionUF {
  // when the nodes are opened they are given their row * col id num
  int[][] idMatrix;
  int openSites;
  int rootValue;
  // WeightedQuickUnionUF id;

  // initialize nodes to be blocked. Blocked value = 0;
  public Percolation(int n) {
    super((n - 2) * (n - 2));
    if (n <= 0) {
      throw new IllegalArgumentException("n must be greater than 0.");
    }
    this.idMatrix = new int[n][n];
    for (int i = 1; i < n - 1; i++) {
      for (int j = 1; j < n - 1; j++) {
        this.idMatrix[i][j] = 0;
      }
    }
    // this.id = new WeightedQuickUnionUF(numNodes);
    this.openSites = 0;
    this.rootValue = -1; // predefined root value
  }

  // open sites by giving the nodes their node number ie. row X col = n
  public void open(int row, int col) {
    this.idMatrix[row][col] = row * col;
    this.openSites++;
  }

  public boolean isOpen(int row, int col) {
    return this.idMatrix[row][col] == row * col; // or value is equal to starting node
  }

  // sites that can be connected to top node and graph
  public boolean isFull(int row, int col) {
    // the site would be full if it is connected to the top node.
    // ? How can we create and connected a top node to the open spots
    // of the top row?
    // Components are consisted of nodes and the bumbers. The index (i) represents
    // the node number
    // The value represents which tree its connected to ie the root value.
    // If the root value matches the node value of row and col then they are
    // connected.
    // return WeightedQuickUnionUF.find(row, col) WeightedQuickUnionUF

    return this.idMatrix[row][col] == this.rootValue;
  }

  public int numberOfOpenSites() {
    return this.openSites;
  }

  public boolean percolates() {
    // if top node is connected to bottom node this system percolates.
    for (int i = 1; i < this.idMatrix.length - 1; i++) {
      if (this.idMatrix[this.idMatrix.length - 2][i] == this.rootValue) {
        return true;
      }
    }
    return false;
  }

  public static void main(String[] args) {
  }
}
