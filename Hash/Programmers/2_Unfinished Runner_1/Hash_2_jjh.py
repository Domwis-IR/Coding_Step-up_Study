def solution(participant, completion):
    participant.sort()
    completion.sort()
    while completion:
        if participant[-1] == completion[-1]:
            participant.pop()
            completion.pop()
        else:
            return participant[-1]
    if participant:
        return participant[0]
    return ""
 
