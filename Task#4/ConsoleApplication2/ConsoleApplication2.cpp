// ConsoleApplication2.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <string>

using namespace std;

/*Function return true when the first element is more than the second one*/

bool compare(string Str1, string Str2) {
	if (Str1.size() == Str2.size()) {
		for (int i = 0; i < Str1.size(); i++) {
			if (Str1[i] > Str2[i]) { return true; }
			else {
				return false;
			}
			return true;
		}
	}
	else {
		if (atoi((Str1 + Str2).c_str()) > atoi((Str2 + Str1).c_str())) {
			return true;
		}
		else {
			return false;
		}
	}
}

int main()
{

	ifstream fin("number.in.txt");
	ofstream fout("number.out.txt");

	string buffer = "";
	vector<string> strArr;
	while (!fin.eof()) {
		fin >> buffer;
		strArr.push_back(buffer);
	}

	for (int i = 0; i < strArr.size() - 1; i++) {
		for (int j = strArr.size() - 1; j > i ; j--) {
			if (compare(strArr[j], strArr[j - 1])) {
				string tmp = strArr[j];
				strArr[j] = strArr[j - 1];
				strArr[j - 1] = tmp;
			}
		}
	}
	for (int i = 0; i < strArr.size(); i++) {
		fout << strArr[i];
}
	
	fin.close();
	fout.close();
	return 0;
}

