import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // System.out.print(n);
        List<Integer> intList = new ArrayList<Integer>();
        // List<String> strList = new ArrayList<String>();

        for(int j = 0; j < n; j++)
        {
            intList.add(in.nextInt());
        }
        // System.out.print(intList[3]);

        // String arr_inp = in.nextLine();
        // String[] currencies = lineOfCurrencies.split(" ");
        // String inp = in.nextLine();
        // String[] arr_inp = in.nextLine().split(" ");
        // String[] arr_inp = inp.split(" ");

        int queries = in.nextInt();
        in.nextLine();

        for(int i = 0; i < queries; i++)
        {
            String command = in.nextLine();
            if(command.equals("Insert"))
            {
                int index = in.nextInt();
                int elem = in.nextInt();
                try 
                {
                    in.nextLine();
                } 
                catch (Exception e) { 
                    // System.out.println("Exception thrown: " + e); 
                }
                intList.add(index, elem);
            }
            else if (command.equals("Delete"))
            {
                int index = in.nextInt();
                try 
                {
                    in.nextLine();
                } 
                catch (Exception e) { 
                    // System.out.println("Exception thrown: " + e); 
                } 
                
                intList.remove(index);
            }
        }
        for(int integ: intList)
        {
            System.out.print(integ + " ");
            // System.out.println(' ');
        }
        
    }
}

