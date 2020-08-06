import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        int i = 0;

        while(i < s.length() - k + 1)
        {
            smallest = s.substring(i, i + k).compareTo(smallest) < 0 ? s.substring(i, i + k) : smallest;
            largest = s.substring(i, i + k).compareTo(largest) > 0 ? s.substring(i, i + k) : largest;
            i++;
        }
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}
