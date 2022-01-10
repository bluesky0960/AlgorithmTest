#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// https://www.acmicpc.net/problem/2309
// 브루트포스 문제

int bf_2309() {

	int N;
	int answer[7];
	vector<int> hList;

	bool isEnd = false;
	
	for (int i = 0; i < 9; i++) {
		cin >> N;
		hList.push_back(N);
	}

	//순열은 오름차순으로 정렬해야 모든 경우의 수를 구함
	// 왼쪽에 큰수가 배치되어 있다면 더이상 탐색을 안함
	sort(hList.begin(), hList.end());

	for (int i = 1; i <= 9; i++) {
		if (!isEnd) {
			do {	//순열을 구하는 next_permutation을 이용해 조합구하기
				int tmp[7];
				int height = 0;
				// nCr -> n=9, r=7이기 때문에 7사용
				for (int j = 0; j < 7; j++) {
					tmp[j]= hList[j];
					height += hList[j];
				}
				// 조합의 합이 100이면 루프문 break;
				if (height == 100) {
					copy(tmp, tmp + 7, answer);
					isEnd = true;
					break;
				}

			} while (next_permutation(hList.begin(), hList.end()));
		}
		else {
			break;
		}
	}
	for (int i = 0; i < 7; i++) {
		cout << answer[i] << endl;
	}

	return 0;
}