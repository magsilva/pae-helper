import java.io.*;
import java.lang.*;

public class Exercicio
{
  public static void main(String[] Args)
  {
    Texto a;
    String param="";
    DataInputStream frase = new DataInputStream(System.in);
    
    try
    {
      param = frase.readLine();
    }
    
    catch (Exception erro)
    {
      System.out.println("Erro de leitura");
    }	

    a = new Texto(param);
  }
}

class Texto
{
  public int num_tags_abertas = 0;
  public int num_palavras = 0;
  public int num_linhas = 1;
  public int num_tags_validas = 0;
  public int num_tags_invalidas = 0;

  public Texto(String frase)
  {
    Palavra word;
    String[] palavras;
    palavras = frase.split(" ");

    for (int i = 0; i < palavras.length; i++)
    {
      /* instancia nova palavra */
      word = new Palavra(palavras[i]);

      /* atualiza os devidos contadores */
    
      /*System.out.println(word.pal.compareTo("\n"));*/
      if (word.pal.compareTo("\n") == 0)
      {
        System.out.println("Linha " + num_linhas + " - " + num_palavras + " palavras - " + num_tags_validas + " tags validas - " + num_tags_invalidas + " tags invalidas."); 

        num_palavras = 0;
        num_linhas += 1;
        num_tags_validas = 0;
        num_tags_invalidas = 0;
        num_tags_abertas = 0;
      }

      num_palavras += 1;
      num_tags_abertas += word.Verifica_tags();
      num_tags_validas += word.tags_validas;
      num_tags_invalidas += word.tags_invalidas;
    }

    System.out.println("Linha " + num_linhas + " - " + num_palavras + " palavras - " + num_tags_validas + " tags validas - " + num_tags_invalidas + " tags invalidas."); 

  }
}

class Palavra
{
  String pal;
  int tags_validas;
  int tags_invalidas;

  public Palavra(String word)
  {
    pal = word;  
    tags_validas = 0;
    tags_invalidas = 0;
  }

  protected int Verifica_tags()
  {
    int pos_abre_tag = pal.indexOf("<");
    int pos_fecha_tag = pal.indexOf(">");
    int tags_abertas = 0;
    boolean existe_tag;

    existe_tag = (pos_abre_tag != -1);

    while (pos_abre_tag != -1)
    {
      tags_abertas++;
      pal = pal.replaceFirst("<", "|");
      pos_abre_tag = pal.indexOf("<");
    }

    while (pos_fecha_tag != -1)
    {
      tags_abertas--;
      pal = pal.replaceFirst(">", "^");
      pos_fecha_tag = pal.indexOf(">");
    }
 
    if (existe_tag)
      if (tags_abertas == 0) /* tag valida */
        tags_validas += 1; 
      else
        tags_invalidas += 1; 

    return tags_abertas;

  }
}
