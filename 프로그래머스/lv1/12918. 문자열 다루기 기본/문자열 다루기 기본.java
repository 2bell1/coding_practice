class Solution {
    public boolean solution(String s) {
        boolean answer = false;
        if(s.length() == 4 || s.length() == 6)
        {
            try {
            int number = Integer.parseInt(s);
            answer = true;
        } catch (NumberFormatException e) {
            answer = false;
        }
        }
        return answer;
    }
}