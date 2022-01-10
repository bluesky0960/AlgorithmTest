#include <iostream>
#include <list>

using namespace std;

// https://www.acmicpc.net/problem/4796
// 그리디 문제

int greedy_4796() {
	int n, N;
	int L, P, V;
	int mod;
	int stayDate = 0;
	int count = 1;
	list<int> stay;
	list<int> date;

	while (1) {
		for (int i = 0; i < 3; i++) {
			cin >> n;
			if (n == 0) {
				break;
			}
			date.push_back(n);
		}
		if (n == 0) {
			break;
		}
	}

	while (!date.empty()) {
		L = date.front();
		date.pop_front();
		P = date.front();
		date.pop_front();
		V = date.front();
		date.pop_front();

		N = V / P;
		mod = V - (N * P);
		if (mod > L) { // 나머지가 사용날짜보다 클때
			stayDate = ((N * L) + L);
		}
		else { // 나머지가 사용날짜보다 적을때
			stayDate = ((N * L) + mod);
		}
		stay.push_back(stayDate);

	}
	
	for (int val : stay) {
		cout << "Case " << count << ": " << val;
		if (stay.size() != count) {
			cout << endl;
		}
		count++;
	}
	return 0;
}