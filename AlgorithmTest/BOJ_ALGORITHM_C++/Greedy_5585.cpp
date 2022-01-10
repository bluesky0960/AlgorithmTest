#include <iostream>

using namespace std;

// https://www.acmicpc.net/submit/5585
// 그리디 문제

int greedy_5585() {
	int money = 1000;
	int N, cost, change;;
	int maxChange = 1;
	int idx = 0;
	int changeList[6] = {500, 100, 50, 10, 5, 1};
	int result = 0;

	cin >> cost;

	change = 1000 - cost;

	for (int i = 0; i < 6; i++) {
		if (change >= changeList[i]) {
			maxChange = changeList[i];
			idx = i;
			break;
		}
	}

	N = change / maxChange;

	while (1) {
		result += N;
		change -= (changeList[idx] * N);
		if (change == 0) {
			cout << result;
			break;
		}
		idx++;
		N = change / changeList[idx];

	}
	return 0;
}