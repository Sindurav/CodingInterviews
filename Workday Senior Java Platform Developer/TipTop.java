public class TipTop
{
  static final Integer i1 = 1;
  final Integer i2 = 2;
  Integer i3 = 3;
  public static void main(String[] args)
  {
    final Integer i4 = 4;
    Integer i5 = 5;

    class Inner
    {
      final Integer i6 = 6;
      Integer i7 = 7;
      Inner()
      {
        System.out.println(i6+i7);
      }
    }
  }
}