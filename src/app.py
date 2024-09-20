

df = pd.read_csv("https://raw.githubusercontent.com/4GeeksAcademy/decision-tree-project-tutorial/main/diabetes.csv", sep = ",")
df.head()

df = df.drop_duplicates().reset_index(drop = True)
df.head()

df.hist(figsize=(12, 10), bins=20, color="#E58139")
plt.suptitle("Histograms of Numeric Features")
plt.show()