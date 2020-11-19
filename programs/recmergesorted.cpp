#include<iostream>
using namespace std;
class Node{
    public:
    int data;
    Node* next;
};
Node* merge(Node* a,Node* b){
    if(a==NULL){
        return b;
    }
    else if(b==NULL){
        return a;
    }
    if(a->data <= b->data){
         a->next = merge(a->next,b);
         return a;
    }
    else{
        b->next = merge(a,b->next);
        return b;
    }
}

void printld(Node* curr){
    while(curr!=NULL){
        cout<<curr->data<<" ";
        curr = curr->next;
    }
    cout<<"\n";
}
void insertelement(Node** n,int val){
    Node* temp = new Node();
    temp->data = val;
    temp->next = NULL;
    if(*n==NULL){
        *n = temp;
        //cout<<" Binchonaa \n";
        return;
    }
    else{
        Node* curr = *n;
        while(curr->next!=NULL){
            curr = curr->next;
        }
        curr->next = temp;
    }
    
}
int main()
{

    Node* head1 = NULL;
    Node* head2 = NULL;
    
    insertelement(&head1,1);
    insertelement(&head1,2);
    insertelement(&head1,4);
    insertelement(&head1,9);
    insertelement(&head2,1);
    insertelement(&head2,2);
    insertelement(&head2,10);
    insertelement(&head2,22);

    printld(head1);
    printld(head2);
    Node* res = merge(head1,head2);
    printld(res); 
    return 0;
}