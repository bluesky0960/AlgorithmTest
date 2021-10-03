#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// https://www.acmicpc.net/problem/2309
// ���Ʈ���� ����

int bf_2309() {

	int N;
	int answer[7];
	vector<int> hList;

	bool isEnd = false;
	
	for (int i = 0; i < 9; i++) {
		cin >> N;
		hList.push_back(N);
	}

	//������ ������������ �����ؾ� ��� ����� ���� ����
	// ���ʿ� ū���� ��ġ�Ǿ� �ִٸ� ���̻� Ž���� ����
	sort(hList.begin(), hList.end());

	for (int i = 1; i <= 9; i++) {
		if (!isEnd) {
			do {	//������ ���ϴ� next_permutation�� �̿��� ���ձ��ϱ�
				int tmp[7];
				int height = 0;
				// nCr -> n=9, r=7�̱� ������ 7���
				for (int j = 0; j < 7; j++) {
					tmp[j]= hList[j];
					height += hList[j];
				}
				// ������ ���� 100�̸� ������ break;
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