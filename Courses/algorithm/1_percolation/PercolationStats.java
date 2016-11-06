import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private double[] results;
    private int trailsN;
    public PercolationStats(int n, int trials) {    
    // perform trials independent experiments on an n-by-n grid
        trailsN = trials;
        int sites = n * n;
        results = new double[trailsN];
        for (int i = 0; i < trailsN; ++i) {
            int count = 0;
            Percolation p = new Percolation(n);
            while (!p.percolates()) {
                int a = StdRandom.uniform(1, n+1);
                int b = StdRandom.uniform(1, n+1);
                if (!p.isOpen(a, b)) {
                    p.open(a, b);
                    ++count;
                }
            }
            results[i] = (double) count / sites;
        }
        // for (int i = 0; i < trailsN; ++i) { StdOut.printf("%g ", results[i]); }
    }

    public double mean() {                          
    // sample mean of percolation threshold
        return StdStats.mean(results);
    }

    public double stddev() {                        
    // sample standard deviation of percolation threshold
        return StdStats.stddev(results);
    }
    public double confidenceLo() {                 
    // low  endpoint of 95% confidence interval
        double w = StdStats.stddev(results); // better code style ?
        double mu = StdStats.mean(results);
        return mu - 1.96 * w / Math.sqrt(trailsN);
    }
    public double confidenceHi() {                 
    // high endpoint of 95% confidence interval
        double w = StdStats.stddev(results); // better code style ?
        double mu = StdStats.mean(results);
        return mu + 1.96 * w / Math.sqrt(trailsN);
    }

    public static void main(String[] args) {    
    // test client (described below)
        int n = Integer.parseInt(args[0]);
        int trails = Integer.parseInt(args[1]);
        if (n <= 0 || trails <= 0) {
            throw new java.lang.IllegalArgumentException();
        }
        PercolationStats ps = new PercolationStats(n, trails);
        StdOut.printf("mean = %f\n", ps.mean());
        StdOut.printf("stddev = %f\n", ps.stddev());
        StdOut.printf("95%% confidence interval = %f, %f\n", 
            ps.confidenceLo(), ps.confidenceHi());
    }
}