#include<stdio.h>
#include <stdlib.h>
int main()
{
int i,len,odd=0,even=0;
char s[20];
gets(s);
len=strlen(s);
for(i=0;i<len;i++)
{
if(i%2==0)
{
odd+=s[i];
}
else
{
even+=s[i];
}}
printf("%d\n",abs(even-odd));
return 0;
}
