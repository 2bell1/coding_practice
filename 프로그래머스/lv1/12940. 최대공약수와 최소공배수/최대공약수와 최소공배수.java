class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        // 최대공약수 계산
        int gcd = calculateGCD(n, m);
        
        // 최소공배수 계산
        int lcm = (n * m) / gcd;
        
        // 결과 배열에 저장
        answer[0] = gcd;
        answer[1] = lcm;
        
        return answer;
    }
    
    // 최대공약수를 계산하는 함수
    private int calculateGCD(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return calculateGCD(b, a % b);
        }
    }
}
