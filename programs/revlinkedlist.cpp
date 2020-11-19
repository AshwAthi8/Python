#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node * next;
};

void revlsit(Node** head){
    Node* current = *head;
    Node* prev = NULL;
    Node* nextN = NULL;
    while(current!=NULL){
        //cout<<current->data<<"\n";
        nextN = current->next;
        current->next = prev;
        prev = current;
        current = nextN;
        
    }
    *head = prev;
}

void printlist(Node* n){
    while(n!=NULL){
        cout<< n->data << " ";
        n=n->next;
    }
    cout<< "\n";
}
void insertNode(Node** head,int value){
    Node* temp = new Node();
    temp->data = value;
    temp->next = NULL;
    if(*head==NULL){
        *head = temp;
            return;
    }
    else{
        Node* lastN = *head;
        while(lastN->next != NULL){
           lastN = lastN->next; 
        }
    
    lastN->next = temp;
    return;
}
}

int main(){
    Node* head = NULL;
    insertNode(&head,1);
    insertNode(&head,2);
    insertNode(&head,3);
    insertNode(&head,4);
    //insertNode(&head,5);

    printlist(head);
    revlsit(&head);
    cout<<"Reversed Linked list"<<"\n";
    printlist(head);
    return 0;
}