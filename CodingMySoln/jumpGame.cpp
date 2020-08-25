#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
  		lengthList = nums.size();
  		bool check = false;
  		for(int i = 0; i < nums.size(); i++){
  			if(nums[i] == 0){
  				check = true;
  			}
  		}
  		if(check){
  			for(int i = 0; i < nums.size(); i++){
  				maxJumps = nums[i];
  				if(maxJumps + i >= lengthList - 1 ){
  					maxJumps = maxJumps - 1;
  					while(maxJumps > 0){
  						if(maxJumps + i < lengthList - 1 && nums[maxJumps + i] != 0){
  							i = maxJumps;
  							break;
  						}else{
  							maxJumps -= 1;
  						}
  					}
  					if(maxJumps == 0){
  						return false;
  					}
  				}else if(maxJumps + i < lengthList - 1 && nums[maxJumps + i] != 0){
  					i = maxJumps - 1 ;
  				}else if(maxJumps + i == lengthList - 1){
  					return true;
  				}
  				return false;
  			}
  		}else{
  			return false;
  		}
    }
};
int main(){

	return 0;
}