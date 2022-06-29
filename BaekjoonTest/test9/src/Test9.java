import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Test9 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int P = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        char[] DNA = br.readLine().toCharArray();
        int[] count = new int[4];

        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int g = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        int start = 0;
        int end = 0;
        int sum = 0;
        int result = 0;

        while (end < P) {
            if (sum < S) {
                sum++;
                if (DNA[end] == 'A')
                    count[0]++;
                else if (DNA[end] == 'C')
                    count[1]++;
                else if (DNA[end] == 'G')
                    count[2]++;
                else if (DNA[end] == 'T')
                    count[3]++;
                end++;
            }
            if (sum == S) {
                if (count[0] >= a && count[1] >= c && count[2] >= g && count[3] >= t)
                    result++;
                sum--;
                if (DNA[start] == 'A')
                    count[0]--;
                else if (DNA[start] == 'C')
                    count[1]--;
                else if (DNA[start] == 'G')
                    count[2]--;
                else if (DNA[start] == 'T')
                    count[3]--;
                start++;
            }
        }

        System.out.println(result);
    }

}
