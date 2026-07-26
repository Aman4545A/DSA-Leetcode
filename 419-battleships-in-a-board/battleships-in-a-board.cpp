class Solution {
public:

    void dfs(int i, int j,
             vector<vector<bool>>& vis,
             vector<vector<char>>& board,
             int n, int m) {

        // Boundary and invalid cell check
        if (i < 0 || i >= n ||
            j < 0 || j >= m ||
            vis[i][j] ||
            board[i][j] != 'X') {
            return;
        }

        vis[i][j] = true;

        // Down
        dfs(i + 1, j, vis, board, n, m);

        // Up
        dfs(i - 1, j, vis, board, n, m);

        // Right
        dfs(i, j + 1, vis, board, n, m);

        // Left
        dfs(i, j - 1, vis, board, n, m);
    }

    int countBattleships(vector<vector<char>>& board) {

        int ans = 0;

        int n = board.size();
        int m = board[0].size();

        vector<vector<bool>> vis(
            n,
            vector<bool>(m, false)
        );

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                if (board[i][j] == 'X' &&
                    !vis[i][j]) {

                    dfs(i, j, vis, board, n, m);

                    ans++;
                }
            }
        }

        return ans;
    }
};