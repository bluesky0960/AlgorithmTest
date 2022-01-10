#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/1003
// 동적 프로그래밍 문제

int save[100];

int fibo(int n);

int dp_1003() {
	int testCase;
	int N;

	cin >> testCase;

	for (int i = 0; i < testCase; i++) {

		cin >> N;
		if (N == 0) {
			cout << 1 << " " << 0 << endl;
		}
		else if (N == 1) {
			cout << 0 << " " << 1 << endl;
		}
		else {
			fibo(N);
			cout << save[N - 1] << " " << save[N] << endl;
		}
	}
	

	return 0;
}

int fibo(int n) {

	if (n == 0) {
		save[0] = 0;
		return save[n];
	}
	else if (n == 1) {
		save[1] = 1;
		return save[n];
	}
	else if (save[n] != 0) {
		return save[n];
	}
	else {
		return save[n] = fibo(n-1) + fibo(n-2);
	}

}