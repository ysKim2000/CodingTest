import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.StringTokenizer;

// 4단계 학습. 덱을 처음 경험...
public class Test10 {
    public static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Deque<Node> deque = new LinkedList<>(); // 연결 리스트
        for (int i = 0; i<n; i++) {
            int temp = Integer.parseInt(st.nextToken());
            // 새로 들어올 값보다 더 큰 값이 있다면 제거
            while(!deque.isEmpty() && deque.getLast().value > temp) {
                deque.removeLast(); // 덱의 마지막 값 제거
            }
            deque.addLast(new Node(temp, i));
            // 범위에서 벗어난 값을 덱에서 제거
            if (deque.getFirst().index <= i -l) {
                deque.removeFirst(); // 덱의 첫 요소 값 삭제
            }
            bw.write(deque.getFirst().value + " "); // 덱의 앞쪽 엘리먼트 하나를 제거하지 않은채 리턴
        }
        bw.flush();
        bw.close();
    }

    static class Node {
        public int value;
        public int index;

        Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}