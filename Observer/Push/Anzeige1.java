package Observer.Push;

public class Anzeige1 implements Ausgabe {
    public Anzeige1(Wetterstation w){
        w.addAusgabe(this);
    }

    public void erhalteUpdate(double Temperatur, double Luftfeuchtigkeit) {
        System.out.println("Neue Temperatur: " + Temperatur + ", Neue Luftfeuchtigkeit: " + Luftfeuchtigkeit + " an Anzeige 1!");
    }
}
