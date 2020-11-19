#include<iostream>
using namespace std;
class stack{
    int *arr;
    int top;
    int capacity;
    public:
        stack(int x);
        ~stack();
        bool push(char x);
        char pop();
        char peek();
        bool isEmpty();
        bool isFull();
};
stack::stack(int x){
    arr = new int[x];
    capacity = x;
    top = -1;
}
stack::~stack(){
    delete[] arr;
}

bool stack::isFull(){
    if(top>=capacity-1){
        cout<<top<<endl;
        return true;
    }
    return false;
}

bool stack::isEmpty(){
    if(top==-1){
        return true;
    }
    return false;
}

bool stack::push(char x){
    if(isFull()){
        cout<<"Stack overflow"<<endl;
        return false;
    }
    else{
        arr[++top]=x;
    }
    return true;
  
}
char stack::pop(){
    if(isEmpty()){
        cout<<"stack underflow\n"<< endl;
        return 0;
    }
    else{
        int temp = arr[top];
        top = top -1;
        return temp;
    }

}

char stack::peek(){
    if(isEmpty())
    {
        cout<<"stack underflow\n"<<endl;
        return 0;
    }
   return arr[top];
}

string matching(string st){
    stack c(st.size()+1);
    int i = 0;
    char k ;

    while(i<st.length()){
        k = st[i];
        //cout<<k<<endl;
        switch(k){
        case '{': 
            {c.push(k);
             break;}
        case '(': 
            {c.push(k);
             break;}
        case '[': 
            {c.push(k);
            break;}
            
        case '}':
        {
            if(c.isEmpty() || c.peek()!= '{' ){
                return "NO";
            }
            else{
                c.pop();
                break;
            }
        }
        case ']':
        {
            if(c.isEmpty() || c.peek()!= '[' ){
                return "NO";
            }
            else{
                c.pop();
                break;
            }
        }
        case ')':
        {
            if(c.isEmpty() || c.peek()!= '(' ){
                return "NO";
            }
            else{
                c.pop();
                break;
            }
        }

    }
    k = st[i];
    i=i+1;
    }
    if(c.isEmpty()){
    return "YES";}
    return "NO";

}

int main(){
    string in ; 
    cin >> in;
    cout<< matching(in)<<endl;
    return 0;
}