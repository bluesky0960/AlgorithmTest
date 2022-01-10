#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// https://www.acmicpc.net/problem/9251
// 동적 프로그래밍 문제

int dp[1001][1001];

int dp_9251() {
	string str1, str2;
	cin >> str1 >> str2;
	

	for (int i = 1; i <= str1.length(); i++) {
		for (int j = 1; j <= str2.length(); j++) {
			if (str1[i - 1] == str2[j - 1]) {
				// 같은 문자는 왼쪽 대각 + 1
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}
			else {
				// 다른 문자는 왼쪽, 윗쪽 중 큰 값
				dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
			}
		}
	}

	cout << dp[str1.length()][str2.length()];
	return 0;
}