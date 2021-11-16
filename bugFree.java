import java.io.*;
import java.util.*;
public class bugFree {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0; i<t; i++) {
            int[] tc = {sc.nextInt(), sc.nextInt(), sc.nextInt()};
            System.out.println(numDay(tc,1));
        }
   }
    static int numDay(int[] tc, int ans) {
        for(int i=tc[2]; i>0;) {
            int t = i - tc[0];
            if(t > 0) {
                i = t + tc[1];
            } else break;
            ans++;
        }
        return ans;
    }
}