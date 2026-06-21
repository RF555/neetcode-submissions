class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        if(s.length() == 1 && t.length() == 1){
            return s.charAt(0) == t.charAt(0);
        }
        
        Map<Character, Integer> charMap = new HashMap<>();
        for ( int i=0; i < s.length(); i++){
            if (charMap.containsKey(s.charAt(i))){
                charMap.put(s.charAt(i), charMap.get(s.charAt(i))+1);
            } else {
                charMap.put(s.charAt(i), 1);
            }
        }

        for (int i=0; i<t.length(); i++){
            if( !charMap.containsKey(t.charAt(i)) || charMap.get(t.charAt(i)) <= 0){
                return false;
            } else {
                charMap.put(t.charAt(i), charMap.get(t.charAt(i))-1);
            }
        }

        for (Integer a: charMap.values()){
            if(a > 0){
                return false;
            }
        }

        return true;
    }

}
