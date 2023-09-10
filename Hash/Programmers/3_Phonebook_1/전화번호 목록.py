# def solution(phone_book): 효율성 테스트 실패
#     score=0
#     for i in phone_book:
#         for j in phone_book:
#             if i == j[:len(i)]:
#                 score += 1
#     if score > len(phone_book):
#         return False
#     else:
#         return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True