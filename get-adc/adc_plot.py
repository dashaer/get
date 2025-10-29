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

def plot_sampling_period_hist(time):
    t=[]
    for i in range(1,len(time)):
        t.append(time[i]-time[i-1])

    print(t)
    plt.figure(figsize=(10,6))
    plt.hist(t)

    plt.xlabel("time,s")
    plt.ylabel("количество измерений")
    plt.xlim(0,1)
    plt.grid(True)
    plt.show()