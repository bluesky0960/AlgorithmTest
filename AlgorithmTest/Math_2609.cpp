#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/2609
// 수학 문제

int getGCD(int a, int b);

int math_2609() {
	int a, b;
	int sN, bN;
	int gcd, lcm;
	cin >> a >> b;
	if (a >= b) {
		sN = b;
		bN = a;
	}
	else {
		sN = a;
		bN = b;
	}

	gcd = getGCD(sN, bN);
	lcm = (a * b) / gcd;
	cout << gcd << endl;
	cout << lcm;

	return 0;
}

int getGCD(int a, int b) {
	while (b != 0) {
		int mod = a % b;
		a = b;
		b = mod;
	}
	return a;
}