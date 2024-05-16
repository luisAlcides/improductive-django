from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import io


def chart_view():
    goal_data = [("Goal 1", 5), ("Goal 2", 10), ("Goal 3", 7)]
    study_day = [("Goal 1", 1), ("Goal 2", 8), ("Goal 3", 5), ("Other", 2)]

    plt.rcParams.update({
        "axes.facecolor": "#2e2e2e",  # Fondo de los ejes
        "axes.edgecolor": "white",    # Color del borde de los ejes
        "axes.labelcolor": "white",   # Color de las etiquetas de los ejes
        "figure.facecolor": "#2e2e2e",  # Fondo de la figura
        "xtick.color": "white",       # Color de los ticks en el eje x
        "ytick.color": "white",       # Color de los ticks en el eje y
        "text.color": "white",        # Color del texto
        "legend.facecolor": "#2e2e2e",  # Fondo de la leyenda
        "legend.edgecolor": "white",  # Borde de la leyenda
    })

    fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
    ax.set_title('Study Goals and Progress')
    ax.set_xlabel('Goals')
    ax.set_ylabel('Hours')
    legend_labels = ['Goal', 'Habit with Goal', '< 30% Goal',
                     '30%-50% Goal', '> 50% Goal']
    legend_colors = ["#C0BEBC", '#448BDB', "#FA5F4B", "#F9EC8A", "#73FA8E"]
    goals_name = ''

    if goal_data:
        goals = [float(data[1]) for data in goal_data if len(data) >= 1]
        goals_name = [data[0] for data in goal_data if len(data) >= 1]

        ax.barh(
            goals_name,
            goals,
            color=legend_colors[0],
            edgecolor='black',
            label='Goals',
            height=0.5,
            alpha=0.8)

    if study_day:
        habits = [float(data[1]) for data in study_day if len(data) >= 1]
        habits_name = [data[0] for data in study_day if len(data) >= 1]

        studied_hours = [float(data[1])
                         for data in study_day if len(data) >= 1]
        colors = []

        for i in range(len(habits)):
            habit_name = habits_name[i]
            if habit_name in goals_name:
                goal_index = goals_name.index(habit_name)
                goal = goals[goal_index]
                percentage = (studied_hours[i] /
                              goal) * 100 if goal != 0 else 0
                if percentage <= 30:
                    colors.append(legend_colors[2])
                elif percentage < 50:
                    colors.append(legend_colors[3])
                elif percentage >= 50:
                    colors.append(legend_colors[4])

                else:
                    colors.append(legend_colors[1])
        ax.barh(
            habits_name,
            habits,
            color=colors,
            edgecolor='black',
            label='Studied Hours',
            height=0.5,
            alpha=0.8)

        legend_handles = [plt.Rectangle(
            (0, 0), 1, 1, color=color) for color in legend_colors]
        ax.legend(legend_handles, legend_labels,
                  loc='upper right', fontsize=12)

        canvas = FigureCanvas(fig)
        buffer = io.BytesIO()
        canvas.print_png(buffer)
        plt.close(fig)
        return buffer.getvalue()
