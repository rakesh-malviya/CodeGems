//============================================================================
// Name        : Huffman3.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

//============================================================================
// Name        : Huffman2.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

//============================================================================
// Name        : Huffman.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

class HFTNode
{
public:
	int freq;
	int code;
	int level;
	string codeString; // for debugging purpose
	HFTNode* parent;
	HFTNode* left;
	HFTNode* right;
	HFTNode* prev;
	HFTNode* next;
	bool leaf;
	bool breakForLoop;

	HFTNode(int cb,int f,string cbs,int l)
	{
		level = l;
		code = cb;
		codeString = cbs;
		freq = f;
		parent = NULL;
		left = NULL;
		right = NULL;
		prev = NULL;
		next = NULL;
		leaf = false;
		breakForLoop = false;
	}
};


bool sortLevels (HFTNode* i,HFTNode* j) { return (i->code < j->code); }

//Huffman Tree class
class HFT{
public:
	vector <vector<HFTNode*> > hftLevel;
	HFTNode* root;

	HFT()
	{
		root = new HFTNode(0,100,"R",0);
		hftLevel.push_back(vector<HFTNode*>()); //insert level for Root node
		hftLevel[0].push_back(root);
	}

	void hftInsert(string s);
	void hftLevelSort();
	int hftSetPrevNext();// will return -1 if input huffman codes are not correct
	int hftCount(HFTNode* cur);
	int hftLevelCount();
	int hftSeqRec(HFTNode* cur);
	int hftLevelCheck();
	bool hftCheck();
	HFTNode* findParent(HFTNode* n1,HFTNode* n2);
};

bool HFT::hftCheck()
{
	bool r = true;
	HFTNode* cur = root;
	while(true)
	{
		if(cur->prev)
		{
			if(cur->prev->freq > cur->freq)
				return false;

			cur = cur->prev;
		}
		else
			break;
	}
	return r;
}

int HFT::hftLevelCheck()
{
	HFTNode* cur = root;
	while(true)
	{
		if(cur->freq==0)
			return -1;

		if(cur->next && cur->freq > cur->next->freq)
			return 0;

		if(cur->prev && cur->freq < cur->prev->freq)
			return 0;

		if(cur->prev)
			cur = cur->prev;
		else
			break;

	}

	return 1;
}

int HFT::hftSeqRec(HFTNode* cur)
{
	int count = 0;
	if(!cur->leaf)
	{
		int curFreq = cur->freq;

		for(int i=0;i<curFreq/2;i++)
		{
			int leftFreq = curFreq/2 -i;
			int rightFreq = curFreq - leftFreq;

			cur->left->freq = leftFreq;
			cur->right->freq = rightFreq;

			if(cur->prev)
			{
				int prevCount = hftSeqRec(cur->prev);
				if(prevCount==0)
				{
					if(cur->breakForLoop)
					{
						cur->breakForLoop = false;
						break;
					}
					else
					{
						cur->breakForLoop = true;
						continue;
					}
				}
				else
					count += prevCount;
			}
			else
			{
				cout <<cur->codeString <<":Error prev is null! We should not be here!" << endl;
			}
		}
	}
	else
	{
		if(cur->prev)
		{
			return hftSeqRec(cur->prev);
		}
		else
		{
			if(hftCheck())
				return 1;
			else
				return 0;
		}
	}

	return count;
}

int HFT::hftLevelCount()
{
	int count=0;

	for(int i=0;i<hftLevel.size();i++)
	{
		int iLevelSize = hftLevel[i].size();
		for(int j=0;j<iLevelSize;j++)
		{
			if(!hftLevel[i][j]->leaf)
			{
				int curFreq = hftLevel[i][j]->freq;
				int leftFreq = curFreq/2;
				int rightFreq = curFreq - leftFreq;

				hftLevel[i][j]->left->freq = leftFreq;
				hftLevel[i][j]->right->freq = rightFreq;
			}
		}
	}

	int check = hftLevelCheck();
	if(check==-1)
	{
		//printf("-1 returning 0\n");
		return 0;
	}

	count = hftSeqRec(root);

	return count;
}

int HFT::hftSetPrevNext()
{
	HFTNode* prev = NULL;
	HFTNode* cur = NULL;
	for(int i=hftLevel.size()-1;i>=0;--i)
	{
		for(int j=0;j<hftLevel[i].size();j++)
		{
			cur = hftLevel[i][j];

			if(!cur->left && !cur->right)
				cur->leaf = true;

			if((!cur->left && cur->right) || (cur->left && !cur->right))
				return -1; // incorect input huffman code resulted in incorrect huffman tree

			cur->prev = prev;

			if(prev)
				prev->next = cur;

			prev = cur;
		}
	}

	return 0;
};

void HFT::hftLevelSort()
{
	for(int i=1;i<hftLevel.size();i++)
	{
		sort(hftLevel[i].begin(),hftLevel[i].end(),sortLevels);
	}
};

void HFT::hftInsert(string s)
{
	//process string and insert nodes in tree
	int code =0;
	string codeString = "";
	HFTNode* curNode = root;
	for(int j=0;j<s.size();j++)
	{
		code = code << 1;

		if(s[j]=='1')
		{
			code = code | 1;
			if(curNode->right)
			{
				curNode = curNode->right;
			}
			else
			{
				HFTNode* temp = new HFTNode(code,0,s.substr(0,j+1),j+1);
				curNode->right = temp;
				temp->parent = curNode;
				curNode = temp;
				while(hftLevel.size()<(j+2))
					hftLevel.push_back(vector<HFTNode*>());

				hftLevel[j+1].push_back(temp);
			}
		}
		else
		{
			if(curNode->left)
			{
				curNode = curNode->left;
			}
			else
			{
				HFTNode* temp = new HFTNode(code,0,s.substr(0,j+1),j+1);
				curNode->left = temp;
				temp->parent = curNode;
				curNode = temp;
				while(hftLevel.size()<(j+2))
					hftLevel.push_back(vector<HFTNode*>());

				hftLevel[j+1].push_back(temp);
			}
		}
	}
};


int main() {

	int count = 0;
	int caseNum = 1;
	while(true){

		cin >> count;
		if(count == 0)
			break;

		HFT hft;

		for(int i=0;i<count;i++)
		{
			string s;
			cin >> s;
			hft.hftInsert(s);
		}
		hft.hftLevelSort();
		if(hft.hftSetPrevNext()==-1)
			cout << "Case "<< caseNum << ": Error. incorect input huffman code resulted in incorrect huffman tree!"  << endl;
		else
			cout << "Case "<< caseNum << ": " << hft.hftLevelCount() << endl;

		caseNum++;
	}

	return 0;
}
