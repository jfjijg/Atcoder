N = int(input()) #水を足す回数

T_list = [] #現在の時間
V_list = [] #水を足す量

#現在の時間と水量をリストに入れる
for i in range(N):
    T, V = map(int, input().split())
    T_list.append(T)
    V_list.append(V)

#水が漏れた量のリスト
water_diff_list = []
for x in range(N - 1):
    water_diff =  T_list[x + 1] - T_list[x]
    water_diff_list.append(water_diff)

#水量の初期値を設定
current_water = V_list[0]

#
for n in range(N - 1):
    pre_water = current_water - water_diff_list[n]
    #水量は常に正
    if pre_water <= 0:
        prewarter = 0
    current_water = pre_water + V_list[n + 1]

print(current_water)

print("大変よくできました。")
    
print("大変よくできました。")


    
