class Solution {
    public String solution(String[] arr) {
        String answer = arr.toString();
        StringBuilder sb = new StringBuilder();

  for (String ch : arr) {
    sb.append(ch);
  }

  answer = sb.toString();
        return answer;
    }
}