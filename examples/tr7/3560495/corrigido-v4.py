// Exercicio 1.1 - Java
// Marco Aurelio Rescia Alher - 3560481
// Santiago de Moura Luz - 3560495

import java.util.*;
import java.io.*;

# ERRO 0 1 100

# ERRO 1 1 50
# ERRO 1 4 25
# ERRO 1 5 100


# ERRO 2 1 100
# ERRO 2 2 100
# ERRO 2 3 100
# ERRO 2 4 100
# ERRO 2 5 100
# ERRO 2 6 100
# ERRO 2 7 100
# ERRO 2 8 100
# ERRO 2 9 100
# ERRO 2 10 100

# ERRO 3 1 100
# ERRO 3 2 100

public class Tags {

	public static void main ( String args[] ) {
		int contpal = 0;
		int conttag = 0;
		int conttaginv = 0;
		String texto = "lendo <tags> falsas> e <tb <tags> <verdadeiras>";
		StringBuffer validas = new StringBuffer();
		String[] palavras = texto.split("\\s");			//***coloca cada palavra num array de strings
			for (int x = 0; x < palavras.length; x++) {	//***confere palavra a palavra
				if ((palavras[x].charAt(0) == '<')
					&& (palavras[x].charAt(palavras[x].length() - 1) == '>')) {
											//***se a palavra x comeca com '<'
											//   e termina com '>'
					validas.append(palavras[x]);		//   adiciona a tag num StringBuffer
					conttag++;					//   incrementa o contador de tags
					}
				if (((palavras[x].charAt(0) == '<')
				    && (palavras[x].charAt(palavras[x].length() - 1) != '>')) ||
				    ((palavras[x].charAt(0) != '<')
				    && (palavras[x].charAt(palavras[x].length() - 1) == '>')))
											//***se a tag eh invalida
					conttaginv++;				//   incrementa o contador de tags invalidas
				contpal++;						//***conta o numero de palavras
			}	
		System.out.print(contpal);					//***imprime os dados
		System.out.print(" palavras - ");
		System.out.print(conttag);
		System.out.print(" tags validas (");
		System.out.print(validas.toString());
		System.out.print(") - ");
		System.out.print(conttaginv);
		System.out.println(" tags invalidas");
	}
}
