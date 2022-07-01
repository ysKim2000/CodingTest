import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] numArray = new int[Integer.parseInt(br.readLine())];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < numArray.length; i++) {
            numArray[i] = Integer.parseInt(st.nextToken());
        }
        // 후입선출의 기능을 갖는 자료구조 스택 선언
        Stack<Integer> stack = new Stack<>();

        // numArray의 길이만큼 반복문 수행
        for (int i = 0; i < numArray.length; i++) {
            for (int j = i + 1; j < numArray.length; j++) {
                if (numArray[i] < numArray[j]) {
                    stack.push(numArray[j]);
                }
            }
            if (!stack.isEmpty()) {
                while (stack.size() != 1) {
                    stack.pop();
                }
                numArray[i] = stack.pop();
            } else {
                numArray[i] = -1;
            }
        }
        numArray[numArray.length - 1] = -1;
        for (int i = 0; i < numArray.length; i++) {
            System.out.print(numArray[i] + " ");
        }
    }
}
