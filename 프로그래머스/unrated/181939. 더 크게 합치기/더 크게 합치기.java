class Solution {
    public int solution(int a, int b) {
        int AB = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int BA = Integer.parseInt(Integer.toString(b) + Integer.toString(a));
        return Math.max(AB, BA);
    }
}