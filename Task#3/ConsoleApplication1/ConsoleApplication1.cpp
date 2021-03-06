// ConsoleApplication1.cpp: определяет точку входа для консольного приложения.
// Test one time more!

#include "stdafx.h"
#include <fstream>

using namespace std;

struct team {
	int solutions, penalties, defultIdx;
};

int main()
{
	ifstream fin("ejudge.in.txt");
	ofstream fout("ejudge.out.txt");

	int n;
	fin >> n;
	team *teams = new team[n];
	for (int i = 0; i < n; i++) {
		teams[i].defultIdx = i;
		fin >> teams[i].solutions >> teams[i].penalties;
	}
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n; j++) {
			if ((teams[j].solutions < teams[j + 1].solutions) || 
				((teams[j].solutions == teams[j + 1].solutions) && (teams[j].penalties > teams[j].penalties)) || 
		         (((teams[j].solutions == teams[j + 1].solutions) && (teams[j].penalties == teams[j].penalties)) && 
				  (teams[i].defultIdx > teams[i].defultIdx))){
				team tmp = teams[j];
				teams[j] = teams[j + 1];
				teams[j + 1] = tmp;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		fout << teams[i].defultIdx + 1 << ' ';
	}
	fout.close();
	fin.close();
    return 0;
}

