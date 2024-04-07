#include <bits/stdc++.h>
using namespace std;

int max_sum (int a[], int n){
	int max_till_here = INT_MIN, max_at_ith = 0;
	for(int i =0;i<n;i++){
		max_at_ith+=a[i];
		if(max_till_here<max_at_ith){
			max_till_here = max_at_ith;
		}
		if(max_at_ith<0){
			max_at_ith=0;
		}
	}
	return max_till_here;
}
int main() {
	int  n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	int ans = max_sum(a, n);
	cout<<ans;
	return 0;
}