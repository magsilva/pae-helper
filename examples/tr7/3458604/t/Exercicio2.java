import java.io.*;
import java.lang.*;
import java.util.*;

public class Exercicio2
{
  public static void main(String[] Args)
  {
    ConjuntoInteiros a;

    /* Instancia e testa o novo conjunto */

    a = new ConjuntoInteiros("1 2 3 3 4");

    a.Adicao(8);

    a.Remocao(2);

    a.Mostra();
 
  }
}

class ConjuntoInteiros
{
  int[] numeros;
  int[] num_string;
  
  /* Construtor da classe */ 
  public ConjuntoInteiros(String param)
  {
    int i, tamanho, j = 0;

    /* Converte o parametro recebido para uma lista de inteiros */
    ConvertToInt(param);
    tamanho = num_string.length;

    /* Instanciacao da lista com tamanho da lista de parametros recebida */
    numeros = new int[tamanho];

    /* Verifica se numero nao eh repetido e, caso nao for, insere-o na lista */
    for (i = 0; i < tamanho; i++)
      if (!ExisteNumero(num_string[i], tamanho))
      {
        numeros[j] = num_string[i];
        j++;
      }

  }

  /* Verifica se o numero ja existe na lista*/
  protected boolean ExisteNumero(int num, int tamanho)
  {
    boolean result = false;
    int i;

    for (i = 0; i < tamanho; i++)
      if (numeros[i] == num)
        result = true;

    return result;
  }
  
  /* Converte os parametros de string para uma lista de inteiros */
  protected void ConvertToInt(String param)
  {
    String[] separado;
    Double aux;
    int i, tamanho;

    separado = param.split(" ");
    tamanho = separado.length;
    num_string = new int[tamanho];

    for (i = 0; i < tamanho; i++)
    {
      /* Testa se o tipo eh valido, atraves do tratamento de excecoes */
      try
      {
        aux = Double.valueOf(separado[i]);
        num_string[i] = aux.intValue();
      }
      catch (Exception erro)
      {
        System.out.println("Tipo invalido de dados");  
      }
    }
  }

  /* Remove um item da lista, caso ele exista */
  protected void Remocao(int param)
  {
    int i, ind_remocao = -1, tamanho = numeros.length;
  	
    for (i = 0; i < tamanho; i++)
      if (numeros[i] == param)
        ind_remocao = i;
  	    
    if (ind_remocao != -1)
      numeros[ind_remocao] = -999;
  	  
  }

  /* Adiciona um item na lista, caso ele nao exista */
  protected void Adicao(int param)
  {
    int i, tamanho, ind_adicao = -1;
    int[] velho;
    boolean existe = false;

    tamanho = numeros.length;

    /* Testa se o numeros nao eh repetido */
    for (i = 0; i < tamanho; i++)
      if (numeros[i] == param)
        existe = true;

    if (!existe)
    {
      velho = new int[tamanho];

      /* Joga o conteudo antigo para posteriror rearmazenamento */
      for (i = 0; i < tamanho; i++)
        velho[i] = numeros[i];

      /* Seta novo tamanho*/
      numeros = new int[tamanho+1];

      for (i = 0; i < tamanho; i++)
        numeros[i] = velho[i];

      numeros[tamanho] = param;
    }           
  }

  /* Mostra os items da classe na tela */
  protected void Mostra()
  {
    int i, tamanho = numeros.length;

    for (i = 0; i < tamanho; i++)
      if (numeros[i] != -999)
        System.out.println(numeros[i]);
  }


}