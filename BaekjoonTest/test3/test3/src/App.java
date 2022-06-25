import java.util.*;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int suNo = sc.nextInt();
        int quizNo = sc.nextInt();

        int[] arr = new int[suNo + 1];
        arr[0]=0;

        for (int i = 1; i <= suNo; i++) {
            arr[i] = arr[i - 1] + sc.nextInt();
        }
        for(int i =0; i< quizNo; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            System.out.println(arr[y] - arr[x - 1]);
        }

        sc.close();
    }
}
