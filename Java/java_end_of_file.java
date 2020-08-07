import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // String[] lines;

        List<String> lis = new ArrayList<>();

        int i = 0;
        while (input.hasNextLine())
        {
            // lines[i] = input.nextLine();
            lis.add(String.valueOf(i + 1) + " " + input.nextLine());
            // System.out.println(line);
            i++;
        }
        for (String z : lis) 
        {
            System.out.println(z);
        }
        // for(int j = 0; i < lines.length; j++)
        // {
        //     System.out.println(String.valueOf(j + 1) + lines[j]);
        // }
    }
}

