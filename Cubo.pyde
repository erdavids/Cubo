w, h = 1601, 801
tile_size = 20

grid_w = int(w/tile_size)
grid_h = int(h/tile_size)

line_width = 1

# Background tile colors
bc = (255, 255, 255)
bl = (0, 0, 0)

# Cube Colors
cf = (255, 255, 255)
cl = (0, 0, 0)
ct = (255, 255, 255)
ctl = (0, 0, 0)
cs = (0, 0, 0)



def setup():
    size(w, h)
    global img
    img = createImage(w, h, ARGB)
    
    grid = []
    white_list = []
    for c in range(grid_w):
        grid.append([])
        for r in range(grid_h):
            chance = random(1)
            if c == 0 or r == 0 or r == 1 or c == grid_w - 1 or r == grid_h - 1 or c == grid_w - 2:
                grid[c].append(7)
            elif chance < .5:
                grid[c].append(7)
            else:
                grid[c].append(1)
                white_list.append((c, r))
                
                        
                
    print(white_list)
    
    background(bc[0], bc[1], bc[2])
    
    strokeWeight(line_width)
    
    # Rules
    for e in white_list:
        # Left of Right
        if e[0] < grid_w - 1:
            if grid[e[0] + 1][e[1]] != 1:
                grid[e[0] + 1][e[1]] = 4
                # Check for white squares beneath
                if e[1] < grid_h -1:
                    if(grid[e[0]][e[1]+1] == 1):
                           grid[e[0]+1][e[1]] = 6
                    if(grid[e[0]+1][e[1]+1] == 1):
                           grid[e[0]+1][e[1]] = 8
                           
            
        if e[1] > 0:
            if grid[e[0]][e[1] - 1] != 1:
                grid[e[0]][e[1] - 1] = 2
                # right of left
                if e[0] > 0:
                    if grid[e[0] - 1][e[1]] == 1:
                        grid[e[0]][e[1] - 1] = 5
                    if grid[e[0] - 1][e[1] - 1] == 1:
                        grid[e[0]][e[1] - 1] = 8
                if e[0] < grid_w - 1:
                    if grid[e[0]][e[1]-1] != 1 and grid[e[0]+1][e[1]-1] != 1 and grid[e[0]+1][e[1]] != 1:
                        grid[e[0]+1][e[1]-1] = 3
                
        if e[1] < grid_h - 1:
            if grid[e[0]][e[1] + 1] != 1:
                stroke(0)
                line(e[0] * tile_size, e[1] * tile_size + tile_size, e[0] * tile_size + tile_size, e[1] * tile_size + tile_size)

    
    # Drawing all the tiles
    for c in range(grid_w):
        for r in range(grid_h):
            if grid[c][r] == 1:
                draw_tile_one(c, r)
            if grid[c][r] == 2:
                draw_tile_two(c, r)
            if grid[c][r] == 3:
                draw_tile_three(c, r)
            if grid[c][r] == 4:
                draw_tile_four(c, r)
            if grid[c][r] == 5:
                draw_tile_five(c, r)
            if grid[c][r] == 6:
                draw_tile_six(c, r)
            if grid[c][r] == 7:
                draw_tile_seven(c, r)
            if grid[c][r] == 8:
                draw_tile_eight(c, r)
                
    for c in range(grid_w):
        for r in range(grid_h):
            if grid[c][r] == 7:
                draw_tile_seven(c, r)
    # Drawing white square borders           
    for e in white_list:
        # Right of left
        if e[0] > 0:
            if grid[e[0] - 1][e[1]] != 1:
                stroke(cl[0], cl[1], cl[2])
                line(e[0] * tile_size, e[1] * tile_size, e[0] * tile_size, e[1] * tile_size + tile_size)
        if e[0] < grid_w - 1:
            if grid[e[0] + 1][e[1]] != 1 and grid[e[0] + 1][e[1]] != 6:
                stroke(cl[0], cl[1], cl[2])
                line(e[0] * tile_size + tile_size, e[1] * tile_size, e[0] * tile_size + tile_size, e[1] * tile_size + tile_size)
        if e[1] > 0:
            if grid[e[0]][e[1] - 1] != 1:
                stroke(cl[0], cl[1], cl[2])
                line(e[0] * tile_size, e[1] * tile_size, e[0] * tile_size + tile_size, e[1] * tile_size)
                
        if e[1] < grid_h - 1:
            if grid[e[0]][e[1] + 1] != 1:
                stroke(cl[0], cl[1], cl[2])
                line(e[0] * tile_size, e[1] * tile_size + tile_size, e[0] * tile_size + tile_size, e[1] * tile_size + tile_size)

    
    seed = int(random(1600))
    save("Website/Cubo-" + str(grid_w) + "-" + str(grid_h) + "-" + str(seed) + ".png")
def draw_tile_one(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    fill(cf[0], cf[1], cf[2])
    noStroke()
    rect(x_p, y_p, x_p + tile_size, y_p + tile_size)
    
def draw_tile_two(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    draw_tile_five(x, y)
    
    fill(ct[0], ct[1], ct[2])
    stroke(bc[0], bc[1], bc[2])
    triangle(x_p, y_p, x_p + tile_size, y_p, x_p, y_p + tile_size)
    
    stroke(ctl[0], ctl[1], ctl[2])
    line(x_p, y_p + tile_size/2, x_p + tile_size/2, y_p)
    line(x_p, y_p + tile_size, x_p + tile_size, y_p)
    

# stripes and bottom right triangle
def draw_tile_three(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    delt = tile_size/9
    draw_tile_five(x, y)
    
    fill(cs[0], cs[1], cs[2])
    triangle(x_p, y_p + tile_size, x_p + tile_size, y_p, x_p + tile_size, y_p + tile_size)

def draw_tile_four(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    draw_tile_seven(x, y)
    fill(cs[0], cs[1], cs[2])
    stroke(bl[0], bl[1], bl[2])
    triangle(x_p, y_p, x_p + tile_size, y_p, x_p, y_p + tile_size)
    
def draw_tile_five(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    stroke(ctl[0], ctl[1], ctl[2])
    
    delt = tile_size/10
    for i in range(0, 10):
        line(x_p, y_p + (i*delt), x_p + tile_size, y_p + (i * delt))
        
def draw_tile_six(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    fill(cs[0], cs[1], cs[2])
    stroke(cs[0], cs[1], cs[2])
    rect(x_p, y_p, tile_size, tile_size)
    
def draw_tile_seven(x, y):
    x_p = x * tile_size
    y_p = y * tile_size

    stroke(bl[0], bl[1], bl[2])
    
    line(x_p, y_p + tile_size/2, x_p + tile_size/2, y_p)
    line(x_p, y_p + tile_size, x_p + tile_size, y_p)
    line(x_p + tile_size/2, y_p + tile_size, x_p + tile_size, y_p + tile_size/2)
    
def draw_tile_eight(x, y):
    x_p = x * tile_size
    y_p = y * tile_size
    
    draw_tile_five(x, y)
    
    fill(cs[0], cs[1], cs[2])
    triangle(x_p, y_p, x_p + tile_size, y_p, x_p, y_p + tile_size)

    
