class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int>left(n,-1);
        vector<int>right(n,n);
        stack<int>s;

       // left smaller 

        for(int i=0; i<n; i++){
            while(s.size()>0 && heights[s.top()]>=heights[i]){
                s.pop();
            }
            if(!s.empty()){
                left[i] = s.top() ;
            }
            s.push(i);
        }

        while(!s.empty()){
            s.pop();
        }

        // Right smaller

          for(int i=n-1; i>=0; i--){
            while(s.size()>0 && heights[s.top()]>=heights[i]){
                s.pop();
            }
            if(!s.empty()){
                right[i] = s.top() ;
            }
            s.push(i);
        }

       int area =0;
       for(int i=0; i<n; i++){
          int width = right[i]-left[i]-1;
          int ans = heights[i]*width;
          area = max(ans, area); 
        } 
        return area;
    }
};