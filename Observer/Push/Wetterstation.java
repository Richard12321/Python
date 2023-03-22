package Observer.Push;

import java.util.ArrayList;

public class Wetterstation {
    private ArrayList<Ausgabe> ausgabenListe = new ArrayList<Ausgabe>(); 

    public void addAusgabe(Ausgabe a){
        ausgabenListe.add(a);
    }

    public void deleteAusgabe(Ausgabe a){
        ausgabenListe.remove(a);
    }

    public void ausgabenBenachrichtigen(double Temperatur, double Luftfeuchtigkeit){
        for(Ausgabe a : ausgabenListe){
            a.erhalteUpdate(Temperatur, Luftfeuchtigkeit);
        }
    }
}
