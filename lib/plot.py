import matplotlib.pyplot as plt

def init_fig_with_coord():
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    # Eliminate upper and right 
    
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    return ax