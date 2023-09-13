import java.util.Arrays;
import java.util.Collections; 
class Solution {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr); // 문자 배열을 오름차순으로 정렬

        // 정렬된 문자 배열을 역순으로 만들어서 문자열로 변환
        StringBuilder sb = new StringBuilder(new String(arr));
        sb.reverse();

        String answer = sb.toString(); // StringBuilder를 String으로 변환

        return answer;
    }
}