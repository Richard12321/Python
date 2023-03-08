package pizzashop;

import Pizza.Pizza;
import PizzaStore.*;


public class PizzaShop {

    public static void main(String[] args) {
        PizzaStore Berlin = new PizzaStoreBerlin();
        PizzaStore Hamburg = new PizzaStoreHamburg();
        PizzaStore Rostock = new PizzaStoreRostock();

        Pizza berlinerSalami = Berlin.orderPizza("Salami");
        System.out.println("Bestellt: " + berlinerSalami.getName());

        System.out.println("---------------------------------------------------");

        Pizza rostockerCalzone = Rostock.orderPizza("Calzone");
        System.out.println("Bestellt: " + rostockerCalzone.getName());

        System.out.println("---------------------------------------------------");

        Pizza hamaburgerHawaii = Hamburg.orderPizza("Hawaii");
        System.out.println("Bestellt: " + hamaburgerHawaii.getName());
    }

}
