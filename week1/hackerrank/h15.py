def count_substring(string, sub_string):
    count=0
    #print(len(string),len(sub_string))
    for i in range(0, len(string)-len(sub_string)+1):
        if string[i] == sub_string[0]:
            done=1
            for j in range (0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    done=0
                    break
            if done==1:
                count += 1
    return count