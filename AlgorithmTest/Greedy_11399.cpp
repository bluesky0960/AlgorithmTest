#include <iostream>
#include <list>

using namespace std;

// https://www.acmicpc.net/problem/11399
// 그리디 문제

int greedy_11399() {
	int num, time;
	int total = 0;
	int last = 0;
	list<int> num_list;
	
	list<int>::iterator iter;

	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> time;
		num_list.push_back(time);
	}
	for (int val : num_list) {
		cout << val << " ";
	}
	cout << endl;

	num_list.sort();
	for (int val : num_list) {
		cout << val << " ";
	}
	cout << endl;

	for (iter = num_list.begin(); iter != num_list.end(); iter++) {
		cout << *iter << endl;
		total = total + *iter + last;
		last += *iter;
		cout << "total: " << total << " last: " << last << endl;
	}

	cout << total << endl;

	return 0;
}