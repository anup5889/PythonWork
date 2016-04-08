"""
public boolean isSameTree(TreeNode p, TreeNode q) 
{
    if(p==null && q==null)
    {
        return true;
    }
    else if(p==null || q==null)
    {   
        return false;
    }
    else
    {
        return (p.val == q.val && 
                isSameTree(p.left,q.left) && 
                isSameTree(p.right,q.right));
    }
}
"""

def isSameTree(p,q):
    if(p==Null and q==null):
        return true
    elif(p==null or q==null):
        return false
    else:
        return(p.val==q.val and
            isSameTree(p.left,q.left)and
            isSameTree(p.right, q.right))



