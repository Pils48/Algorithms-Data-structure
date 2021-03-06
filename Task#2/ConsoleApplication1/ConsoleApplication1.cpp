// ConsoleApplication1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("taxi.in.txt");
	ofstream fout("taxi.out.txt");

	int n;
	fin >> n;
	int *staff = new int[n];
	for (int i = 0; i < n; i++) {
		fin >> staff[i];
	}
	int *cabs = new int[n];
	for (int i = 0; i < n; i++) {
		fin >> cabs[i];
	}
	int *idxs = new int[n];

	for (int j = 0; j < n; j++) {
		int min = staff[0];
		int max = cabs[0];
		int iMin = 0;
		int iMax = 0;
		for (int i = 0; i < n; i++) {
			if (staff[i] < min) {
				min = staff[i];
				iMin = i;
			}
			if (cabs[i] > max) {
				max = cabs[i];
				iMax = i;
			}
		}
		staff[iMin] = 100000;
		cabs[iMax] = -1;
		idxs[iMin] = iMax;
	}

	for (int i = 0; i < n; i++) {
		fout << idxs[i] + 1 << ' ';
	}
	fin.close();
	fout.close();
    return 0;
}

