class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # if we could have an array that keep track of the row and
        # colum to be transfer to 0
        #  - - -
        #- 0 2 3  
        #- 4 0 6 
        #- 7 8 9

        # if we go from the left to right, top to bottom, we can mark directly 
        # to the matrix at the first row and second row
        # except, we need to create an extra cell that hold the very first element of the matrid
        # why, because, we need to 1) transfer the other row, col > 1 first, then zeros


        ROWS, COLS = len(matrix), len(matrix[0])

        firstElement = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstElement = True
        

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if firstElement:
            for c in range(COLS):
                matrix[0][c] = 0

        