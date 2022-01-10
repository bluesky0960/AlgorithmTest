#include <iostream>
#include <queue>

#define MAX_VALUE 101

using namespace std;

// https://www.acmicpc.net/problem/2178
// BFS ����

// �ִܰŸ��� ���� BFS�� Ǭ��(�ʺ� �켱�̱� ������ ���ۺ��� ���������� ������ �ִܰŸ�)
// DFS�� ���ۺ��� ��� ��带 Ž���ؾ� ������ ������ ����� ���� �ʹ� ����(�ð� �ʰ�)

int N, M;
char mat[MAX_VALUE][MAX_VALUE];
bool isVisited[MAX_VALUE][MAX_VALUE];

int dx[4] = {1, -1, 0, 0}; // ������, ����, ����, �Ʒ���
int dy[4] = {0, 0, -1, 1};

int getBFS();

int bfs_2178() {

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> mat[i];
	}

	cout << getBFS();
	return 0;
}

int getBFS() { 

	queue<pair<pair<int, int>, int>> q;
	q.push(make_pair(make_pair(0, 0), 1)); // ù° Pair: ��ġ, ��° Pair: ������ �Ÿ�

	isVisited[0][0] = 1;

	while (!q.empty()) {
		int x = q.front().first.second; // ��ġ�� X��ǥ
		int y = q.front().first.first; // ��ġ�� Y��ǥ
		int dist = q.front().second; // ������ �Ÿ�

		q.pop();

		if (x == M - 1 && y == N - 1) {
			return dist;
		}

		for (int i = 0; i < 4; i++) { // �������� üũ
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= M || ny >= N) { // ���������� ũ�⸦ ������� continue
				continue;
			}
			if (isVisited[ny][nx] == 1) { // �̹� �湮�ߴٸ� continue
				continue;
			}
			if (mat[ny][nx] != '1') { // 0�� ����� continue
				continue;
			}
			q.push(make_pair(make_pair(ny, nx), dist + 1)); // �� 3���� ������ �ش��� �ȵǸ� Q�� �ֱ�
			isVisited[ny][nx] = 1; // �湮�ߴٰ� ǥ��
		}
	}
}