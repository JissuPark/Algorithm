package com.company.BOJ;

import java.util.Scanner;

public class AplusB5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while(true) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            if(A+B==0){break;}
            System.out.println(A + B);
        }
    }
}
