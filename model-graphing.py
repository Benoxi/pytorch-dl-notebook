import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

model_name = "model-1582833658"

def create_acc_loss_graph(model_name):
    contents = open("model.log", "r").read().split('\n') # Open our model file for reading and split every line

    times = [] # this is our X axis
    # everything else we want to know how it behaves over time
    accuracies = []
    losses = []
    val_accs = []
    val_losses = []

    for c in contents: 
        if model_name in c:
            name, timestamp, acc, loss, val_acc, val_loss = c.split(",")

            times.append(float(timestamp)) # Everything is a string! CONVER TO FLOAT
            accuracies.append(float(acc))
            losses.append(float(loss))
            val_accs.append(float(val_acc))
            val_losses.append(float(val_loss))

    fig = plt.figure()
    # each axis is a graph
    ax1 = plt.subplot2grid((2, 1), (0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)

    ax1.plot(times, accuracies, label="acc")
    ax1.plot(times, val_accs, label="val_acc")
    ax1.legend(loc=2) # should be out of the way if the training was successful :P

    ax2.plot(times, losses, label="loss")
    ax2.plot(times, val_losses, label="val_loss")
    ax2.legend(loc=2)

    plt.show()
    

create_acc_loss_graph(model_name)