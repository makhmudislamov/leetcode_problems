# Given a bag with 100 balls simulate choosing the a ball randomly each time and discard the choosen ball.


# populate array - 1-100
# while size > 0:
# random_ball_ind = random.randint(0, arrsize-1)
# pop(random_ball_ind)

import random
def random_balls(balls):

    end_pointer = len(balls) - 1

    while end_pointer >= 0:
        random_inx = random.randint(0, end_pointer)
        print(balls[random_inx])
        balls[random_inx], balls[end_pointer] = balls[end_pointer], balls[random_inx]
        end_pointer -= 1

balls = []
for i in range(1, 11):
    balls.append(i)

print(balls)

random_balls(balls)