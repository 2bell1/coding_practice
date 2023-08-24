class Solution {
    boolean solution(String s) {
        boolean answer = true;

        
        long p = s.chars().filter(c -> c == 'p' || c == 'P').count();
        long y = s.chars().filter(c -> c == 'y' || c == 'Y').count();
        
        if(p == y)
            answer= true;
        else
            answer =false;
        return answer;
    }
}