#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/10870
// 동적 프로그래밍 문제

int fiboList[100];

int fibo2(int n);

int dp_10870() {

	int N;
	cin >> N;
	fibo2(N);
	cout << fiboList[N];

	return 0;
}

int fibo2(int n) {
	if (n == 0) {
		fiboList[0] = 0;
		return 0;
	}
	else if (n == 1) {
		fiboList[1] = 1;
		return 1;
	}
	else if (fiboList[n] != 0) {
		return fiboList[n];
	}
	else {
		return fiboList[n] = fibo2(n - 1) + fibo2(n - 2);
	}
}