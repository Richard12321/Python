package PizzaStore;
import Pizza.Pizza;
import Pizza.Rostock.*;;

public class PizzaStoreRostock extends PizzaStore{

    @Override
    Pizza createPizza(String type) {
        switch(type){
            case "Salami": return new PizzaSalamiRostock();
            case "Calzone": return new PizzaCalzoneRostock();
            case "Hawaii": return new PizzaHawaiiRostock();
            case "QuattroStagioni": return new PizzaQuattroStagioniRostock();
        }
        return null;
    }

}
