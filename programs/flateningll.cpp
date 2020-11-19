#include<iostream>
using namespace std;
class Node {
public:
    int data;
    Node* prev;
    Node* next;
    Node* child;
};
    Node* flatten(Node* head) {
        Node *temp = head;
        while(temp!=NULL){
            if(temp->child!=NULL){
                Node *temp1 = temp->next;
                Node *temp2 = temp->child;
                while(temp2->next!=NULL){
                    temp2 = temp2->next;
                }
                temp->next = temp->child;
                temp->child->prev = temp;
                if(temp1!=NULL){
                    temp2->next=temp1;
                    temp1->prev = temp2;
                }
                temp->child = NULL;
                
            }
            
                 temp=temp->next;
            
        }
        return head;
    }



void printll(Node* curr){
    while(curr!=NULL){
        cout<<curr->data<<" ";
        curr = curr->next;
    }
    cout<<"\n";
}
void insertval(Node** curr,int val){
    Node* temp = new Node();
    temp->data = val;
    temp->next = NULL;
    temp->child = NULL;
    temp->prev = NULL;
    if(*curr==NULL){
        *curr = temp;

    }
    else{
        Node* lastn = *curr;
        Node* penul = *curr;
        while(lastn->next!=NULL){
            penul = lastn;
            lastn=lastn->next;

        }
        lastn->prev = penul;
        lastn->next = temp;
    }
    return;
}

int main(){
    Node * head =NULL;
    insertval(&head,5);
    insertval(&(head->next),6);
    insertval(&(head->next->next),15);
    insertval(&(head->child),10);
    insertval(&(head->child->child),16);
    
    printll(flatten(head));


    return 0;
}


