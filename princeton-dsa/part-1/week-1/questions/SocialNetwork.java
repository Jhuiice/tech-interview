
public class SocialNetwork {
  private int[] users;
  private int[] timeStamp;
  private int[] sz;

  public SocialNetwork(int N, int M) {
    for (int i = 0; i < N; i++) {
      this.users[i] = i;
      int rint = (int) Math.rint((double) N);
      while (rint != i) {
        rint = (int) Math.rint((double) N);
      }
      this.timeStamp[i] = rint;
    }
    this.sz = new int[N];

    System.out.println("hello");
    System.out.println(this.users);
    System.out.println(this.timeStamp);
  }

  public void union(int p, int q) {
    int qid = this.users[p];
    int pid = this.users[q];

    if (qid == pid)
      return;
    if (sz[q] > sz[p]) {
      this.users[q] = pid;
      sz[q] += sz[p];
    } else {
      this.users[p] = qid;
      sz[p] += sz[q];
    }
  }

  // ? How do I compress the graph to give the component to the main largest root?
  public int root(int i) {
    while (users[i] != i) {
      this.users[i] = this.users[this.users[i]]; // this is path compression
      i = this.users[i];
    }
    return i;
  }

  public void checkSocials() {
    for (int i = 0; i < this.users.length; i++) {
      continue;
    }
  }

  public static void main(String[] args) {

  }
}
