package PizzaStore;
import Pizza.Berlin.*;
import Pizza.Pizza;

public class PizzaStoreBerlin extends PizzaStore{

    @Override
    Pizza createPizza(String type) {
        switch(type){
            case "Salami": return new PizzaSalamiBerlin();
            case "Calzone": return new PizzaCalzoneBerlin();
            case "Hawaii": return new PizzaHawaiiBerlin();
            case "QuattroStagioni": return new PizzaQuattroStagioniBerlin();
        }
        return null;
    }

}
