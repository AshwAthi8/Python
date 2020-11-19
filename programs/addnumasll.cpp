#include<iostream>
using namespace std;
class Node{
    public:
        int data;
        Node* next;
};

void inserttell(Node** head,int val){
    Node* temp = new Node();
    temp->data = val;
    temp->next = NULL;

    if(*head==NULL){
        *head=temp;
    }
    else{
        Node* laston = *head;
        while(laston->next !=NULL){
            laston=laston->next;
        }
        laston->next = temp;
    }
      return;
}
Node* addll(Node* a,Node* b){
    Node* sumnum = NULL;

    int sum,carry=0;
    while(a!=NULL || b!=NULL){
        sum = carry + ((a!=NULL)?a->data:0)+((b!=NULL)?b->data:0);
        carry =(sum>=10)?1:0;
        sum = sum%10;
        //cout<<sum<<"<< \n";
        inserttell(&sumnum,sum);
        if(a!=NULL){
            a=a->next;
        }
        if(b!=NULL){
            b=b->next;
        }
    }
    if(carry>0){
        inserttell(&sumnum,1);
    }
    return sumnum;
}


void printll(Node * curr){
    while(curr!=NULL){
        cout<<curr->data<<" ";
        curr=curr->next;
    }
    cout<<"\n";
}

int main(){
    Node* head =NULL;
    inserttell(&head,1);
    inserttell(&head,2);
   // inserttell(&head,9);
    printll(head);
    Node* head1 =NULL;
    inserttell(&head1,4);
    inserttell(&head1,6);
    inserttell(&head1,1);
    printll(head1);
    Node* res = addll(head1,head);
    printll(res);
    

    return 0;
}