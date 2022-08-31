from re import L
import sys

class LOC():
    """_summary_: Line of Code Matrix Measurement
    """
    def __init__(self, file) -> None:
        """Initialization for the LOC metrics.
        """
        self.file = file
        self.singleline_comment_operator = "#"
        self.multiline_comment_start_operator = "'''"
        self.multiline_comment_end_operator = "'''"
        self.line_Count = 0
        self.total_BlankLine_Count = 0
        self.total_CommentLine_Count = 0
        self.total_code_line_count = 0

    def filter_code_lines(self):
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


    def Compute(self):
        with open(self.file, 'r') as f:
            for line in f:
                self.line_Count += 1
                line_without_whitespace = line.strip()
                if not line_without_whitespace:
                    self.total_BlankLine_Count += 1
        code_lines = self.filter_code_lines()
        self.total_code_line_count = len(code_lines)
        self.total_CommentLine_Count = self.line_Count - (self.total_BlankLine_Count+self.total_code_line_count)

    def display_metrics(self):
        self.Compute()
        print('\t\t------LOC------\t\t')
        print('Total Lines:\t\t\t' + str(self.line_Count))
        print('Total Blank lines:\t\t' + str(self.total_BlankLine_Count))
        print('Total Comment lines:\t\t' + str(self.total_CommentLine_Count))
        print('Total Code lines:\t\t' + str(self.total_code_line_count))



if __name__ == "__main__":
    file = sys.argv[-1]
    loc = LOC(file)
    loc.display_metrics()

                


    


    