#!/usr/bin/env python3
def age_convert():
    # 儿子刚出身时母亲的年龄
    for mom_age_start in range(18, 50):
        count = 0
        son_age_temp = 0
        mom_age_temp = mom_age_start
        while True:
            # 年龄100以上不会出现年龄相反的巧合
            if mom_age_temp >= 100:
                break

			# 考虑了妈妈20岁时宝宝02岁
            mom_age_convert = int(str(mom_age_temp)[::-1])
            # 发生巧合
            if son_age_temp == mom_age_convert:
                count = count + 1
                # 6次巧合时是儿子现在的年龄
                # 之前没有放在if里面,已修复bug
                if count == 6:
                    son_now_age = son_age_temp

            mom_age_temp = mom_age_temp + 1
            son_age_temp = son_age_temp + 1

        if count == 8:
            print('Nowadays the son\'s age is: %d' % son_now_age)
            print('The women was became mom at %d years old' % mom_age_start)


if __name__ == '__main__':
    age_convert()
