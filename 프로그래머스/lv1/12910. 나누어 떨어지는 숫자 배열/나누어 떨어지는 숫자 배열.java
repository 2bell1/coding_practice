import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for(int a : arr)
        {
            if(a % divisor == 0)
                answer.add(a);
        }
        if(answer.isEmpty() )
        {
            return new int[]{-1};
        }
        Collections.sort(answer);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}