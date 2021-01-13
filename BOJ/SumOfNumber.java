package com.company.BOJ;

import java.util.Scanner;

public class SumOfNumber {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int res = 0;
        int N = scanner.nextInt();
        String number = scanner.next();
        for(int i=0;i<number.length();i++){
            res += Integer.parseInt(number.substring(i,i+1));
        }
        System.out.println(res);
    }
}
