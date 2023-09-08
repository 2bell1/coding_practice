class Solution {
    public int solution(int[] numbers) {
        int answer;
        answer = 45;
        for(int a : numbers)
        {
            answer -= a;
        }
        return answer;
    }
}