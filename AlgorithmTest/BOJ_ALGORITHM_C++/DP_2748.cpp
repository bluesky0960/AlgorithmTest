#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/2748
// 동적 프로그래밍 문제

// 숫자 범위가 int를 넘어감
long long dp[100];

long long fibo3(int n);

int dp_2748() {
	
	int N;

	cin >> N;

	dp[0] = 0;
	dp[1] = 1;

	cout << fibo3(N);
	return 0;
}

long long fibo3(int n) {

	if (n == 0) {
		dp[0] = 0;
		return dp[n];
	}
	else if (n == 1) {
		dp[1] = 1;
		return dp[n];
	}
	else if (dp[n] != 0) {
		return dp[n];
	}
	else {
		return dp[n] = fibo3(n - 1) + fibo3(n - 2);
	}
}