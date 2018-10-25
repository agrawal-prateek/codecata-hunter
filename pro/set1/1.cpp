#include <bits/stdc++.h>
using namespace std;
string commonPrefixUtil(string str1, string str2)
{
	string result;
	int n1 = str1.length(), n2 = str2.length();
	for (int i = 0, j = 0; i <= n1 - 1 && j <= n2 - 1; i++, j++) {
		if (str1[i] != str2[j])
			break;
		result.push_back(str1[i]);
	}

	return (result);
}

void commonPrefix(string arr[], int n)
{
	sort(arr, arr + n);
	cout << commonPrefixUtil(arr[0], arr[n - 1]);
}

int main()
{
    string s1,s2;
    int n;
    std::cin >> n;
    std::cin >> s1;
    std::cin >> s2;
	string arr[] = { s1,s2};

	commonPrefix(arr, n);

	return 0;
}
