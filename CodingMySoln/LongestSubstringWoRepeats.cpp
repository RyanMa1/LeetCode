#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
using namespace std;
class Solution {

public:
    int lengthOfLongestSubstring(string s) {
        vector<string> AnsOfSubstrings;
        vector<char> checkVec;
        deque<char> queChar;
        unordered_map<char, int> checkUmap;

        if(s.empty()){
            return 0;
        }else if(s.size() == 1){
            return 1;
        }
        int end = s.length();

        for(auto letter : s){
            //if you dont get consecutive letter

            if(checkUmap.find(letter) == checkUmap.end()){
                checkUmap.emplace(letter, 1);
                queChar.push_back(letter);
            }else {
//                cout << "in else" << endl;

                string posAns{queChar.begin(), queChar.end()};
//                cout << "PosAns:" << posAns << endl;
                AnsOfSubstrings.push_back(posAns);
                char frontChar = queChar.front();
                while (frontChar != letter) {
                    checkUmap.erase(frontChar);
                    queChar.pop_front();
                    frontChar = queChar.front();
                }

                queChar.pop_front();

                queChar.push_back(letter);
//                cout << "after clearing map: " << endl;
//
//
            }
        }
        if(!queChar.empty() && AnsOfSubstrings.empty()){
            return queChar.size();
        }
        int highestNum = AnsOfSubstrings[0].size();
        for(int i = 1; i < AnsOfSubstrings.size(); i++){
            if(highestNum < AnsOfSubstrings[i].size()){
//                cout << highestNum << endl;
                highestNum = AnsOfSubstrings[i].size();
            }
        }
        if(highestNum < queChar.size()){
            return queChar.size();
        }
//        for(const auto& x : queChar){
//            cout << "QueChar:" << x << endl;
//        }
        return highestNum;
    }
};
int main(){
    Solution sol;
    queue<char> que;
//    string x = "               ";
//    cout << x.size() << endl;
    cout << sol.lengthOfLongestSubstring("aab") << endl;

    return 0;
}