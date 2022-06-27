import java.util.*;

public class Test1 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        String sNum = sc.next();
        int sum = 0;

        for (int i = 0; i < num; i++) {
            sum += sNum.charAt(i) - '0';
        }
        System.out.println(sum);
        sc.close();
    }
}
