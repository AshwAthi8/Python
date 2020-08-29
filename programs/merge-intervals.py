def merge(intervals):
        out = [[-1,-1]]
        t=[]
        size = len(intervals)
        if(size == 1 or size == 0):
            return intervals
        i=0
        j=0
        intervals.sort()
        '''
        if(intervals[i][1]>=intervals[i+1][0]):
            t.append(min(intervals[i][0],intervals[i+1][0]))
            t.append(max(intervals[i][1],intervals[i+1][1]))
            out.append(t)
        else:
            t = (intervals[i])
            out.append(t)
        '''
        
        t=[]
        while(i<size):
            #print(i,j,out,intervals)
            if(out[j][1]>=intervals[i][0]):
                t.append(min(intervals[i][0],out[j][0]))
                t.append(max(intervals[i][1],out[j][1]))
                if(out[j][1]<intervals[i][1]):
                    out[j]=(t)
            else:
                out.append(intervals[i])
                j=j+1
            t=[]
            i=i+1
        if(out[0] == [-1,-1]):
            out.remove([-1,-1])
        return out

                    
print(merge([[1,4],[0,0],[2,3],[6,7]]))  


'''
i=0
size = len(intervals)
        intervals.sort()
        print(intervals)
        while(i < size-1):
            if(intervals[i][1]>=intervals[i+1][0]):
                t.append(min(intervals[i][0],intervals[i+1][0]))
                t.append(max(intervals[i+1][1],intervals[i][1]))
                out.append(t)
                i=i+1
            else:
                out.append(intervals[i])
            i=i+1
            t=[]
        if(i==size):
            return out
        elif(size==1):
            return intervals 
        elif(i==size-1 and out[-1][1]>=intervals[i][0]):
            t.append(min(intervals[i][0],out[-1][0]))
            t.append(max(out[-1][1],intervals[i][1]))
            out[-1] = (t)
            return out
        else:
            out.append(intervals[i])
            return out
            
        '''
    