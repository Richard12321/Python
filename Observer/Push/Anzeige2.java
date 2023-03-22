package Observer.Push;

public class Anzeige2 implements Ausgabe{
    public Anzeige2(Wetterstation w){
        w.addAusgabe(this);
    }
    public void erhalteUpdate(double Temperatur, double Luftfeuchtigkeit) {
        System.out.println("Neue Temperatur: " + Temperatur + ", Neue Luftfeuchtigkeit: " + Luftfeuchtigkeit + " an Anzeige 2!");
    }   
}
