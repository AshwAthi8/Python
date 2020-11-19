#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
};

Node* klast(Node* curr,int k){
    Node* refptr = curr;
    Node* mainptr = curr;
    int c=0;
    while(c<k && refptr!=NULL){
        refptr=refptr->next;
        c=c+1;
    }
    if(refptr==NULL){
        return mainptr;
    }
    else{
        while(refptr!=NULL){
            mainptr=mainptr->next;
            refptr=refptr->next;
        }
    }
    return mainptr;

}
void printll(Node* curr){
    while(curr!=NULL){
        cout<<curr->data<<" ";
        curr = curr->next;
    }
cout<<"\n";
}

void insertval(Node* n,int val){
    Node* temp = new Node();
    temp->data = val;
    temp->next = NULL;
    if(n==NULL){
        n=temp;
    }
    else{
        Node* lastnode = n;
        while(lastnode->next!=NULL){
            lastnode=lastnode->next;
        } 
        lastnode->next = temp;
    }
    return;

}
int main(){
    Node* head = NULL;
    insertval(head,1);
    insertval(head,2);
    insertval(head,3);
    insertval(head,4);
    insertval(head,5);
    insertval(head,6);
    printll(head);
    Node* res = klast(head,3);
    cout<<"K the element from last is "<<res->data<<"\n";
    return 0;
}

/*
Node* insert(Node *head,int data)
      { Node** curr = &head;
        Node* temp = new Node(data);
        temp->next=NULL;
        if(*curr==NULL){
            *curr=temp;
        }
        else{
            Node *lastone = *curr;
            while(lastone->next!=NULL){
                lastone=lastone->next;
            }
            lastone->next=temp;
        }
        return head;
      }
*/