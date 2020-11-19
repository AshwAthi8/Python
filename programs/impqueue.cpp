#include<iostream>
using namespace std;
class queue{
    int rear,front,capacity;
    int * arr;
    public:
    queue(int x);
    ~queue();
    bool enqueue(int x);
    int  dequeue();
    int frontq();
    void display();
};

queue::queue(int x){
    rear= -1;
    front =-1 ;
    capacity = x;
    arr = new int[x];
}
queue::~queue(){
    delete[] arr;
}
bool queue::enqueue(int x){
    if(rear >= capacity-1){
        cout<<rear<<endl;
        cout<<"Cannot add more"<<endl;
        return false;
    }
    if(rear==front && front==-1){
        front = front +1;
    }
    arr[++rear]=x;
    return true;
}

int queue::dequeue(){
    int k ;
    if(front==-1){
         cout<<"Empty queue "<<endl;
        return -1;
    }
    if(front<=rear){
    k = arr[front];
    front++;}
    else if(front-1==rear)
    {
     front = -1 ;
     rear = -1;
    }
    
    return k;
}

int queue::frontq(){
    if(rear==front && front==-1){
        cout<<"empty queue"<<endl;
        return -1;
    }
    return arr[front];
}

void queue::display(){
    for(int i =front;i<rear+1;i++){
        cout<<arr[i]<<"  ";
    }
    cout<<"\n";
}
int main(){
    queue qt(10);
    qt.dequeue();
    qt.enqueue(10);
    qt.enqueue(32);
    qt.enqueue(32);
    qt.display();
   // cout<<qt.dequeue()<<endl;


    return 0;
}