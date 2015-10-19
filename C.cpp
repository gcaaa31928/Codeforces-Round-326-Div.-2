// Created by GCA on 2015/10/19

#include  <bits/stdc++.h>
using namespace std;

const int maxn = 1000105;
int a[maxn];
int n;
int main() {
    memset(a, 0, sizeof(a));
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int t;
        scanf("%d", &t);
        a[t]++;
    }
    int ans=0;
    for (int i = 0; i < maxn; i++) {
        ans += a[i]%2;
        a[i+1]+=a[i]/2;
    }
    printf("%d\n",ans);
}