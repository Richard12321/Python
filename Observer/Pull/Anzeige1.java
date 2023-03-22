package Observer.Pull;

public class Anzeige1 implements Ausgabe {
    private Wetterstation w;

    public Anzeige1(Wetterstation w){
        w.addAusgabe(this);
        this.w = w;
    }

    public void erhalteUpdate() {
        double Temperatur = w.getTemperatur();
        double Luftfeuchtigkeit = w.getLuftfeuchtigkeit();
        System.out.println("Neue Temperatur: " + Temperatur + ", Neue Luftfeuchtigkeit: " + Luftfeuchtigkeit + " an Anzeige 1!");
    }
}
