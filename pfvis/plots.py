from matplotlib.pyplot import title, xlim, ylabel, show, gca, plot

from numpy import array
import seaborn
import ipyplots
import networkx as nx


def plot_graph(net):
    """
    Plots a nice D3 network graph

    :param net: a pfnet network
    :return: a IPython HTML object containing the graph
    """
    g = nx.Graph()
    g.add_nodes_from([bus.index for bus in net.buses])
    g.add_edges_from([(branch.bus_from.index, branch.bus_to.index) for branch in net.branches])
    return ipyplots.nx_graph_plot(g)


def plot_vargen_injection(mpnet):
    """
    Plots the aggregated injection by variable generators (renewable generation)

    :param mpnet: The MP-PFNET network
    """
    num_generators = mpnet.networks[0].num_vargens
    powers = [array([mpnet.networks[i].var_generators[n].P * mpnet.base_power * 1e3 for i in range(mpnet.timesteps)])
              for n in
              range(num_generators)]
    ipyplots.area_plot(powers, label="Vargen", title="Vargen Power", xlabel="Time [h]", ylabel='Vargen Power [kW]')


def plot_energy_price(mpnet, bus_index=0):
    """
    Plots the energy price.

    :param mpnet: The MP-PFNET network
    :param bus_index: The bus the price should be plotted for. (default: 0)
    """
    plot([mpnet.get_network(time=i).buses[bus_index].price / (mpnet.base_power * 1e3) for i in range(mpnet.timesteps)],
         color=seaborn.color_palette("muted", 1)[0])
    ylabel("EUR/kWh")
    title("Energy Price (EUR)")
    xlim([0, mpnet.timesteps])
    show()


def plot_load_power(mp):
    """
    Plots the aggregated load power

    :param mp: The MP-PFNET network
    """
    load_powers = [array([mp.networks[i].loads[load_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   load_id in range(mp.get_network().num_loads)]

    ipyplots.area_plot(load_powers, ylabel='Load Power [kW]', xlabel='Time [h]', title="Load Power")


def plot_power(mp):
    """
    Plots the aggregated power of all loads and generators including batteries.

    :param mp: The MP-PFNET network
    """
    load_powers = [array([mp.networks[i].loads[load_id].P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                   load_id in range(mp.get_network().num_loads)]
    load_powers += [array([battery.P_c * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                    battery in mp.get_network().batteries]
    gen_powers = [array([(-1) * generator.P * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                  generator in mp.get_network().generators]
    gen_powers += [array([(-1) * battery.P_d * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
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

    ipyplots.area_plot(battery_powers, ylabel='Charging Power [kW]', xlabel='Time [h]', title="Battery Charging Power")


def plot_battery_soc(mp):
    """
    

    :param mp:
    :return:
    """
    battery_socs = [array([mp.networks[i].batteries[bat_id].E * mp.base_power * 1e3 for i in range(mp.timesteps)]) for
                    bat_id in range(mp.get_network().num_bats)]
    ipyplots.area_plot(battery_socs, ylabel='SOC [kWh]', xlabel='Time [h]', title="Battery SOC")
