import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Test5 {
    // 나머지 합 구하기
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 수 개수
        int M = Integer.parseInt(st.nextToken()); // 나누는 수
        long sum = 0;
        long S[] = new long[M];
        long result = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < N + 1; i++) {
            sum += Integer.parseInt(st.nextToken());
            sum %= M;
            S[(int) sum]++;
        }

        result += S[0];
        for (int i = 0; i < M; i++) {
            result += (S[i] * (S[i] - 1)) / 2;
        }
        System.out.println(result);
    }
}