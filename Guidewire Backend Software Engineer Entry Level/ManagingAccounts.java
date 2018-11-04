class ManagingAccoutns 
{
    public int solution(int A) 
    {
        // write your code in Java SE 8

        String num;
        num = String.valueOf(A);
        
        if (num.length() == 1)
        {
            return A;
        }
		
        int i, j;
        String res;        
        
        i = 0;
        j = num.length()-1;
        res = "";
        
        while (i<j)
        {
            res += String.valueOf(num.charAt(i))+String.valueOf(num.charAt(j));
            i = i+1;
            j = j-1;
        }
        
        if (i == j)
        {
            res += String.valueOf(num.charAt(i));
        }
        
        return Integer.parseInt(res);
    }
}
