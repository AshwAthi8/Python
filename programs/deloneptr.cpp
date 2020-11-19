#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
};

void printll(Node *curr){
    while(curr!=NULL){
        cout<<curr->data<<" ";
        curr = curr->next;
    }
    cout<<"\n";
}
void insertll(Node ** head,int val){
    Node* temp = new Node();
    temp->data=val;
    temp->next = NULL;
    if(*head==NULL){
        *head=temp;
    }
    else{
        Node* lastnode = *head;
        while(lastnode->next!=NULL){
            lastnode=lastnode->next;
        }
        lastnode->next=temp;
    }
    return;
}

void delNode(Node * delno){
    if(delno->next==NULL){
        free(delno);
    }
    else{
        Node* temp = delno->next;
        delno->data=temp->data;
        delno->next=temp->next;
        free(temp); 
    }
    return;
}

int main(){
    Node* head = NULL;
    insertll(&head,1);
    insertll(&head,2);
    insertll(&head,3);
    insertll(&head,4);
    printll(head);
    delNode(head->next);
    printll(head);

}