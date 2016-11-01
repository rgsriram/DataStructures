/**
 * Created by sriram on 24/7/16.
 */

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class LinearSearch {
    public int search(int array[], int element) {
        int index = -1;

        for (int i=0; i<array.length; i++){
            if (element == array[i]) {
                index = i;
            }
        }
        return index;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String range = br.readLine();
//        int N = Integer.parseInt(line);
//        for (int i = 0; i < N; i++) {
//            System.out.println(line);
//        }
        String numbers = br.readLine();
        String element = br.readLine();


    }

}

