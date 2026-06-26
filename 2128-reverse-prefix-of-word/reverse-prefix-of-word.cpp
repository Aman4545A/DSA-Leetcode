class Solution {
public:
    string reversePrefix(string word, char ch) {
        // stack<char>st;
        
        
        // if (word.find(ch) == string::npos) {
        //     return word;
        // }
        
        // for(int i=0; i<word.size(); i++){
        //     if(word[i]==ch){
        //         st.push(word[i]);
        //         break;
        //     }
        //     st.push(word[i]);
        // }
        // int i =0;
        // while(!st.empty()){
        //    word[i]= st.top();
        //    st.pop(); 
        //    i++;
        // }

        // return word;

         if (word.find(ch) == string::npos) {
            return word;
        }

        int index = word.find(ch);
        int i =0; 
        int j = index;

        while(i<=j){
          swap(word[i],word[j]);
          i++;
          j--;
        }
        return word;
    }
};