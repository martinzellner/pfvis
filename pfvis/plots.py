from matplotlib.pyplot import title, ylim, xlim, ylabel, xlabel, show, gca, plot

from numpy import zeros, array, max
import seaborn


def plot_vargen_injection(mpnet):
    seaborn.set_style("whitegrid")

    ax = gca()

    N = mpnet.networks[0].num_vargens

    powers = [array([mpnet.networks[i].var_generators[n].P * mpnet.base_power * 1e3 for i in range(mpnet.timesteps)]) for n in
              range(N)]

    for i, power in enumerate(powers):
        previous = zeros((mpnet.timesteps,))
        for n in range(i):
            previous += powers[n]
        ax.fill_between(range(mpnet.timesteps), previous, previous + power, lw=0.3, alpha=0.5, edgecolor='black',
                        facecolor=seaborn.color_palette("muted", N)[i], label="Vargen {}".format(i))

    ylim([0, sum([max(power) for power in powers]) * 1.1])
    xlim([0, mpnet.timesteps])

    # legend(loc='right')
    ylabel('Vargen Power [kW]')
    xlabel('Time [h]')
    title("Vargen Power")
    show()

def plot_energy_price(mpnet):
    plot([mpnet.get_network(time=i).buses[0].price for i in range(mpnet.timesteps)],
         color=seaborn.color_palette("muted", 1)[0])
    title("Energy Price (EUR)")
    xlim([0, mpnet.timesteps])
    show()

def plot_load_power(mp):
    seaborn.set_style("whitegrid")

    ax = gca()

    load_powers = [array([mp.networks[i].loads[load_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   load_id in range(mp.get_network().num_loads)]

    for i, load_power in enumerate(load_powers):
        previous_loads = zeros((mp.timesteps,))
        for n in range(i):
            previous_loads += load_powers[n]
        ax.fill_between(range(mp.timesteps), previous_loads, previous_loads + load_power, lw=0.3, alpha=0.5,
                        edgecolor='black', facecolor=seaborn.color_palette("muted", mp.networks[i].num_loads)[i],
                        label="Load {}".format(i))

    #ylim([0, sum([max(power) for power in load_powers]) * 1.1 ])
    xlim([0, mp.timesteps])

    # legend(loc='right')
    ylabel('Load Power [kW]')
    xlabel('Time [h]')
    title("Load Power")
    show()

def plot_battery_power(mp):
    seaborn.set_style("whitegrid")

    ax = gca()

    battery_power = [array([mp.networks[i].batteries[bat_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                     bat_id in range(mp.get_network().num_bats)]

    for i, power in enumerate(battery_power):
        previous = zeros((mp.timesteps,))
        for n in range(i):
            previous += battery_power[n]
        ax.fill_between(range(mp.timesteps), previous, previous + power, lw=0.3, alpha=0.7, edgecolor='black',
                        facecolor=seaborn.color_palette("muted", mp.networks[i].num_bats)[i],
                        label="Battery {}".format(i))
#    ylim([-310, 310])
    xlim([0, mp.timesteps])

    # legend(loc='right')
    ylabel('Power Injection [kW]')
    xlabel('Time [h]')
    title("Battery Charging Power")
    show()

def plot_battery_soc(mp):
    seaborn.set_style("whitegrid")

    ax = gca()

    battery_soc = [array([mp.networks[i].batteries[bat_id].E * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   bat_id in range(mp.get_network().num_bats)]

    for i, soc in enumerate(battery_soc):
        previous = zeros((mp.timesteps,))
        for n in range(i):
            previous += battery_soc[n]
        ax.fill_between(range(mp.timesteps), previous, previous + soc, lw=0.3, alpha=0.7, edgecolor='black',
                        facecolor=seaborn.color_palette("muted", mp.networks[i].num_bats)[i],
                        label="Battery {}".format(i))
    #ylim([0, 350])
    xlim([0, mp.timesteps])

    # legend(loc='right')
    ylabel('SOC [kWh]')
    xlabel('Time [h]')
    title("Battery SOC")
    show()