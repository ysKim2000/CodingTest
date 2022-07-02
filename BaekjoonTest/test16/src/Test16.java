import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

// 4단계 학습
public class App {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        mData[] arr = new mData[n]; 

        for (int i = 0; i < n; i++) {
            arr[i] = new mData(); // index와 value
            arr[i].value = Integer.parseInt(br.readLine());
            arr[i].index = i;
        }
        Arrays.sort(arr);

        int max = 0;
        for (int i = 0; i < n; i++) {
            if (max < arr[i].index - i)
                max = arr[i].index - i;
        }
        System.out.println(max + 1);
    }
}

class mData implements Comparable<mData> {
    int value;
    int index;

    @Override
    public int compareTo(mData o) {
        return this.value - o.value;
    }
}