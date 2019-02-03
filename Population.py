import matplotlib
import matplotlib.pyplot as plt
plt.plot([2035,2030,2025,2020,2019,2015,2010,2005,2000,1995,1990,1985,1980,1975,1970,1965,1960,1955,1950],
         [19564170,17583604,15845219,14850066,14755186,14422670,14002798,13595152,13097153,11992194,10974177,
          10003665,9100166,8165629,7329372,6589384,5910210,5219086,4604143],'-.',label='Population')
#You need to call legend fuction to display the label in the graph
plt.legend()
plt.title("Population Graph",size=25,color='blue')
#Putting a variable to initialize the fonts
font = {'family': 'serif','color':  'darkred','weight': 'normal'}
#use font dictionary "fontdict" function to change the fonts ...note that you could have added the size inside the font variable
plt.xlabel("Year",size=20,fontdict=font)
plt.ylabel("Population",size=20,fontdict=font)
#To write text in the graph just use plt.text(x,y,"text",size="",rotation="",ha="left/right/center(with respect to x)",va="center/top/down(with respect to y)")
plt.text(1960, 17583604, "Population vs Year", size=10, rotation=0.,
         ha="left", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
#To remove axis values to 1E7
plt.ticklabel_format(style = 'plain') 
plt.show()
