import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 수의 개수
        int A[] = new int[N];
        int result = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);
        for (int i = 0; i < N; i++) {
            int start = 0;
            int end = N - 1;
            int k = A[i];
            while (start < end) {
                if (A[start] + A[end] == k) {
                    if (start != i && end != i) {
                        result++;
                        break;
                    } else if (start == i) {
                        start++;
                    } else {
                        end--;
                    }
                } else if (A[start] + A[end] < k) {
                    start++;
                } else {
                    end--;
                }
            }
        }
        System.out.println(result);
    }
}
