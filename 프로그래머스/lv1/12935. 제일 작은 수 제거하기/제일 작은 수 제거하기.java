import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int[] answer;
        int min = arr[0];
        int min_index = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
                min_index = i;
            }
        }
        
        // 새로운 배열 생성하여 값을 복사
        ArrayList<Integer> resultList = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (i != min_index) {
                resultList.add(arr[i]);
            }
        }
        
        // 새로운 배열을 기존 배열로 변환
        if (resultList.isEmpty()) {
            answer = new int[]{-1};
        } else {
            answer = new int[resultList.size()];
            for (int i = 0; i < resultList.size(); i++) {
                answer[i] = resultList.get(i);
            }
        }
        
        return answer;
    }
}
