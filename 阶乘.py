def search(q,w,e,r):
        if e==r:
                assert w==q[r]
                return r
        else:
                middle=(e+r)//2
                if w>q[middle]:
                        return search(q,w,middle+1,r)
                else:
                        return search(q,w,e,r)
