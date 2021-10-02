#include <iostream>

using namespace std;

int dp_2133() {
	int N;
	int board[31] = {};

	cin >> N;
	board[0] = 1;
	board[2] = 3;

	for (int i = 4; i <= N; i++) {
		// 2*3도형 종류가 3개 -> *3
		board[i] = board[i - 2] * 3;
		for (int j = 4; j <= i; j += 2) {
			// n=4부터는 새로운 도형이 2개씩 추가 -> 4,6,8...이므로 +=2씩 해준다
			board[i] += board[i - j] * 2;
		}
	}
	cout << board[N];

	return 0;
}