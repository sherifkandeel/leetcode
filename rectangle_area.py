class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        if C<E or G<A:
            return (D-B)*(C-A) + (G-E)*(H-F)
        if H<B or D<F:
            return (D-B)*(C-A) + (G-E)*(H-F)
        right = min(C,G)
        left = max(A,E)
        top = min(H,D)
        bottom = max(F,B)
        return (G-E)*(H-F) + (C-A)*(D-B) - (right-left)*(top-bottom)
        
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
