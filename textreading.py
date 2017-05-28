import turtle
#open text file and assign it to a variable
def lab_data():
    '''get data from labdata.text and place each line in a list as x,y coordinates'''
    lab_text = open("labdata.txt", "r")
    plot_list = []

    for line in lab_text:
        list_line = line.split()
        plot_list.append((list_line[0], list_line[1]))
    return plot_list

#iterate through the text file and set first number to x, second to y
#assign each pair to a list
#create a turtle
def draw_turtle(trt, points):
    xsum = 0
    ysum = 0
    for i in range(len(points)):
        trt.setpos(points[i])
        trt.stamp()
        xsum += int(points[i][0])
        ysum += int(points[i][1])    
    #draw best fit line
    trt.setpos(0, 0)
    trt.pendown()
    trt.setpos(xsum / len(points), ysum / len(points))



def main():
    '''define turtle and window, call starting functions'''
    t = turtle.Turtle()
    t.shape("circle")
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, 100, 100)
    t.penup()
    wn.exitonclick()

    draw_turtle(t, lab_data())

main()




#create a window sized based on min/max #'s from the list
#plot the points in the window with a turtle
#draw a 'best fit' line that goes through the points

