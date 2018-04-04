package sopaprimordial;

import java.util.Random;
import java.util.Scanner;

/**
 *
 * @author ci
 */
public class SopaPrimordial {


 public static void pulaLinha(){
     System.out.println("\n");
 }
    
 public static void main(String[] args) {
        /*
        Primeiro vamos fazer como se fosse tudo no prompt normal
        */
        String monstro_informacoes, dados_vida, dados_ataque[];
        dados_ataque = new String[50];
        int vida;
        short ataques = 0;
        Random gerador = new Random();
        
        vida = 0;
        Scanner leitor = new Scanner(System.in);
        System.out.println("Tipo do monstro:");
        monstro_informacoes = leitor.nextLine();
        pulaLinha();
        
        System.out.println("Tamanho do monstro:");
        monstro_informacoes += " " + leitor.nextLine();
        pulaLinha();
        
        System.out.println("Dados de vida:");
        dados_vida = leitor.nextLine();
        monstro_informacoes += " " + dados_vida;
        pulaLinha();
        
        /*String aux[] = dados_vida.split("d");
        for(int i = 0; i < Integer.parseInt(aux[0]); i++){
            vida += gerador.nextInt(Integer.parseInt(aux[1]));
        }
        System.out.println("Bonus de vida(Caso não haja, coloque '0'):");
        vida += leitor.nextInt();
        monstro_informacoes += " " + vida;*/
        System.out.println("Iniciativa:");
        monstro_informacoes += " " + leitor.nextLine();
        pulaLinha();
        
        System.out.println("Deslocamento em Terra/Ar/Agua em metros:");
        monstro_informacoes += " " + leitor.nextLine();
        pulaLinha();
        
        System.out.println("Classe de Armadura:");
        monstro_informacoes += " " + leitor.nextLine();
        pulaLinha();
        
        System.out.println("Ataque Base/Agarrar:");
        monstro_informacoes += " " + leitor.nextLine();
        pulaLinha();
        
        monstro_informacoes += " ";
        for(int i = 0; i < dados_ataque.length; i++){
            //Primeiro gravamos o ataque padrão do monstro
            System.out.println("Dados de ataque:");
            dados_ataque[i] = leitor.nextLine();
            monstro_informacoes += dados_ataque[i];
        
            System.out.println("Possui mais algum ataque?(s/n)");
            if(leitor.nextLine().equals("n")) break;
            
            //Mais um ataque foi adicionado
            monstro_informacoes += "/";
            ataques++;
        }
        System.out.println(monstro_informacoes);
        pulaLinha();
        
        
                
        pulaLinha();
    }
    
}
