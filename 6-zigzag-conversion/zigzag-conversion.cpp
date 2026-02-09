class Solution {
public:
    string convert(string s, int row) {

        if (row == 1) return s;

        int n = s.length();
        int start = 0;
        int tempRow = row;

        int cycle = 2 * row - 2;

        string result = "";

        while (tempRow > 0) {

            int i = start;

            while (i < n) {

                result += s[i];

                if (start != 0 && start != row - 1) {

                    int diag = i + cycle - 2 * start;

                    if (diag < n)
                        result += s[diag];
                }

                i = i + cycle;
            }

            start++;
            tempRow--;
        }

        return result;
    }
};