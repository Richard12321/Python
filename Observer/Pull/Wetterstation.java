package Observer.Pull;

import java.util.ArrayList;

public abstract class Wetterstation {
    private ArrayList<Ausgabe> ausgabenListe = new ArrayList<Ausgabe>(); 

    public void addAusgabe(Ausgabe a){
        ausgabenListe.add(a);
    }

    public void deleteAusgabe(Ausgabe a){
        ausgabenListe.remove(a);
    }

    public void ausgabenBenachrichtigen(){
        for(Ausgabe a : ausgabenListe){
            a.erhalteUpdate();
        }
    }
    public abstract double getTemperatur();
    public abstract double getLuftfeuchtigkeit();
    public abstract void setStatus(double Temperatur, double Luftfeuchtigkeit);
}
