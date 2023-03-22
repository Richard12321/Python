package Observer.Push;

public class WetterstationInnnsbruck extends Wetterstation {
    private double Temperatur;
    private double Luftfeuchtigkeit;

    public void setStatus(double Temperatur, double Luftfeuchtigkeit){
        this.Temperatur = Temperatur;
        this.Luftfeuchtigkeit = Luftfeuchtigkeit;
        super.ausgabenBenachrichtigen(Temperatur, Luftfeuchtigkeit);
    }
}
