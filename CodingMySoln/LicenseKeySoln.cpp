#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        int count = 0;
        int totalNumLetters = 0;
        string noHyphen = "";
        string ans;
        int firstDash = 0;
//------------------------------------------------------------
        for(auto& letter : S){
            if(letter != '-'){

                totalNumLetters++;
                noHyphen += toupper(letter);
            }
        }
        int odd = totalNumLetters % K;
        if(totalNumLetters < K){
            return noHyphen;
        }
//--------------------------------------------------------------
        else if(!odd){
            int pos = 1;
            for(auto& letter : noHyphen) {
                count++;
                if(count % K == 0 && count + K <= noHyphen.length()){
                    noHyphen.insert(count, "-");
                    count++;
                }
            }
            ans = noHyphen;
        }else if(odd == 1){
            int pos = 1;
            for(auto& letter : noHyphen){
                count++;

                if(count == 1 && firstDash == 0) {
                    noHyphen.insert(pos, "-");
                    firstDash = 1;
                    count = 0;
                    pos += K + 1;
                }else if((count % K == 0) && firstDash == 1 && pos < noHyphen.length() ){
                    noHyphen.insert(pos, "-");
                    pos += K + 1;
                    count = 0;
                }
            }
            ans = noHyphen;
        }else if(odd > 1){
            int firstTotalGroup = odd;
            int pos = firstTotalGroup;

            for(auto& letter : noHyphen){
                count++;
                if(count == firstTotalGroup && firstDash == 0){
                    noHyphen.insert(pos, "-");
                    count = 0;
                    firstDash = 1;
                }else if(count == K && firstDash == 1){
                    pos = pos + count + 1;
                    if(pos < noHyphen.length()){
                        noHyphen.insert(pos, "-");
                        count = 0;
                    }
                }

            }
            ans = noHyphen;
        }
        cout << ans << endl;
        return ans;
    }
};

int main(){
    Solution sol;
    sol.licenseKeyFormatting("----------kmhvVuPIyobPjThzMdhzvBWqNwfDajFiWUQvSUfrQsTuHorFisEjIbHtNEPrLbHJFnDNWFijctwBskljKratHqSOWBOgDnaQodjo", 11);

    return 0;
}


