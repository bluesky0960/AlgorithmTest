#include <iostream>
#include <algorithm>

using namespace std;

int dp_2579() {
	int N;
	int num[301];
	int dp[301];
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}
	
	dp[0] = num[0];
	dp[1] = max(num[0] + num[1], num[1]);
	dp[2] = max(num[0] + num[2], num[1] + num[2]);

	for (int i = 3; i < N; i++) {
		dp[i] = max(dp[i - 2] + num[i], dp[i - 3] + num[i - 1] + num[i]);
	}

	cout << dp[N - 1];

	return 0;
}