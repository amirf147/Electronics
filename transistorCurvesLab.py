from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

vin_npn = [0, 0.5, 0.66, 0.7, 0.75, 0.77, 0.8, 0.82, 0.85, 0.88, 0.91, 0.94, 0.98,
       1, 1.04, 1.07, 1.1, 1.13, 1.16, 1.2, 1.23, 1.27, 1.3, 1.34, 1.38, 1.43,
       1.5, 1.54, 1.59, 1.83, 1.9, 2.04, 2.2, 2.4, 2.7, 3.23, 3.92, 4, 4.13, 4.2,
       4.34, 4.42, 4.5, 4.6, 4.8, 5]

vout_npn = [12, 12, 11.8, 11.4, 11, 10.7, 10.25, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6,
        5.5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0.4, 0.3, 0.2, 0.19, 0.18,
        0.17, 0.16, 0.15, 0.14, 0.13, 0.129, 0.128, 0.127, 0.126, 0.125, 0.124,
        0.123, 0.121, 0.119]

vin_pnp = [-0, -0.5, -0.64, -0.67, -0.7, -0.72, -0.74, -0.76, -0.78, -0.81,
           -0.83, -0.85, -0.87, -0.90, -0.92, -0.94, -0.97, -1, -1.02, -1.05,
           -1.09, -1.12, -1.16, -1.21, -1.27, -1.46, -2, -3, -4, -5, -6, -7, -8,
           -9, -10, -11, -12]

vout_pnp = [-12, -12, -11.5, -11, -10.5, -10, -9.5, -9, -8.5, -8, -7.5, -7,
            -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5,
            -0.25, -0.18, -0.142, -0.124, -0.113, -0.11, -0.1, -0.094,-0.09,
            -0.086, -0.083,-0.081]


dict_npn = {'Vin': vin_npn, 'Vout': vout_npn}
dict_pnp = {'Vin': vin_pnp, 'Vout': vout_pnp}

def graph_volts(values):

    """dict_npn or dict_pnp"""

    title = input("Enter the title of your graph: ")

    choice = input("is it npn or pnp?: ")
    
    plt.plot(values['Vin'], values['Vout'])
    plt.xlabel("Vin (Volts)")
    plt.ylabel("Vout (Volts)")
    plt.minorticks_on()
    plt.grid(b = 'true', which = 'both', axis = 'both', alpha = 0.2)
    plt.title(title)
    
    if choice == 'npn':

        plt.fill_between([0, 0.5], [11.8 , 11.8], [12.2, 12.2], color='lightblue',
                    alpha=0.5)

        plt.fill_between([0.5, 1.65], [12.2 , 12.2], color='lightgreen',
                    alpha=0.5)
    
        plt.fill_between([1.65, 5], [0.5 , 0.5], color='pink',
                    alpha=0.5)

    elif choice == 'pnp':

        plt.fill_between([0, 0.5], [11.8 , 11.8], [12.2, 12.2], color='lightblue',
                    alpha=0.5)

        plt.fill_between([0.5, 1.65], [12.2 , 12.2], color='lightgreen',
                    alpha=0.5)
    
        plt.fill_between([1.65, 5], [0.5 , 0.5], color='pink',
                    alpha=0.5)
        
    off = mpatches.Patch(color='lightblue', label='OFF')
    sat = mpatches.Patch(color='lightgreen', label='ACTIVE')
    active = mpatches.Patch(color='pink', label='SATURATED')
    plt.legend(handles=[off, sat, active])
    plt.show()
    


ib_npn = []
ic_npn = []


ib_pnp = []
ic_pnp = []

def volt_to_current_npn(values):

    for i in range(len(values['Vin'])):
        current_ib = round(((abs(values['Vin'][i]) - 0.65)/10000) * 1000000, 3)
        current_ic = round(((12 - abs(values['Vout'][i]))/1000) * 1000, 3)
        ic_npn.append(str(current_ic))
        ib_npn.append(str(current_ib))

def volt_to_current_pnp(values):

    for i in range(len(values['Vin'])):
        current_ib = round(((abs(values['Vin'][i]) - 0.65)/10000) * 1000000, 3)
        current_ic = round(((12 - abs(values['Vout'][i]))/1000) * 1000, 3)
        ic_pnp.append(str(current_ic))
        ib_pnp.append(str(current_ib))

table_npn = pd.DataFrame(dict_npn)
table_pnp = pd.DataFrame(dict_pnp)

volt_to_current_npn(dict_npn)
volt_to_current_pnp(dict_pnp)

dict_npn['Ib'] = ib_npn
dict_npn['Ic'] = ic_npn
dict_pnp['Ib'] = ib_pnp
dict_pnp['Ic'] = ic_pnp


def graph_currents(values):

    """dict_npn or dict_pnp"""

    title = input("Enter the title of your graph: ")
    
    plt.plot(values['Ib'], values['Ic'])

    plt.xlabel("I(B) (microAmps)")
    plt.ylabel("I(C) (milliAmps)")
    plt.grid(b = 'true', which = 'both', axis = 'both', alpha = 0.2)
    plt.title(title)
    ax = plt.axes()
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.yaxis.set_major_locator(plt.MaxNLocator(10))

    plt.show()

table_npn = pd.DataFrame(dict_npn)
table_pnp = pd.DataFrame(dict_pnp)
