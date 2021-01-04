package com.company.BOJ;

import java.util.Scanner;

public class Multiply {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int first = scanner.nextInt();
        String second = scanner.next();
        // 처음 짠 코드
        for(int i=second.length()-1; i>=0 ; i--){
            System.out.println(Integer.parseInt((String.valueOf(second.charAt(i))))*first);
        }
        // 두번째 코드
        for(int i=second.length()-1; i>=0 ; i--){
            System.out.println(Character.getNumericValue(second.charAt(i))*first);
        }
        // 마지막 코드
        for(int i=second.length()-1; i>=0 ; i--){
            System.out.println(Integer.parseInt(second.substring(i,i+1))*first);
        }
        System.out.println(first*Integer.parseInt(second));
    }
}
