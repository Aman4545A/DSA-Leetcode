class Solution {
public:
    string frequencySort(string s) {
        string ans = "";

        unordered_map<char, int> mp;

        for (auto i : s) {
            mp[i]++;
        }

        vector<pair<char, int>> v(mp.begin(), mp.end());

       
        sort(v.begin(), v.end(), [](auto &a, auto &b) {
            return a.second > b.second;
        });

        
        for (auto x : v) {
            for (int i = 0; i < x.second; i++) {
                ans += x.first;
            }
        }

        return ans;
    }
};