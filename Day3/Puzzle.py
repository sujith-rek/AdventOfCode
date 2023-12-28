part_sum = 0

symbols = ['*', '/', '$', '+', '&', '@', '#', '%', '=', '-']

lines = []
with open('input.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    line_num = lines.index(line)
    num = ''
    st = 0
    ed = 0
    cur_index = 0
    for char in line:
        if char == '.':
            if num != '':

                for i in range(st, ed):

                    if ((lines[line_num][i] in symbols) or
                        (i-1 >= 0 and lines[line_num][i-1] in symbols) or
                        (i+1 < len(lines[line_num]) and lines[line_num][i+1] in symbols) or
                        (line_num-1 >= 0 and lines[line_num-1][i] in symbols) or
                        (line_num-1 >= 0 and i-1 >= 0 and lines[line_num-1][i-1] in symbols) or
                        (line_num-1 >= 0 and i+1 < len(lines[line_num]) and lines[line_num-1][i+1] in symbols) or
                        (line_num+1 < len(lines) and lines[line_num+1][i] in symbols) or
                        (line_num+1 < len(lines) and i-1 >= 0 and lines[line_num+1][i-1] in symbols) or
                        (line_num+1 < len(lines) and i+1 < len(lines[line_num]) and lines[line_num+1][i+1] in symbols)):

                        
                        part_sum += int(num)
                        lines[line_num] = lines[line_num][:st] + '.' * (ed - st) + lines[line_num][ed:]
                        break

                num = ''
                st = 0
                ed = 0

                
            else:
                continue
        
        elif char.isdigit():
            if num == '':
                st = cur_index
            num += char
            ed = cur_index + 1
        
        cur_index += 1
            
    
print(part_sum)
