
# Goal: have utils provide functions that automatically send all plots to
# streamlit.
# archived because there are a lot of edge cases

def sns_ax_stwrite(func):
    def wrapper(*args, **kwargs):
        fig, ax = plt.subplots()
        func(ax=ax, *args, **kwargs)
        st.write(plt.gcf())
    return wrapper

boxplot = sns_ax_stwrite(sns.boxplot)