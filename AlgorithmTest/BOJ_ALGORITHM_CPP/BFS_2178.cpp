#include <iostream>
#include <queue>

#define MAX_VALUE 101

using namespace std;

// https://www.acmicpc.net/problem/2178
// BFS 문제

// 최단거리는 보통 BFS로 푼다(너비 우선이기 때문에 시작부터 도착지점에 닿으면 최단거리)
// DFS는 시작부터 모든 노드를 탐색해야 끝나기 때문에 경우의 수가 너무 많다(시간 초과)

int N, M;
char mat[MAX_VALUE][MAX_VALUE];
bool isVisited[MAX_VALUE][MAX_VALUE];

int dx[4] = {1, -1, 0, 0}; // 오른쪽, 왼쪽, 윗쪽, 아랫쪽
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
	q.push(make_pair(make_pair(0, 0), 1)); // 첫째 Pair: 위치, 둘째 Pair: 움직인 거리

	isVisited[0][0] = 1;

	while (!q.empty()) {
		int x = q.front().first.second; // 위치의 X좌표
		int y = q.front().first.first; // 위치의 Y좌표
		int dist = q.front().second; // 움직인 거리

		q.pop();

		if (x == M - 1 && y == N - 1) {
			return dist;
		}

		for (int i = 0; i < 4; i++) { // 동서남북 체크
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || ny < 0 || nx >= M || ny >= N) { // 동서남북이 크기를 벗어났을땐 continue
				continue;
			}
			if (isVisited[ny][nx] == 1) { // 이미 방문했다면 continue
				continue;
			}
			if (mat[ny][nx] != '1') { // 0인 노드라면 continue
				continue;
			}
			q.push(make_pair(make_pair(ny, nx), dist + 1)); // 위 3개의 조건이 해당이 안되면 Q에 넣기
			isVisited[ny][nx] = 1; // 방문했다고 표시
		}
	}
}