import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

public class WordLock {

    public int[][] words;
    public int[][] occurrences;
    public int[][] tempOccurrences;
    public int[] totals;
    public int best;
    public int[][] guess;
    public int[][] bestGuess;
    public boolean hasGuessed;

    public WordLock() {
        hasGuessed = false;
        this.words = new int[7647][8];
        this.occurrences = new int[8][27];
        this.tempOccurrences = new int[8][27];
        this.totals = new int[8];
        this.best = 0;
        this.guess = new int[8][10];
        this.bestGuess = new int[8][10];
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 27; j++) {
                occurrences[i][j] = 0;
            }
        }
        int c = 0;
        try {
            File myObj = new File("src/input.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                int j = 0;
                for (char ch: data.toCharArray()) {
                    this.words[c][j] = ch - 96;
                    this.occurrences[j][ch - 96] += 1;
                    j++;
                }
                while (j < 8) {
                    this.words[c][j] = 0;
                    this.occurrences[j][0] += 1;
                    j++;
                }
                for (int k = 0; k < 8; k++) {
                    System.out.print(this.words[c][k]);
                    System.out.print(' ');
                }
                System.out.println(" ");
                c++;
                System.out.println(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        for (int i = 0; i < 8; i++) {
            int total = 0;
            for (int j = 0; j < 27; j++) {
                System.out.print(this.occurrences[i][j]);
                System.out.print(" ");
                this.occurrences[i][j] = this.occurrences[i][j] * this.occurrences[i][j];
                total += this.occurrences[i][j];
            }
            this.totals[i] = total;
            System.out.print(total);
            System.out.println(" ");
        }
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 27; j++) {
                this.tempOccurrences[i][j] = this.occurrences[i][j];
            }
        }
        Random random = new Random();
        System.out.println(" ");
        int q = 0;
        //int totalTotal = 0;
        while (true) {
            // Find random combination
            if (!this.hasGuessed) {
                for (int i = 0; i < 8; i++) {
                    int tempTotal = this.totals[i];
                    for (int j = 0; j < 10; j++) {
                        int rand = random.nextInt(tempTotal);
                        int a = -1;
                        while (rand >= 0) {
                            a++;
                            rand -= this.tempOccurrences[i][a];
                        }

                        this.guess[i][j] = a;
                        tempTotal -= this.tempOccurrences[i][a];
                        this.tempOccurrences[i][a] = 0;
                        //System.out.print(a);
                        //System.out.print(" ");
                    }
                    //System.out.println(" ");
                }
                this.hasGuessed = true;
                // Reset letter counts
                for (int i = 0; i < 8; i++) {
                    for (int j = 0; j < 10; j++) {
                        this.tempOccurrences[i][this.guess[i][j]] = this.occurrences[i][this.guess[i][j]];
                    }
                }
                // End reset letter counts
            } else {
                for (int i = 0; i < 8; i++) {
                    int rand = random.nextInt(this.totals[i]);
                    int a = -1;
                    while (rand >= 0) {
                        a++;
                        rand -= this.occurrences[i][a];
                    }
                    boolean foundIn = false;
                    for (int j = 0; j < 10; j++) {
                        if (this.guess[i][j] == a) {
                            foundIn = true;
                            break;
                        }
                    }
                    if (!foundIn) {
                        int tar = random.nextInt(10);
                        this.guess[i][tar] = a;
                    }
                }
            }
            // End find random combination

            // Count occurrences
            int count = 0;
            boolean letterExists;
            boolean wordExists;
            for (int i = 0; i < 7647; i++) {
                wordExists = true;
                for (int j = 0; j < 8; j++) {
                    letterExists = false;
                    for (int k = 0; k < 10; k++) {
                        if (this.words[i][j] == this.guess[j][k]) {
                            letterExists = true;
                            break;
                        }
                    }
                    if (!letterExists) {
                        wordExists = false;
                        break;
                    }
                }
                if (wordExists) {
                    count++;
                }
            }
            //totalTotal += count;
            //System.out.println(count);
            // End count occurrences

            // Check if better
            if (count > best) {
                this.best = count;
                System.out.println();
                System.out.println(this.best);
                System.out.println();
                System.out.println(q);
                q = 0;
                for (int i = 0; i < 8; i++) {
                    for (int j = 0; j < 10; j++) {
                        this.bestGuess[i][j] = this.guess[i][j];
                        if (this.bestGuess[i][j] > 0) {
                            System.out.print((char) (this.bestGuess[i][j] + 96));
                        }
                        //System.out.print(" ");
                    }
                    System.out.println("");
                }
            }
            // End check if better

            // Reset guess
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 10; j++) {
                    this.guess[i][j] = this.bestGuess[i][j];
                }
            }
            // End reset guess

            q++;
            if (q > 200000) {
                System.out.println("Reseting");
                q = 0;
                hasGuessed = false;
            }
        }
        //System.out.println(this.best);
        //System.out.println(totalTotal);
    }

    public static void main(String[] args) {
        WordLock wordLock = new WordLock();
    }
}
