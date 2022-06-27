import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 주몽 문제(pseudo-code 참고함)
public class Test7 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 재료의 개수
        int M = Integer.parseInt(br.readLine()); // 갑옷이 완성되는 번호의 합
        int A[] = new int[N];
        int result = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        int i = 0; // start
        int j = N - 1; // end
        while (i < j) {
            if (A[i] + A[j] < M) {
                i++;
            } else if (A[i] + A[j] > M) {
                j--;
            } else {
                result++;
                i++;
                j--;
            }
        }
        System.out.println(result);
    }
}
