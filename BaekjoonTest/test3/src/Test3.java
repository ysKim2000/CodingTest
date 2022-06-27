import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 풀이는 같음, 입력 받는 방법에 따른 속도차이 있음(버퍼로 입력받는게 더 빠름)
public class Test3 {
    public static void main(String[] args) throws Exception {
        code();
    }

    public static void myCode() throws Exception {
        Scanner sc = new Scanner(System.in);
        int suNo = sc.nextInt();
        int quizNo = sc.nextInt();

        int arr[] = new int[suNo + 1];
        arr[0] = 0;
        for (int i = 1; i <= suNo; i++) {
            arr[i] = arr[i - 1] + sc.nextInt();
        }
        for (int i = 0; i < quizNo; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            System.out.println(arr[y] - arr[x - 1]);
        }
        sc.close();
    }

    public static void code() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼로 입력받음
        StringTokenizer st = new StringTokenizer(br.readLine()); // 문자열을 쪼개줌(토큰화)
        int suNo = Integer.parseInt(st.nextToken());
        int quizNo = Integer.parseInt(st.nextToken());

        int[] sum = new int[suNo + 1];
        sum[0] = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= suNo; i++) {
            sum[i] = sum[i - 1] + Integer.parseInt(st.nextToken());
        }

        for (int k = 0; k < quizNo; k++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            System.out.println(sum[j] - sum[i - 1]);
        }
    }
}
