import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static int pibo(int[]arr, int n){
        arr[n] = pibo(arr,n-1) + pibo(arr,n-2);
        return 0;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[42];
        arr[0] = 0;
        arr[1] = 1;
        int n = Integer.parseInt(bf.readLine());
        for (int i = 0; i<n; i++){
            int tmp =Integer.parseInt(bf.readLine());
            if (tmp == 0){
                System.out.println(arr[tmp-1]+" "+arr[tmp]);
            }
            else if (arr[tmp] == 0){
                pibo(arr,tmp);
                System.out.println(arr[tmp-1]+" "+arr[tmp]);
            }
            else{
                System.out.println(arr[tmp-1]+" "+arr[tmp]);
            }

        }
    }
}