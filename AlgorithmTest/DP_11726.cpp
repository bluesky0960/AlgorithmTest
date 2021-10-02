#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/11726
// 동적 프로그래밍 문제

int getNum(int n);

int dp_11726() {
	int N;

	cin >> N;

	cout<< getNum(N);

	return 0;
}

int getNum(int n) {
	int board[1000];
	int div = 10007;

	board[1] = 1;
	board[2] = 2;

	for (int i = 3; i <= n; i++) {
		board[i] = (board[i - 1] + board[i - 2]) % div;
	}
	return board[n];
}