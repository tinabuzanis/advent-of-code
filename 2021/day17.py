def simulate(x_vel, y_vel, target_x_min, target_x_max, target_y_min, target_y_max):
  x = 0
  y = 0
  max_y = 0
  while True:
    x += x_vel
    y += y_vel
    max_y = max(max_y, y)
    x_vel = max(x_vel-1, 0)
    y_vel -= 1
    if target_x_min <= x <= target_x_max and target_y_min <= y <= target_y_max:
      max_h.append(max_y) 
      return True
    if y_vel < 0 and y < target_y_min:
      return False

target_x_min, target_x_max = 81, 129 #20, 30
target_y_min, target_y_max = -150, -108 #-10, -5

max_h = []
works_count = 0
for x in range(target_x_max):
  for y in range(target_y_min, 250):
    if simulate(x,y, target_x_min, target_x_max, target_y_min, target_y_max ):
      works_count += 1
print(works_count)

max(max_h)
target area: x=81..129, y=-150..-108


len(max_h)

## ───────────────────────────────────── ▼ ─────────────────────────────────────
# {{{                             --          --
#···············································································
def simulate(x_vel, y_vel, target_x_min, target_x_max, target_y_min, target_y_max):
  x = 0
  y = 0
  max_y = 0
  while True:
    x += x_vel
    y += y_vel
    max_y = max(max_y, y)
    x_vel = max(x_vel-1, 0)
    y_vel -= 1
    if target_x_min <= x <= target_x_max and target_y_min <= y <= target_y_max:
      return True
    if y_vel < 0 and y < target_y_min:
      return False

target_x_min, target_x_max = 81, 129 #20, 30
target_y_min, target_y_max = -150, -108 #-10, -5

works_count = 0
for x in range(-1000, 1000):
  for y in range(-1000, 1000):
    if simulate(x,y, target_x_min, target_x_max, target_y_min, target_y_max ):
      works_count += 1
print(works_count)
#                                                                            }}}
## ─────────────────────────────────────────────────────────────────────────────



## ───────────────────────────────────── ▼ ─────────────────────────────────────
# {{{                             --          --
#···············································································






def launch(xv, yv):
    highest_y = -math.inf
    x, y = 0, 0
    for _ in range(1000):
        x += xv
        y += yv
        highest_y = max(highest_y, y)

        if 81 <= x <= 129 and -150 <= y <= -108:
            return True
        if yv < 0 and y < -1505:
            return False
        if xv > 0 and x > 120:
            return False
        if xv == 0 and (x < 81 or x > 129):
            return False

        if xv != 0:
            xv = (xv - 1) if xv > 0 else (xv + 1)
        yv -= 1

    return False

ans = 0
for vx in range(-1000, 1000):
    for vy in range(-1000, 1000):
        ans += launch(vx, vy)
    print(ans)










#                                                                            }}}
## ─────────────────────────────────────────────────────────────────────────────


