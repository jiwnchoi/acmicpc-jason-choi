import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int exp = 64;
        int count = 0;

        while (x != 0){
            if(exp > x){
                exp = exp / 2;
            }

            else{
                x -= exp;
                count ++;
            }

        }

        System.out.println(count);


    }
}
0