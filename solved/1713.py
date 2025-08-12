from sys import stdin  

N = int(stdin.readline().strip())
r_cnt = int(stdin.readline().strip())
if r_cnt > 0:
    r_student = list(map(int,stdin.readline().strip().split()))
    r_status = [0]*101

    frame = []
    for i in range(r_cnt):
        r_status[r_student[i]]+=1

        if r_student[i] in frame:
            continue

        if len(frame) < N:
            frame.append(r_student[i])
            continue

        m_student_cnt = 1001
        for k,j in enumerate(frame):
            if m_student_cnt > r_status[j]:
                m_student = j
                m_student_cnt = r_status[j]
                change_loc = k

        del frame[change_loc]
        frame.append(r_student[i])
        r_status[m_student] = 0

    print(*sorted(frame))
