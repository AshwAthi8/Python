#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* prev;
    Node* next;
    Node(int x){
        prev = NULL;
        next = NULL;
        data =x;
    }
};
class Dequeue{

 Node* head;
 Node* tail; 
 int size;
    public:
    Dequeue(){
        head = NULL;
        tail = NULL;
        size =0;
    }
    void insert_front(int x);
    void insert_back(int x);
    void del_front();
    void del_back();
    int get_size();
    bool isEmpty();
    void earse();
    int get_front();
    int get_back();
    void display();
};
void Dequeue::insert_front(int x){
    Node *newnode = new Node(x);
    if(head==NULL){
        head = tail = newnode;
    }
    newnode->next = head;
    head->prev = newnode;
    head = newnode;
    size = size +1;
}

void Dequeue::insert_back(int x){
    Node *newnode = new Node(x);
    if(tail==NULL){
        head = tail = newnode;
    }
    
    tail->next = newnode;
    newnode->prev = tail;
    tail = newnode; 
    size = size +1;    
}
void Dequeue::del_front( ){
    if(isEmpty()){
        cout<<"underflow"<<endl;
        return;
    }
    head = head->next;
    head->prev = NULL;
    size = size -1;
    return ;
    
}
void Dequeue::del_back( ){
    if(isEmpty()){
        cout<<"underflow"<<endl;
        return;
    }
    tail = tail->prev;
    tail->next = NULL;
    size = size -1; 
    
}
int Dequeue::get_size(){
    return size;
}
int Dequeue::get_front(){
    if(isEmpty()){
        cout<<"underflow"<<endl;
       return -1;
    }
    return head->data;
}
int Dequeue::get_back(){
      if(isEmpty()){
        cout<<"underflow"<<endl;
       return -1;
    }
    return tail->data;
}
bool Dequeue::isEmpty(){
    if(size==0){
        return true;
    }
    return false;
}

void Dequeue::display(){
    if(isEmpty()){
        cout<<"Dequeuq is emppty;"<<endl;
        return;
    }
    Node *temp = head;
    while(temp!=tail){
        cout<<temp->data<<"\t";
        temp=temp->next;
    }
    cout<<temp->data<<"\t";
    cout<<endl;
return;
}
int main(){
    Dequeue *dq = new Dequeue();
    dq->del_front();
    dq->insert_front(4);
    dq->insert_front(5);
    dq->insert_front(9);
    dq->insert_back(10);
    dq->display();
    return 0;
 
}