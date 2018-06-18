package sopaprimordial;

/**
 *
 * @author Douglas
 */

import java.net.*;
import sopaprimordial.Comunicacao;
 
public class Cliente {
    public static void main(String[] args) {
    try{
    Socket servidor = new Socket("localhost",50007);
    Comunicacao protocolo = new Comunicacao(servidor);
    protocolo.protocoloSaida("Abyssal Greater Basilisk");
    String teste = protocolo.protocoloEntrada();
    System.out.println(teste);
    servidor.close();
    }catch(Exception ex){
        ex.printStackTrace();
    }
    }
}

