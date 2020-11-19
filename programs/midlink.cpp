#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node * next;
};

void midvalue(Node** n){
    Node* fastPtr = *n;
    Node* slowPtr = *n;

    while(fastPtr->next!= NULL && slowPtr!=NULL){
        fastPtr = fastPtr->next->next;
        slowPtr = slowPtr->next;
       // cout<<slowPtr->data<<"\n";
    }
    cout<<"Mid value is "<<slowPtr->data;
return;
}

void pushval(Node** n, int val){
    Node* temp = new Node();
    temp->data = val;
    temp->next = NULL;
    if(*n == NULL){
        *n = temp;
        return;
    }
    else{
        Node* lastone = *n;
        while(lastone->next!=NULL){
            lastone=lastone->next;
        }
        lastone->next = temp;
    }
    return;
}
void printll(Node* curr){
    while(curr!=NULL){
       // cout<<curr->data<<"\n";
        curr=curr->next;
    }
}


int main(){
    Node* head = NULL;
    pushval(&head,1);
    pushval(&head,2);
    pushval(&head,3);
    pushval(&head,4);
    pushval(&head,5);
    pushval(&head,6);
    pushval(&head,7);
    printll(head);
    midvalue(&head);
    return 0 ;
}