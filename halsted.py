import sys
import math
from cofig import get_python_operators, get_python_operands

		
class HalsteadMetric:
    """ Compute various HalsteadMetric metrics. """

    def __init__( self, file_name):
        """ Initialization for the HalsteadMetric metrics."""
        self.file = file_name
        self.unique_operators = get_python_operators()
        self.unique_operands = get_python_operands()
        self.singleline_comment_operator = "#"
        self.multiline_comment_start_operator = "'''"
        self.multiline_comment_end_operator = "'''"
        self.n1 = {}
        self.n2 = {}


    def filter_token(self, token):
        tok = token
        while tok:
            # print(tok)
            tok = self.break_token(tok) 


    def break_token(self, token):
        op_pos = len(token)
        for op in self.unique_operators:
            if token.startswith(op):
                self.n1[op] = self.n1.get(op, 0) + 1
                return token[len(op):]
            if op in token:
                op_pos = min(op_pos, token.find(op))

        remaining_token = token[:op_pos]
        for keyword in self.unique_operands:
            if remaining_token == keyword:
                self.n2[op] = self.n2.get(op, 0) + 1

        self.n2[remaining_token] = self.n2.get(op, 0) + 1
        return token[op_pos:]

    def __LOGb( self, x, b ): 
        """ convert to LOGb(x) from natural logs."""
        try:
            result = math.log( x ) / math.log ( b )
        except OverflowError:
            result = 1.0
        return result

    def measure_halstead(self, N1, N2, n1, n2):
        Vocabulary = n1 + n2
        Volume = (N1 + N2) * self.__LOGb(Vocabulary, 2)
        Difficulty = ((n1 / 2) * (N2 / n2))
        Effort = Difficulty * Volume

        print("Vocabulary: ", Vocabulary)
        print("Volume: ", Volume)
        print("Difficulty: ", Difficulty)
        print("Effort: ", Effort)

    
    def filter_comments(self):
        singleline_comment_operator_pos = -1
        multiline_comment_start_operator_pos = -1
        multiline_comment_end_operator_pos = -1
        filtered_lines = []
        inside_comment = False
        with open(self.file, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                if self.singleline_comment_operator in line:
                    singleline_comment_operator_pos = line.find(self.singleline_comment_operator)
                if self.multiline_comment_start_operator in line:
                    multiline_comment_start_operator_pos = line.find(self.multiline_comment_start_operator)
                if self.multiline_comment_end_operator in line:
                    multiline_comment_end_operator_pos = line.find(self.multiline_comment_end_operator)

                if not inside_comment and singleline_comment_operator_pos != -1:
                    line = line[:singleline_comment_operator_pos].strip()
                    if line:
                        filtered_lines.append(line)
                elif inside_comment and multiline_comment_end_operator_pos != -1:
                    inside_comment = False
                elif multiline_comment_start_operator_pos != -1:
                    inside_comment = True
                elif inside_comment:
                    inside_comment = True
                else:
                    line = line.strip()
                    if line:
                        filtered_lines.append(line)

                singleline_comment_operator_pos = -1
                multiline_comment_start_operator_pos = -1
                multiline_comment_end_operator_pos = -1

        return filtered_lines


    def display_matrix(self):
        src_code = self.filter_comments()
        for line in src_code:
            tokens = line.split()
            for token in tokens:
                self.filter_token(token)
        print('\t\t------n1(Operators)-----\t\t\n')
        for key, value in self.n1.items():
            print(key + " = " + str(value))
        print('\t\t------n2(Operands)------\t\t\n')
        for key, value in self.n2.items():
            print(key + " = " + str(value))

        self.measure_halstead(sum(self.n1.values()),
                             sum(self.n2.values()), 
                             len(self.n1), len(self.n2))



if __name__ == "__main__":
    file = sys.argv[-1]
    halstead_mat = HalsteadMetric(file)
    halstead_mat.display_matrix()