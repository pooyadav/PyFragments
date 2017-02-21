"""
SRM 709, 250 point

Problem Statement:

Hero owns a factory. There are n robots working at the factory. The robots are numbered 0 through n-1.

Today, exactly one of the robots became corrupted. Hero has decided to give all robots a test that may determine the number of the corrupted robot. The test works as follows: For each x from 0 to n-1, in order, Hero tells robot x a positive integer and the robot answers whether the integer is odd or even. Each normal robot will always give the correct answer. The corrupted robot may sometimes give the opposite answer. More precisely: the corrupted robot will answer incorrectly if and only if the previous robot was given an odd number. In particular, if robot 0 is the corrupted robot, it will give the correct answer (as there is no previous robot).

You are given a log of the test: a query and a answer, each with n elements. For each x, query[x] is the positive integer given to robot x, and answer[x] is the answer given by the robot: either "Odd" or "Even".

It is guaranteed that the situation described by query and answer could have occurred as described above. If it is possible to determine the index of the corrupted robot, return it. Otherwise, return -1.
Definition
Class:
Robofactory
Method:
reveal
Parameters:
tuple (integer), tuple (string)
Returns:
integer
Method signature:
def reveal(self, query, answer):
Limits
Time limit (s):
2.000
Memory limit (MB):
256
Constraints
- n will be between 1 and 50, inclusive.
- query and answer will contain exactly n elements.
- Each element in query will be between 1 and 1000, inclusive.
- Each element in answer will be either "Odd" or "Even".
- It is guaranteed that there will be at least one possible number of the corrupted robot.

"""

# Final Score: 129 --> 0 (challenged)

class Robofactory:

    # def int_to_even(self, a): return 1 if a % 2 == 0 else 0
    # def str_to_even(self, a): return 1 if a == 'Even' else 0

    # (int) -> (string) -> int
    def reveal(self, query, answer):
        n = len(query)
        if n == 1 : return 0
        que = map(lambda x: 1 if x % 2 == 0 else 0, query)
        ans = map(lambda x: 1 if x == 'Even' else 0, answer)
        for i in range(n):
            if que[i] != ans[i]:
                return i
        if (que[0] == 0): return 0 #
        return -1

def test():
    x = Robofactory()
    q1 = (3,2,2); a1 = ("Odd", "Odd", "Even")
    q2 = (1,3,5,10); a2 = ("Odd", "Odd", "Odd", "Even")
    q3 = (2,3,5,10); a3 = ("Even", "Odd", "Odd", "Even")
    q4 = (2,4,6,10); a4 = ("Even", "Even", "Even", "Even")
    q5 = (107,); a5 = ("Odd")
    q6 = (1,1,1); a6 = ("Odd", "Odd", "Even")
    print x.reveal(q1, a1) # 1
    print x.reveal(q2, a2) # 0
    print x.reveal(q3, a3) # -1
    print x.reveal(q4, a4) # -1
    print x.reveal(q5, a5) # 0
    print x.reveal(q6, a6) # 2



# test()

"""
One C++ solution:
# include <vector>
# include <string>

class Rbofactory {
	const std::string odd = "Odd";
	const std::string even = "Even";

public:
	int reveal(std:vector<int> query, std::vector<std::string> answer) {
		std::vector<int> candidates;
		candidated.push_back(0);
		for (size_t i = 0; i < query.size(); +i){
			bool isEven = query[i] % 2 == 0;
			bool strEven = answer[i] == even;
			if (isEven != strEven) {
				return i;
			}
			if (i > 0 && (query[i-1] % 2 == 0)) {
				candidates.push_back(i)
			}
		}

		if (candidates.size() == 1)
			return candidates[0]

		return -1;
	}

}

"""