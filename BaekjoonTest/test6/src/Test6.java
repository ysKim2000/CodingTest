import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Test6 {
    public static void main(String[] args) throws Exception {
        myCode();
    }
    public static void myCode() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 버퍼로 입력받음
        StringTokenizer st = new StringTokenizer(br.readLine()); // 문자열을 쪼개줌(토큰화)
        int N = Integer.parseInt(st.nextToken()); // 2차원 배열의 크기
        int result = 1; // 가짓수

        for (int i = 1; i < N - 1; i++) { // 앞 수
            int sum = i;
            for (int j = i + 1; i < N; j++) { // 뒷 수
                if (sum == N) {
                    result++;
                    break;
                } else if (sum > N) { // 종료
                    break;
                }
                sum += j;
            }
        }
        System.out.println(result);
    }
    
}
