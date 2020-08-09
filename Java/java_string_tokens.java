import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().replace("[\\W]", " ").trim();
        String[] arr = s.split("[\\W]");//.trim();
        // arr.replaceAll("\\s+","");
        // String[] arr = s.split("[,\\s\\-:\\?']");
        // System.out.println(arr.getClass());
        /*
        for(int i = 0; i < arr.length; i++)
        {
            // if (StringUtils.isBlank(arr[i]))
            // if (arr[i].isBlank())
            // if (org.apache.commons.lang3.StringUtils.isBlank(arr[i]))
            if (arr[i] != "\\W")
            {
                System.out.println("wrks");
                arr[i] = arr[i].replace(arr[i],"");
            }
        }
        */
        System.out.println(arr.length);
        for ( String ss : arr)
        {
            System.out.println(ss);
        }


        scan.close();
    }
}


