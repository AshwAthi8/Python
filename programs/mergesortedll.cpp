#include<iostream>

using namespace std;

class Node{
    public:
    int data;
    Node * next;
};

void printll(Node * curr){
  //  Node* curr = head;
    while(curr!= NULL ){
        cout<<curr->data<<" ";
        curr = curr->next;
    }
cout<<"\n";
}

/*
void addnode(Node** des, Node** source){
    Node* newnode = *source;
    *source = newnode->next;

    *des = newnode;

}*/

void insertvl(Node** n,int val){
    Node* temp = new Node();
    temp->data = val;
    temp->next = NULL;
    if(*n == NULL){
        *n = temp;
        return;
    }
    else{
        Node* laston = *n;
        while(laston->next != NULL){
            laston=laston->next;
        }
        laston->next = temp;
    }
    return;
}
Node* mergelist(Node* a, Node* b){
    Node dummy;
    Node* tail = &dummy;
    dummy.next = NULL;
    while(1){
        if(a==NULL){
            tail->next = b;
            break;
        }
        else if(b==NULL){
            tail->next = a;
            break;
        }
        if(a->data <= b->data){
            tail->next = a;
            a=a->next;
            //addnode(&(tail->next),&a);

        }
        else{
            tail->next = b;
            b=b->next;
            //addnode(&(tail->next),&b);
        }
        tail = tail->next;
    }

    return (dummy.next);
/*
    while(a!=NULL || b!=NULL){
        if(a->data >= b->data){
            tail->next = b;
            b=b->next;
        }
        else{
            tail-next = a;
            a=a->next;
        }
        cout<<tail->data<<"\n";
        tail=tail->next;
    }
    
    if(a!=NULL){
        while(a!=NULL){
            tail = a;
            a=a->next;
            cout<<tail->data<<"\n";
            tail=tail->next;
        }
     tail = a;   
    }
    if(b!=NULL){
       while(b!=NULL){
            tail = b;
            b=b->next;
            cout<<tail->data<<"\n";
            tail=tail->next;
        }
    }
    tail->next = NULL;
    return dummy.next;*/

}


int main(){
    Node* head1 = NULL;
    Node* head2 = NULL;
    insertvl(&head1,1);
    insertvl(&head1,5);
    insertvl(&head1,9);
    insertvl(&head1,10);
    insertvl(&head1,22);

    insertvl(&head2,0);
    insertvl(&head2,4);
    insertvl(&head2,9);
    printll(head1);
    printll(head2);
    Node * res = mergelist(head1,head2);
    printll(res);


    return 0;
}