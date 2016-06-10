from matplotlib.pyplot import title, ylim, xlim, ylabel, xlabel, show, gca, plot

from numpy import zeros, array, max
import seaborn
import ipyplots

def plot_vargen_injection(mpnet):
    N = mpnet.networks[0].num_vargens
    powers = [array([mpnet.networks[i].var_generators[n].P * mpnet.base_power * 1e3 for i in range(mpnet.timesteps)]) for n in
              range(N)]
    ipyplots.area_plot(powers ,label="Vargen", title="Vargen Power", xlabel="Time [h]", ylabel='Vargen Power [kW]')

def plot_energy_price(mpnet):
    plot([mpnet.get_network(time=i).buses[0].price for i in range(mpnet.timesteps)],
         color=seaborn.color_palette("muted", 1)[0])
    title("Energy Price (EUR)")
    xlim([0, mpnet.timesteps])
    show()

def plot_load_power(mp):
    load_powers = [array([mp.networks[i].loads[load_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   load_id in range(mp.get_network().num_loads)]

    ipyplots.area_plot(load_powers, ylabel='Load Power [kW]', xlabel='Time [h]', title="Load Power")

def plot_power(mp):
    seaborn.set_style("whitegrid")

    ax = gca()

    load_powers = [array([mp.networks[i].loads[load_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   load_id in range(mp.get_network().num_loads)]
    load_powers += [array([battery.P_c * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   battery in mp.get_network().batteries]
    gen_powers = [array([(-1) * generator.P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
               generator in mp.get_network().generators]
    gen_powers += [array([(-1) *  battery.P_d * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   battery in mp.get_network().batteries]

    ipyplots.area_plot(load_powers, label="Load", hold=True)
    ipyplots.area_plot(gen_powers, label="Load", ylabel="Power [kW]", xlabel='Time [h]', title="Power")

def plot_battery_power(mp):
    """
    Plots the battery power injection of all batteries in the MP-Pfnet network.
    :param mp: The MP-PFNET network
    """

    battery_powers = [array([mp.networks[i].batteries[bat_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                     bat_id in range(mp.get_network().num_bats)]


    ipyplots.area_plot(battery_powers, ylabel='Charging Power [kW]', xlabel='Time [h]',  title="Battery Charging Power")


def plot_battery_soc(mp):
    battery_socs = [array([mp.networks[i].batteries[bat_id].E * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   bat_id in range(mp.get_network().num_bats)]
    ipyplots.area_plot(battery_socs, ylabel='SOC [kWh]', xlabel='Time [h]', title="Battery SOC")
