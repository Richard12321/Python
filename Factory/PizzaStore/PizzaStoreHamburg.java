package PizzaStore;
import Pizza.Pizza;
import Pizza.Hamburg.*;;

public class PizzaStoreHamburg extends PizzaStore{

    @Override
    Pizza createPizza(String type) {
        switch(type){
            case "Salami": return new PizzaSalamiHamburg();
            case "Calzone": return new PizzaCalzoneHamburg();
            case "Hawaii": return new PizzaHawaiiHamburg();
            case "QuattroStagioni": return new PizzaQuattroStagioniHamburg();
        }
        return null;
    }

}
