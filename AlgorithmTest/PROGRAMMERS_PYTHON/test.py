def solution(money, costs):
    answer = 300000
    moneys=[1, 5, 10, 50, 100, 500]
    table = [[i, j] for i, j in zip(moneys, costs)]
    table.reverse()
    
    for i, v in enumerate(table):
        f1 = money//v[0]
        if f1 == 0:
            continue
        print('table', v)
        print('f1', v[0], f1)
        while True:
            cost=0
            last = money - (v[0]*f1)
            cost += v[1] * f1
            print('last, v, cost, total', last, v[1], v[1] * f1, cost)
            for j in table[i+1:]:
                f2 = last//j[0]
                if f2==0:
                    continue
                print('f2', j[0], f2)
                last -= (j[0] * f2)
                cost+= j[1] * f2
                print('last, j, cost, total', last, j[1], j[1] * f2, cost)
                if last == 0 or cost >= answer:
                    break
            if last == 0 and cost < answer:
                answer = cost
                print('answer', answer)
            if f1 == 0:
                break
            
            f1 -= 1
            print(f1, '='*30)
        break
    return answer


print(solution(4578, [1,4,99,35,50,1000]))