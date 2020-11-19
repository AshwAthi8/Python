#include<iostream>
#include<list>
using namespace std;
class graph{
int ver;
list<int> *adj;
    public:
    graph(int x);
    void addedge(int ,int);
    void BFS(int );
};

graph::graph(int x)
{
    ver = x;
    adj = new list<int>[x];

}

void graph::addedge(int sr,int des){
    adj[sr].push_back(des);
}
void graph::BFS(int s){
    bool *visited = new bool[ver];
    for(int i=0;i<ver;i++){
        visited[i]=false;
    }
    list<int> queue;
    visited[s]=true;
    queue.push_back(s);

    list<int>::iterator i;
    while(!queue.empty()){
        s = queue.front();
        cout<<s<< " ";
        queue.pop_front();
        for (i=adj[s].begin();i!=adj[s].end();i++){
            if(!visited[*i]){
                visited[*i]=true;
                queue.push_back(*i);
            }
        }
    }
}

int main(){
    graph g(4);
    g.addedge(0,1);
    g.addedge(0,2);
    g.addedge(1,2);
    g.addedge(2,0);
    g.addedge(2,3);
    g.addedge(3,3);

    g.BFS(2);
    return 0;
}

