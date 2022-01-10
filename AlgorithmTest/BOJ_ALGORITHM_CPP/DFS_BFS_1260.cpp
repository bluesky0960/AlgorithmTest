#include <iostream>
#include <queue>

#define MAX_VALUE 1001	// N�� 1~1000

using namespace std;

// https://www.acmicpc.net/problem/1260
// DFS, BFS ����

int N, M, V; // �Է°�
int mat[MAX_VALUE][MAX_VALUE]; // ������� ����
bool isVisited[MAX_VALUE]; // �湮�� ���(ó���� �� FALSE)


void getDFS(int v);
void getBFS(int v);

int dfs_bfs_1260() {
	int x, y; // ��尣 ����
	cin >> N >> M >> V;
	
	for (int i = 0; i < M; i++) {
		cin >> x >> y;
		mat[x][y] = mat[y][x] = 1; // ������� �� ǥ��
	}
	getDFS(V);
	cout << endl;
	getBFS(V);

	return 0;
}

void getDFS(int v) {
	cout << v << " ";
	isVisited[v] = true; // �湮�� V�� ��� TRUE�� ����
	for (int i = 1; i <= N; i++) {
		if (isVisited[i] || mat[v][i] == 0) {  // �湮�Ǿ��ų� ��������� 0�̸� �ʿ�����Ƿ� Continue
			continue;
		}
		getDFS(i); // ����Լ��� ��� ��忡 ���� Ž��
	}
}

void getBFS(int v) {
	queue<int> q;
	q.push(v);
	isVisited[v] = false; // �ռ� DFS���� �� �湮�� �Ͽ� TRUE�س��� ������ �ݴ�� ����
	while (!q.empty()) { // ť�� ��� ���Ұ� ������������ �ݺ�
		v = q.front();
		cout << q.front() << " ";
		q.pop(); // ���� ó���� ���Ҹ� ��ȯ

		for (int i = 1; i <= N; i++) {
			if (!isVisited[i] || mat[v][i] == 0) { // �湮�� �Ǿ��ų� ������Ŀ��� ���谡 ������ continue
				continue;
			}
			q.push(i); // if�� ������ �ش���� �ʴ´ٸ� ť�� ���� �ֱ�
			isVisited[i] = false; // �湮�� �Ǿ��ٰ� ǥ��
		}
	}
}