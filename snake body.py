import turtle

body = {(0, 0)}
def build_grid():
    for x in range(12):
        x +=1
        for y in range(9):
            y += 1
            body.append((x, y))
        y = 0
    return body
build_grid()
print(body)