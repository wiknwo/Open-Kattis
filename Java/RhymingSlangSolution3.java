/**
 * Medium
 * 
 * This is the correct solution.
 * 
 * Hypothesis: I think the other solutions were incorrect because they
 * didn't account for the case where more than one word in the phrase
 * or a word that is not the last word in the phrase has an ending
 * in the list of word endings.
 */
import java.util.Scanner;

public class RhymingSlangSolution3
{
	public static void main(String[] args) 
	{
		//Typically, two words rhyme (or can be forced to rhyme) if both of their endings can be found on the same list of word endings.**
		//All words and letters will be in lower case. The common word's ending will appear in at least one ending list.

		String S = ""; //common word.
		int E = 0; //One line containing an integer E (1 <= E <= 10), the number of lists of word endings that sound the same.
		int P = 0; //One line containing an integer P (1 <= P <= 10), the number of phrases to test.
		int i, j; //Array indices
		Scanner sc = new Scanner(System.in);
		boolean phrase_rhymes_with_S;
		
		S = sc.nextLine();
		E = Integer.parseInt(sc.nextLine());
		String[][] wordEndings = new String[E][];
		
		//Placing lists of word endings into multidimensional array.
		for(i = 0;i < E;i++)
		{
			wordEndings[i] = sc.nextLine().split(" ");
		}
		
		P = Integer.parseInt(sc.nextLine());
		String[] phrases = new String[P];
		
		//Placing each phrase into array.
		for(i = 0;i < P;i++)
		{
			phrases[i] = sc.nextLine();
		}
		
		sc.close();
		
		//Does it rhyme?
		for(i = 0;i < phrases.length;i++)
		{
			phrase_rhymes_with_S = false;
			
			for(j = 0;j < wordEndings.length;j++)
			{
				if((wordEndingIsInList(phrases[i], wordEndings[j])) && wordEndingIsInList(S, wordEndings[j]))
				{
					phrase_rhymes_with_S = true;
					break;
				}
			}
			
			System.out.println(phrase_rhymes_with_S ? "YES" : "NO");
		}
	}
	
	
	/**
	 * This method checks if word contains any of the 
	 * word endings in the list of word endings.
	 * 
	 * @param word
	 * @param list
	 * @return true || false
	 */
	public static boolean wordEndingIsInList(String word, String[] list)
	{
		for(String ending : list)
		{
			if(word.endsWith(ending))
			{
				return true;
			}
		}
		
		return false;
	}
}