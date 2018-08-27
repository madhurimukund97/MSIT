import java.util.Scanner;

public class Solution {
	/*
	Do not modify this main function.
	*/
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int base = scan.nextInt();
		int height = scan.nextInt();
		areaOfTriangle(base, height);
	}
	public static void areaOfTriangle(int base1, int height1){
		double area;
		area = 0.5*base1*height1;
		System.out.println(area);
	}
	/*
	Need to fill the areaOfTriangle function and print the output
	of fahrenheit.
	*/
}