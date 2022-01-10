#include <iostream>
#include <queue>

#define MAX_VALUE 1001	// N이 1~1000

using namespace std;

// https://www.acmicpc.net/problem/1260
// DFS, BFS 문제

int N, M, V; // 입력값
int mat[MAX_VALUE][MAX_VALUE]; // 인접행렬 생성
bool isVisited[MAX_VALUE]; // 방문된 노드(처음은 다 FALSE)


void getDFS(int v);
void getBFS(int v);

int dfs_bfs_1260() {
	int x, y; // 노드간 연결
	cin >> N >> M >> V;
	
	for (int i = 0; i < M; i++) {
		cin >> x >> y;
		mat[x][y] = mat[y][x] = 1; // 인접행렬 값 표시
	}
	getDFS(V);
	cout << endl;
	getBFS(V);

	return 0;
}

void getDFS(int v) {
	cout << v << " ";
	isVisited[v] = true; // 방문된 V번 노드 TRUE로 변경
	for (int i = 1; i <= N; i++) {
		if (isVisited[i] || mat[v][i] == 0) {  // 방문되었거나 인접행렬이 0이면 필요없으므로 Continue
			continue;
		}
		getDFS(i); // 재귀함수로 모든 노드에 대해 탐색
	}
}

void getBFS(int v) {
	queue<int> q;
	q.push(v);
	isVisited[v] = false; // 앞서 DFS에서 다 방문을 하여 TRUE해놨기 때문에 반대로 진행
	while (!q.empty()) { // 큐의 모든 원소가 없어질때까지 반복
		v = q.front();
		cout << q.front() << " ";
		q.pop(); // 제일 처음의 원소를 반환

		for (int i = 1; i <= N; i++) {
			if (!isVisited[i] || mat[v][i] == 0) { // 방문이 되었거나 인접행렬에서 관계가 없으면 continue
				continue;
			}
			q.push(i); // if의 사항이 해당되지 않는다면 큐에 원소 넣기
			isVisited[i] = false; // 방문이 되었다고 표시
		}
	}
}