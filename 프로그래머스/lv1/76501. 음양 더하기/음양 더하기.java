class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int i =0;
        for(int a : absolutes)
        {
            answer += (a * (signs[i] ? 1 : -1));
            i++;
        }
        return answer;
    }
}