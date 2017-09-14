//============================================================================
// Name        : Codility.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>


#include <string>

using namespace std;

/*
int solution(string strA, string strB) {
    // write your code in C++11 (g++ 4.8.2)
    size_t pos = strB.find(strA);

    if(pos == string::npos)
    	return -1;
    else
    	return pos;
}
*/
/*
int solution(string strA, string strB) {
    // write your code in C++11 (g++ 4.8.2)

}
*/
/*
int solution(int A, int B) {
    // write your code in C++11 (g++ 4.8.2)
    int C = 0;

    int decA = 1;
    int decB = 1;

    while(A/decA)
    {
    	decA = decA*10;
    }
    decA = decA/10;
    if(A==0)
    	decA = 1;

    while(B/decB)
	{
		decB = decB*10;
	}
	decB = decB/10;
	if(B==0)
		decB = 1;

	while(C <= 100000000 && (decA || decB))
	{
		if(decA)
		{
			C = C*10;
			C += (A/decA);
			A = A%decA;
			decA = decA/10;
		}

		if(decB)
		{
			C = C*10;
			C += (B/decB);
			B = B%decB;
			decB = decB/10;
		}
	}

	if(C > 100000000)
		return -1;
	else
		return C;
}*/
#include <map>
#include <sstream>

void parseString(string &str,int* t,int* n,int* c)
{
	int time = 0; // in sec
	int num = 0;
	int cost = 0;
	//hour
	int hr = (str[0]-'0')*10+(str[1]-'0');
	int min = (str[3]-'0')*10+(str[4]-'0');
	int sec = (str[6]-'0')*10+(str[7]-'0');

	min = hr*60 + min;
	time = min*60+sec;
	if(min>=5)
	{
		if(sec>0)
			cost = (min+1)*150;
		else
			cost =min*150;
	}
	else
		cost = time*3;

	num = (str[9]-'0')*100000000 +
		  (str[10]-'0')*10000000 +
		  (str[11]-'0')*1000000 +
		  (str[13]-'0')*100000 +
		  (str[14]-'0')*10000 +
		  (str[15]-'0')*1000 +
		  (str[17]-'0')*100 +
		  (str[18]-'0')*10 +
		  (str[19]-'0');

	*t =time;
	*n = num;
	*c = cost;
}

int solution(string &S) {
    // write your code in C++11 (g++ 4.8.2)
	map<int,int> timeMap;
	map<int,int> costMap;

	int maxTime = 0;
	int maxNum = 0;
	int totalCost = 0;
	stringstream sst(S);
	string str;
	map<int,int>::iterator it;
	while(sst >> str)
	{
		int time = 0; // in sec
		int num = 0;
		int cost = 0;

		parseString(str,&time,&num,&cost);



		it = costMap.find(num);
		if(it!=costMap.end())
		{
			costMap[num] = costMap[num]+cost;
		}
		else
			costMap.insert(pair<int,int>(num,cost));

		totalCost += cost;

		it = timeMap.find(num);
		if(it!=timeMap.end())
		{
			int tempTime = timeMap[num]+time;
			timeMap[num] = tempTime;
			if(maxTime<tempTime)
			{
				maxTime = tempTime;
				maxNum = num;
			}
			else if(maxTime == tempTime)
			{
				if(num < maxNum)
					maxNum = num;
			}
		}
		else
		{
			timeMap.insert(pair<int,int>(num,time));
			if(maxTime<time)
			{
				maxTime = time;
				maxNum = num;
			}
			else if(maxTime == time)
			{
				if(num < maxNum)
					maxNum = num;
			}
		}
	}//end of while

	//Remove promotion amount
	it = costMap.find(maxNum);
	if(it!=costMap.end())
	{
		totalCost -= it->second;
	}



	return totalCost;
}

int main() {
	string sss = "00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090";
	cout << solution(sss) << endl; // prints !!!Hello World!!!
	return 0;
}
