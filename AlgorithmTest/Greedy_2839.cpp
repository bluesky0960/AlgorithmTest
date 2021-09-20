#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/2839
// 그리디 문제

int greedy_2839() {
	int kg;
	int kg3, kg5, bag;

	cin >> kg;
	
	kg5 = kg / 5;

	while (1) {
		if (kg5 < 0) {
			cout << -1;
			return 0;
		}
		if ((kg - (kg5 * 5)) % 3 == 0) {
			kg3 = (kg - (kg5 * 5)) / 3;
			break;
		}
		kg5--;
	}
	cout << kg5 + kg3;

}