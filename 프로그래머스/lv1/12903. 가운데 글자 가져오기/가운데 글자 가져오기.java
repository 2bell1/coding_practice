class Solution {
    public String solution(String s) {
         String answer = "";
        int index = s.length() / 2;
        if (s.length() % 2 == 0)
            answer = String.valueOf(s.charAt(index - 1)) + String.valueOf(s.charAt(index));
        else
            answer = String.valueOf(s.charAt(index));
        return answer;
    }
}