import matplotlib.pyplot as plt

def plot_voltage_vs_time(time,voltage,max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time,voltage)
    plt.xlabel("time,s")
    plt.ylabel("voltage, V")
    # plt.label("зависимость напряжения от времени")
    plt.xlim()
    plt.ylim()
    plt.grid(True)
    plt.show()

