public class Asn_17 {
    public static void main(String[] args) {
        try {
            String inputString = "Hello, World!";
            checkForVowels(inputString);
            System.out.println("The input string '"+inputString+"' contains vowels.");
        } catch (NoVowelsException e) {
            System.out.println("NoVowelsException: " + e.getMessage());
        }
    }
    static void checkForVowels(String input) throws NoVowelsException {
        boolean containsVowels = false;
        for (char ch : input.toCharArray()) {
            if (isVowel(ch)) {
                containsVowels = true;
                break;
            }
        }
        if (!containsVowels) {
            throw new NoVowelsException("The input string does not contain any vowels.");
        }
    }
    static boolean isVowel(char ch) {
        ch = Character.toLowerCase(ch);
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
}
class NoVowelsException extends Exception {
    public NoVowelsException(String message) {
        super(message);
    }
}
