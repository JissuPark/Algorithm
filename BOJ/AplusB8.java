package com.company.BOJ;

import java.util.Scanner;

public class AplusB8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            // 방법 1 : println
            String s = "Case #" + (i + 1) + ": " + A + " + " + B + " = " + (A + B);
            System.out.println(s);
            // 방법 2 : printf
            System.out.printf("Case #%d: %d + %d = %d\n", (i + 1), A, B, (A + B));
        }
    }
}
