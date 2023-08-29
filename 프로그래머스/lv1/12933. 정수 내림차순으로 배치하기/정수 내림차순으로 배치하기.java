import java.util.Arrays;
import java.util.Comparator;

class Solution {
        public long solution(long n) {
             String sortedNumberStr = Arrays.stream(String.valueOf(n).split(""))
            .sorted((a, b) -> b.compareTo(a))
            .reduce("", (acc, digit) -> acc + digit);
        
        return Long.parseLong(sortedNumberStr);
        }
    }