"""
This is the implementation of Levenshtein distance algorithm.

Usage: levenshtein_distance().of("apple","banana")

Author: Prakash
Github: https://github.com/ppml38/levenshtein_distance
This code is licensed under a permissive MIT license -- see LICENSE.txt.
"""

__all__ = ['levenshtein_distance']

__version__ = '1.1'

class data:
    def __init__(self, input_data):
        self.data_piece = input_data
        self.length = len(self.data_piece)
    def get(self, i):
        return self.data_piece[i]

class dp_table:
    def __init__(self, data_a, data_b):
        self.data_a=data_a
        self.data_b=data_b
        self.no_of_rows=data_b.length+1
        self.no_of_columns=data_a.length+1
        self._dp_table=[]
        for _ in range(self.no_of_rows):
            self._dp_table.append([0]*(self.no_of_columns))
        self._populate_distance()

    def _populate_distance(self):
        for i in range(self.no_of_columns):
            self._dp_table[0][i]=i
        for j in range(self.no_of_rows):
            self._dp_table[j][0]=j

        for i in range(0,self.data_b.length):
            for j in range(0,self.data_a.length):
                if self.data_a.get(j)==self.data_b.get(i):
                    self._dp_table[i+1][j+1]=self._dp_table[i][j]
                else:
                    self._dp_table[i+1][j+1]=min(self._dp_table[i][j+1],self._dp_table[i+1][j],self._dp_table[i][j])+1
    def get_distance(self):
        return self._dp_table[self.data_b.length][self.data_a.length]

class levenshtein_distance:

    def __init__(self):
        self.of = self._calculate_distance

    def _calculate_distance(self, input_a: str,input_b: str) -> int:
        distance_table = dp_table(data(input_a),data(input_b))
        return distance_table.get_distance()
