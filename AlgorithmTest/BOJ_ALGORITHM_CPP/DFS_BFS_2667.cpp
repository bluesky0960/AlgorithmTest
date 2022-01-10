#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

#define MAX_VALUE 26

using namespace std;


bool isVisited[MAX_VALUE][MAX_VALUE] = { false };
char board[MAX_VALUE][MAX_VALUE];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};
int N, cnt;
vector<int> v;

void dfs(int x, int y);
void bfs(int x, int y);

int dfs_bfs_2667() {

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> board[i];
	}


	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			//방문 안하고 1인 보드
			if (!isVisited[i][j] && board[i][j] == '1') {
				cnt = 0;
				//dfs(i, j);

				bfs(i, j);
				//단지 아파트 개수 넣기
				v.push_back(cnt);
			}
		}
	}
	sort(v.begin(), v.end());

	//vector의 크기가 단지 수
	cout << v.size() << endl;
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << endl;
	}
	return 0;
}

void dfs(int x, int y) {
	isVisited[x][y] = true;

	//단지내 아파트 개수
	cnt++;
	
	//상하좌우 검색
	for (int i = 0; i < 4; i++) {
		int newX = x + dx[i];
		int newY = y + dy[i];

		if (0 <= newX && newY <= N && 0 <= newY && newY <= N) {
			if (board[newX][newY] == '1' && !isVisited[newX][newY]) {
				dfs(newX, newY);
			}
		}
	}
}

void bfs(int x, int y) {
	isVisited[x][y] = 1;

	cnt++;

	queue<pair<int, int>>q;

	q.push(make_pair(x, y));

	while (!q.empty()) {
		int qx = q.front().first;
		int qy = q.front().second;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int newX = qx + dx[i];
			int newY = qy + dy[i];

			if (0 <= newX && newY <= N && 0 <= newY && newY <= N) {
				if (board[newX][newY] == '1' && !isVisited[newX][newY]) {
					q.push(make_pair(newX, newY));
					isVisited[newX][newY] = true;
					cnt++;
				}
			}
		}
	}
}