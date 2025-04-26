import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
# df = pd.read_csv('netflix_titles_sample.csv')
df = pd.read_csv(r"C:\Users\hp\Desktop\Projects Python\Netflix Movie Analysis\netflix_titles_sample.csv")
# Display basic info 
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Fill Missing values (optional)
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown') 

# Filter only movies (if TV shows are included)
movies_df = df[df['type'] == 'Movie']

# Extract year from data_added
movies_df['year_added'] = pd.to_datetime(movies_df['date_added'], errors='coerce').dt.year

# 1. Top 10 Countries with most movies
top_countries = movies_df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index,palette="mako")
plt.title('Top 10 Countries with Most Movies on Netflix')
plt.xlabel('Number of Movies')
plt.ylabel('Country')
plt.show()

# 2. Number of Movies Added Each Year
plt.figure(figsize=(12,6))
movies_df['year_added'].value_counts().sort_index().plot(kind='bar', color='coral')
plt.title('Number of Movies Added Each Year')
plt.xlabel('Year Added')
plt.ylabel('Number of Movies')
plt.show()

# 3. Movies Rating Distribution
plt.figure(figsize=(10,5))
movies_df['rating'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Set3')
plt.title('Distribution of Movies Ratings')
plt.ylabel('')
plt.show()

# 4. Top 10 Directors
top_directors = movies_df['director'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_directors.values, y=top_directors.index, palette="flare")
plt.title('Top 10 Directors with Most Movies')
plt.xlabel('Number of Movies')
plt.ylabel('Director')
plt.show()

# 5. Most Common Genres
# Splitting the 'listed_in' column
from collections import Counter
genres = ','.join(movies_df['listed_in']).split(',')
genre_counts = Counter(genres)
common_genres = genre_counts.most_common(10)

# Convert to dataframe for plotting
genre_df = pd.DataFrame(common_genres, columns=['Genre', 'Count'])

plt.figure(figsize=(10,5))
sns.barplot(x='Count', y='Genre', data=genre_df, palette="rocket")
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()

# 6. Duration Distribution (Movie Lengths)
# Extract numeric duration (in minutes)
movies_df['duration_mins'] = movies_df['duration'].str.extract('(\d+)').astype(float)

plt.figure(figsize=(12,6))
sns.histplot(movies_df['duration_mins'], bins=30, kde=True, color='teal')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# 7. Word Cloud of Movie Titles
from wordcloud import WordCloud

wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(' '.join(movies_df['title']))

plt.figure(figsize=(15,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Netflix Movie Titles')
plt.show()