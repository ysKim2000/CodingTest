import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class Test11 {
    // 1부터 자연수를 증가시키면서 입력으로 주어진 숫자와 비교하여 증가시킨 자연수를 스택에 추가하거나 빼는 방식
    public static void main(String[] args) throws Exception {
        myCode();
        // code();
    }

    public static void myCode() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int[] stack = new int[num];
        StringBuilder result = new StringBuilder();

        int start = 0;
        int x = 0; // index 번호

        for (int i = 0; i < stack.length; i++) {
            int value = Integer.parseInt(br.readLine());
            if (value > start) {
                for (int j = start + 1; j <= value; j++) {
                    stack[x] = j;
                    x++;
                    result.append('+').append('\n');
                }
                start = value;
            } else if (stack[x - 1] != value) {
                System.out.println("NO");
                System.exit(0); // 이거 해야지 출력초과되지 않음
            }
            x--;
            result.append('-').append('\n');
        }
        System.out.println(result);
    }

    public static void code() throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        StringBuffer bf = new StringBuffer();
        int num = 1;
        boolean result = true;
        for (int i = 0; i < A.length; i++) {
            int su = A[i];
            if (su >= num) {
                while (su >= num) {
                    stack.push(num++);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            } else {
                int n = stack.pop();
                if (n > su) {
                    System.out.println("NO");
                    result = false;
                    break;
                } else {
                    bf.append("-\n");
                }
            }
        }
        if (result)
            System.out.println(bf.toString());
    }
}
