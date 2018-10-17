// Enter your code here.
import java.util.Scanner;

abstract class Distance {
    protected int feet;
    protected float inches;
    
	abstract public void setFeetAndInches(int feet, float inches);
	abstract public int getFeet();
	abstract public float getInches();
	abstract String getDistanceComparison(Distance dist2);
}


class DistanceImplementation extends Distance
{
    public void setFeetAndInches(int feet, float inches)
    {
        this.feet = feet;
        this.inches = inches;
    }
    
    String getDistanceComparison(Distance dist2)
    {
        if (((dist2.feet*12)+(dist2.inches))>((this.feet*12)+(this.inches)))
        {
            return "Second distance is greater.";
        }
        else if (((dist2.feet*12)+(dist2.inches))<((this.feet*12)+(this.inches)))
        {
            return "First distance is greater.";
        }
        else
        {
            return "Both distances are equal.";
        }
    }
    
    public int getFeet()
    {
        return this.feet;
    }
    
    public float getInches()
    {
        return this.inches;
    }
}

public class DistanceCalculator {
    private static final Scanner scan = new Scanner(System.in);
    
	public static void main(String[] args) {
		Distance dist1 = new DistanceImplementation();
		Distance dist2 = new DistanceImplementation();
        
        int feet1 = scan.nextInt();
        float inches1 = scan.nextFloat();
        
        int feet2 = scan.nextInt();
        float inches2 = scan.nextFloat();
        
        dist1.setFeetAndInches(feet1, inches1);
        dist2.setFeetAndInches(feet2, inches2);
        
        System.out.println(dist1.getDistanceComparison(dist2));
	}
}