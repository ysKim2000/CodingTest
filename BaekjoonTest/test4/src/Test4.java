import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Test4 {
    public static void main(String[] args) throws Exception {
        myCode();
    }

    public static void myCode() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼로 입력받음
        StringTokenizer st = new StringTokenizer(br.readLine()); // 문자열을 쪼개줌(토큰화)
        int N = Integer.parseInt(st.nextToken()); // 2차원 배열의 크기
        int M = Integer.parseInt(st.nextToken()); // 구간합 질의의 개수
        StringBuilder sb = new StringBuilder();

        int arr[][] = new int[N + 1][N + 1]; // 2차원 배열
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine()); // 한 줄씩 입력받음
            for (int j = 1; j <= N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken()); // input
            }
        }

        int result[][] = new int[N + 1][N + 1]; // 2차원 구간합 배열
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                result[i][j] = result[i][j - 1] + result[i - 1][j] - result[i - 1][j - 1] +
                        arr[i][j];
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            // (a, b) ~ (c, d)까지의 구간합
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            sb.append(result[c][d] - result[a - 1][d] - result[c][b - 1] + result[a - 1][b - 1]);
            sb.append('\n');
        }
        System.out.println(sb);
    }
}
