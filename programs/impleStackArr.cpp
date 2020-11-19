#include<iostream>
using namespace std;
#define SIZE 10
class stack{
    int *arr;
    int top;
    int capacity;
    public:
        stack(int);
        ~stack();
        bool push(int y);
        int pop();
        int peek();
        bool isEmpty();
        bool isFull();

};
//comstructor
stack::stack(int x){
    arr = new int[x];
    capacity = x;
    top = -1;
}

stack::~stack(){
    delete[] &arr;
}
bool stack::isEmpty(){
    if(top == -1){
        return true;
    }
    else{
        return false;
    }
}
bool stack::isFull(){
    if(top>=capacity-1){
        return true;
    }
    else{
    return false;
    }
}

bool stack::push(int x){
    if(isFull()){
        cout<<"Stack overflow!!"<<endl;
        return false;}
    else{
        ++top;
        cout<< top<<endl;
        arr[top]=x;
        cout<<arr[top]<<endl;
        return true;}
}
int stack::pop(){
    if(isEmpty()){
        cout<<"Stack underflow!!"<<endl;
        return 0;
    }
    else{
        int temp = arr[top];
        top = top -1;
        return temp;
    }
}

int stack::peek(){
    if(isEmpty()){
        cout<<"Stack underflow!!"<<endl;
        return 0;
    }
    else{
   return arr[top];
    }
}

int main(){
    stack s(5);
    s.push(2);
//     stack *st = new stack();
//    // st(10);
//     st->push(1);
    //st.push(2);
    //st.push(3);
    //cout<<st.pop()<<endl;

    return 1;
}