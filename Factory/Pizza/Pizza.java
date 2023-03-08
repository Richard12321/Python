package Pizza;

import java.util.ArrayList;

public abstract class Pizza {

    public String name;
    public ArrayList<String> toppings = new ArrayList<>();

    public void prepare() {
        System.out.println("Preparing " + name + " ...");
        for (String topping : toppings) {
            System.out.println("\t" + topping);
        }
    }

    public void bake() {
        System.out.println("Baking");
    }

    public void cut() {
        System.out.println("Cutting");
    }

    public void box() {
        System.out.println("Boxing");
    }

    public String getName() {
        return name;
    }
}
