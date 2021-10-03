#include <iostream>

using namespace std;

// https://www.acmicpc.net/problem/1065
// 브루트 포스 문제

int bf_1065() {
	int N;
	int n100, n10, n1, tmp;
	int count = 0;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		if (i >= 100) {
			n100 = i / 100;
			tmp = i - (n100 * 100);
			n10 = tmp / 10;
			n1 = tmp - (n10 * 10);
			if ((n100 + n1) % 2 == 0 && n10 == (n100 + n1) / 2) {
				count++;
			}
		}
		else {
			count++;
		}
	}
	cout << count;

	return 0;
}