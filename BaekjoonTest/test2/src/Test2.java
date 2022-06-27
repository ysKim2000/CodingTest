import java.util.*;

public class Test2 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int score[] = new int[num];
        int sum = 0, max = 0;

        for(int i=0; i<num;i++){
            score[i] = sc.nextInt();
            if(score[i] > max) max = score[i];
            sum += score[i];
        }
        System.out.println(sum * 100.0 / max / num);
        sc.close();
    }
}
