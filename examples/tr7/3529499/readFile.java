import java.io.*;


public class readFile{
  
  private String data;

/////////////////////////////////////////////////////
 
  public readFile(File filename){

    FileInputStream input;    
    byte buffer[] = new byte[(int)filename.length()];

    try{
      input = new FileInputStream(filename);    
      input.read(buffer);
    }
    catch(IOException e){
      System.out.println("File not found");
    }
    
    data = new String(buffer);        
  }

/////////////////////////////////////////////////////

  public int getNumberWords(String line){
    int count=0;
    
    char temp[] = line.toCharArray();

    for(int i=0 ; i < temp.length ; i++){
      if(temp[i] == ' ')
        count++;
    }
    count++;

    return count;
  }

/////////////////////////////////////////////////////

  public String getTags(String temp){
    int rightTags, errorTags, beginTag, endTag;
    rightTags = errorTags = 0;

    String tags="";
    char line[] = temp.toCharArray();

    int i=0;
    while(i < line.length){
      if(line[i] == '>')
        errorTags++;

      if(line[i] == '<'){
        beginTag = i;
        i++;         

        while(i < line.length){
          if(line[i] == '>'){
            endTag = i;
            for(int j=beginTag ; j <= endTag ; j++)
              tags += line[j];

            rightTags++;
            break;
          }
          else if(line[i] == ' ' || line[i] == '<' || line[i] == '\n'){
            errorTags++;            
            break;
          }
          i++;           
        }//fim do 2º while
        i++;
      }//fim do if
      
      i++;
    }//fim do 1º while

    String retorno = " " + rightTags + " tags validas " + tags + " - " + errorTags + " tags invalidas";
    return retorno;
  }

/////////////////////////////////////////////////////

  public void execute(){
      
    String line = "";
    int nline=1;
    char temp[] = data.toCharArray();

    for(int i=0 ; i < temp.length ; i++){      
      
      while((temp[i] != '\n') && ((temp.length-1) > i)){
        line += temp[i];       
        i++;
      }
     
      System.out.println("linha " + nline + " - " + getNumberWords(line) + " palavras -" + getTags(line));
      line = "";
      nline++;
    }
  }


/////////////////////////////////////////////////////

  public static void main(String[] args){
    readFile _read = new readFile(new File(args[0]));  
    _read.execute();
  }

}