// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);

        // Read the number of testcases
        int n = sc.nextInt();
        int m = sc.nextInt();
        int p = sc.nextInt();

        int[][] data = new int[m][3];
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = 0;
        }

        // Process each test case
        for (int t = 0; t < m; t++) {
            data[t][0] = sc.nextInt();
            data[t][1] = sc.nextInt();
            data[t][2] = sc.nextInt();
        }

        Comparator<int[]> myComparator = new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] != o2[1]) {
                    return o1[1] - o2[1];
                }
                return o1[0] - o2[0];
            }
        };

        Arrays.sort(data, myComparator);
        for (int i = 0; i < m; i++) {
            int current = 0;
            for (int k = data[i][0]; k <= data[i][1]; k++) {
                current = (current + answer[k]) % p;
            }

            System.out.println(data[i][0] + " " + data[i][1] + " " + data[i][2]);
        }

    }
}
