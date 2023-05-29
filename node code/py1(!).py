











def DeleteElementAt(self,position):
    if position == 0:
        return self.head.next 
    else:
    
        CurrentNode = self.head 
        for i in range(position-1):
            current = current.next.next
            