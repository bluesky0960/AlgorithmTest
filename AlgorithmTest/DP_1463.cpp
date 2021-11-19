#include <iostream>
#include <algorithm>

using namespace std;

int result[1000001]; // 입력값 N이 10^6


int dp_1463() {
	
	int N;

	cin >> N;

	result[1] = 0;

	for (int i = 2; i <= N; i++) {
		result[i] = result[i-1] + 1;
		if (i % 2 == 0) result[i] = min(result[i], result[i / 2] + 1);
		if (i % 3 == 0) result[i] = min(result[i], result[i / 3] + 1);
	}

	cout << result[N];

	return 0;
}