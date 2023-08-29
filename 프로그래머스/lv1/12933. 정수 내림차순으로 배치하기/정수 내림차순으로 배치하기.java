import java.util.Arrays;
import java.util.Comparator;

class Solution {
        public long solution(long n) {
            //String[] digitsStr = String.valueOf(n).split("");
            //Arrays.sort(digitsStr, Comparator.reverseOrder());
            //String sortedNumberStr = String.join("", digitsStr);
            //long answer = Long.parseLong(sortedNumberStr);
            //return answer;
            
            // 람다식
            
             String sortedNumberStr = Arrays.stream(String.valueOf(n).split(""))
            .sorted((a, b) -> b.compareTo(a))
            .reduce("", (acc, digit) -> acc + digit);
        
        return Long.parseLong(sortedNumberStr);
        }
    }
