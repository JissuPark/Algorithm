package com.company.BOJ;

import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public class Two00seven {
    public static void main(String[] args){
        String[] day = new String[]{"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        Scanner scanner = new Scanner(System.in);
        int month = scanner.nextInt();
        int date = scanner.nextInt();
        Date when = new Date(107, month-1, date);
        Calendar calendar = Calendar.getInstance();
        calendar.setTime(when);
        System.out.println(day[calendar.get(calendar.DAY_OF_WEEK)-1]);
    }
}
