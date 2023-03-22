package Observer.Pull;

public class Controller {
    public static void main(String[] args) {
        Wetterstation w = new WetterstationInnnsbruck();

        Anzeige1 a1 = new Anzeige1(w);
        Anzeige2 a2 = new Anzeige2(w);

        w.setStatus(10,50);
    }
}
