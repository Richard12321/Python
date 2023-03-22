package Observer.Pull;

public class Anzeige2 implements Ausgabe{
    private Wetterstation w;

    public Anzeige2(Wetterstation w){
        w.addAusgabe(this);
        this.w = w;
    }

    public void erhalteUpdate() {
        double Temperatur = w.getTemperatur();
        double Luftfeuchtigkeit = w.getLuftfeuchtigkeit();
        System.out.println("Neue Temperatur: " + Temperatur + ", Neue Luftfeuchtigkeit: " + Luftfeuchtigkeit + " an Anzeige 2!");
    }
}
