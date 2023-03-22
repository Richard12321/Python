package Observer.Pull;

public class WetterstationInnnsbruck extends Wetterstation {
    private double Temperatur;
    private double Luftfeuchtigkeit;

    public void setStatus(double Temperatur, double Luftfeuchtigkeit){
        this.Temperatur = Temperatur;
        this.Luftfeuchtigkeit = Luftfeuchtigkeit;
        super.ausgabenBenachrichtigen();
    }

    public double getTemperatur(){
        return this.Temperatur;
    }
    public double getLuftfeuchtigkeit(){
        return this.Luftfeuchtigkeit;
    }
}
