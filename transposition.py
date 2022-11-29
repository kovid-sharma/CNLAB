'''
#include<bits/stdc++.h>
using namespace std;
string to_bit(char x)
{
int a= x-'a';
string r="00000";
int i=4;
while(a)
{
if(a%2)
{
r[i]='1';
}
i--;
a/=2;
}
return r;
}
int main()
{
int ch;
cout<<"Enter the choice\n1 for encryption\n2 for decryption\n3 to exit\n";
cin>>ch;
while(ch!=3)
{
if(ch==1)
{
cout<<"Enter the text you want to encrypt\n";
string in;
cin>>in;
string sentence;
cout<<"Enter the encryption sentence of atleast "<<in.size()*5<<":
\n"; cin.ignore();
getline(cin,sentence);
string ans;
string x;
for(int i=0;i<sentence.size();i++)
{
if(sentence[i]==' ')
{
}
else
x.push_back(sentence[i]);
}
for(int i=0;i<in.size();i++)
{
ans+=to_bit(in[i]);
}
string out;
for(int i=0;i<ans.size();i++)
{
if(ans[i]=='1')
{
out+=(toupper(x[i]));
}
else
{
out+=(tolower(x[i]));
}
}
cout<<"The encrypted text is: "<<out<<endl;
}
else if(ch==2)
{
cout<<"Enter the encrypted message\n";
string en;
cin>>en;
if(en.size()%5!=0)
{
cout<<"This string was not encrypted\n";
}
else
{
string msg;
for(int i=0;i<en.size();i++)
{
if(isupper(en[i]))
en[i]='1';
else
en[i]='0';
}
for(int i=0;i<en.size();i+=5)
{
string new5;
for(int j=0;j<5;j++)
{
new5.push_back(en[i+j]);
}
long int num= stoi(new5,0,2);
msg.push_back(num+'a');
}
cout<<"Your message was:"<<msg<<endl;
}
}
cout<<"Enter the choice value again: \n";
cin>>ch;
}
return 0;
}
'''